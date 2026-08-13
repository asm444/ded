"""Valida uma ficha de personagem contra as regras aritmeticas de D&D 2024.

Checa o que e' decidivel por calculo; o que depende de arbitragem fica de fora.
Uso: `validar_ficha.py fichas/<nome>.json`. Sai 0 se a ficha passa, 1 se falha.
"""
import json
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).parent.parent
ATRIBUTOS = ("forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma")
DADO_DE_VIDA = {"barbaro": 12, "bardo": 8, "bruxo": 8, "clerigo": 8, "druida": 8,
                "feiticeiro": 6, "guardiao": 10, "guerreiro": 10, "ladino": 8,
                "mago": 6, "monge": 8, "paladino": 10}
CUSTO_COMPRA = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}
OBRIGATORIOS = ("nome", "classe", "nivel", "atributos", "pv_maximo", "ca")


def sem_acento(texto):
    base = unicodedata.normalize("NFKD", str(texto)).encode("ascii", "ignore").decode()
    return base.lower().strip()


def modificador(valor):
    return (valor - 10) // 2


def bonus_de_proficiencia(nivel):
    return 2 + (nivel - 1) // 4


def validar(ficha):
    """Lista de falhas; vazia significa ficha valida."""
    falhas = []
    for campo in OBRIGATORIOS:
        if campo not in ficha:
            falhas.append(f"campo obrigatorio ausente: {campo}")
    if falhas:
        return falhas

    nivel = ficha["nivel"]
    if not 1 <= nivel <= 20:
        falhas.append(f"nivel {nivel} fora de 1..20")

    classe = sem_acento(ficha["classe"])
    if classe not in DADO_DE_VIDA:
        falhas.append(f"classe desconhecida: {ficha['classe']}")
    if not (RAIZ / "docs" / "classes" / f"{classe}.md").exists():
        falhas.append(f"sem doc para a classe: docs/classes/{classe}.md")

    atributos = ficha["atributos"]
    for nome in ATRIBUTOS:
        if nome not in atributos:
            falhas.append(f"atributo ausente: {nome}")
        elif not 1 <= atributos[nome] <= 20:
            falhas.append(f"{nome} = {atributos[nome]} fora de 1..20 (nivel 1..20 sem magia)")
    if falhas:
        return falhas

    esperado = bonus_de_proficiencia(nivel)
    if ficha.get("bonus_proficiencia", esperado) != esperado:
        falhas.append(f"bonus de proficiencia {ficha['bonus_proficiencia']} != {esperado} para o nivel {nivel}")

    dado = DADO_DE_VIDA.get(classe)
    if dado:
        con = modificador(atributos["constituicao"])
        maximo = dado + con + (nivel - 1) * (dado // 2 + 1 + con)
        minimo = dado + con + (nivel - 1) * (1 + con)
        if not minimo <= ficha["pv_maximo"] <= maximo:
            falhas.append(f"pv_maximo {ficha['pv_maximo']} fora de {minimo}..{maximo} "
                          f"(d{dado}, Con {con:+d}, nivel {nivel})")

    if ficha["ca"] < 10 + min(0, modificador(atributos["destreza"])):
        falhas.append(f"ca {ficha['ca']} abaixo do minimo possivel")

    base = ficha.get("atributos_base")
    if base:
        custo = sum(CUSTO_COMPRA.get(v, -1) for v in base.values())
        if any(CUSTO_COMPRA.get(v, -1) < 0 for v in base.values()):
            falhas.append("atributos_base fora de 8..15: nao e' compra por pontos valida")
        elif custo > 27:
            falhas.append(f"compra por pontos custa {custo}, teto e' 27")

    for magia in ficha.get("magias", []):
        if not isinstance(magia, dict) or "nome" not in magia:
            falhas.append(f"magia sem nome: {magia!r}")

    return falhas


def main():
    if len(sys.argv) < 2:
        print("uso: validar_ficha.py <ficha.json>")
        return 2
    caminho = Path(sys.argv[1])
    ficha = json.loads(caminho.read_text(encoding="utf-8"))
    falhas = validar(ficha)
    if falhas:
        print(f"REPROVADA: {caminho} ({len(falhas)} falhas)")
        for f in falhas:
            print(f"  - {f}")
        return 1
    print(f"APROVADA: {caminho} — {ficha['nome']}, {ficha['classe']} nivel {ficha['nivel']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
