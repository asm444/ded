"""Gera os .md de docs/ a partir da marcacao produzida por extrair.py.

Emite regras — headings, caracteristicas, tabelas; a prosa de sabor fica de fora.
Uso: `gerar_docs.py <dominio>` ou `gerar_docs.py todos`.
"""
import re
import sys
from pathlib import Path

import pymupdf

sys.path.insert(0, str(Path(__file__).parent))
import extrair

RAIZ = Path(__file__).parent.parent
# dominio -> (subpasta, [(arquivo, titulo, pag_ini, pag_fim)], manter_prosa)
CLASSES = [
    ("barbaro", "Bárbaro", 51, 57), ("bardo", "Bardo", 59, 67),
    ("bruxo", "Bruxo", 69, 79), ("clerigo", "Clérigo", 81, 89),
    ("druida", "Druida", 91, 101), ("feiticeiro", "Feiticeiro", 103, 115),
    ("guardiao", "Guardião", 117, 125), ("guerreiro", "Guerreiro", 127, 135),
    ("ladino", "Ladino", 137, 145), ("mago", "Mago", 147, 157),
    ("monge", "Monge", 159, 165), ("paladino", "Paladino", 167, 175),
]
REGRAS = [
    ("fundamentos", "Fundamentos: Dados, Atributos e Testes de D20", 8, 13),
    ("acoes", "Ações", 14, 15),
    ("interacao-social", "Interação Social", 15, 18),
    ("exploracao", "Exploração", 19, 22),
    ("combate", "Combate", 23, 26),
    ("dano-e-cura", "Dano e Cura", 27, 28),
    ("condicoes", "Condições", 29, 31),
    ("glossario", "Glossário de Regras", 360, 377),
]
DOMINIOS = {
    "regras": ("regras", REGRAS, True),
    "classes": ("classes", CLASSES, False),
    "personagem": ("personagem", [
        ("criacao", "Criando Seu Personagem", 33, 40),
        ("avanco-de-nivel", "Avanço de Nível", 41, 43),
        ("multiclasse", "Multiclasse", 44, 45),
        ("bugigangas", "Bugigangas", 46, 47),
    ], True),
    "origens": ("especies", [
        ("antecedentes", "Antecedentes", 177, 185),
        ("especies", "Espécies", 186, 197),
    ], True),
    "talentos": ("talentos", [("talentos", "Talentos", 199, 211)], True),
    "equipamento": ("equipamento", [("equipamento", "Equipamento", 213, 233)], True),
    "magias": ("magias", [
        ("regras-de-conjuracao", "Adquirindo e Conjurando Magias", 235, 238),
        ("descricoes", "Descrições das Magias", 239, 343),
    ], True),
    "apendices": ("apendices", [
        ("multiverso", "O Multiverso", 344, 345),
        ("criaturas", "Estatísticas de Criaturas", 346, 359),
    ], True),
}
# Marcadores de que a secao entrou em conteudo de regra (encerra a prosa de abertura).
INICIO_REGRA = re.compile(r"^(N[íi]vel \d+:|Tra[çc]os B[áa]sicos|Caracter[íi]sticas de|Subclasse)", re.I)


def limpar(paragrafo):
    """Junta hifenizacao de quebra de linha e normaliza espacos."""
    texto = re.sub(r"(\w)-[^\S\n]+(?=[a-záàâãéêíóôõúç])", r"\1", paragrafo)
    return re.sub(r"[^\S\n]+", " ", texto).strip()


def blocos(linhas):
    """Agrupa linhas consecutivas de mesmo papel; run-in acompanha o paragrafo."""
    saida = []
    for linha in linhas:
        alvo = "corpo" if linha["papel"] == "runin" else linha["papel"]
        if saida and saida[-1][0] == alvo and alvo in ("corpo", "tabela"):
            saida[-1][1].append(linha)
        else:
            saida.append([alvo, [linha]])
    return saida


def texto_do_paragrafo(grupo):
    """Junta as linhas do paragrafo, marcando run-in em negrito e restaurando a capitular."""
    partes = []
    for linha in grupo:
        if linha["papel"] == "runin":
            partes.append("\n\n")                      # run-in abre um novo paragrafo
        for bruto, negrito in linha["trechos"]:
            partes.append(f"**{bruto.strip()}** " if negrito else bruto)
        partes.append(" ")
    texto = limpar("".join(partes)).replace("** **", " ")
    texto = re.sub(r"(?:^|(?<=\n))([A-ZÁÂÃÉÊÍÓÔÕÚÇ])\s+(?=[a-záâãéêíóôõúç])", r"\1", texto)
    return re.sub(r"\s*•\s*", "\n- ", texto).strip()


def markdown_tabela(matriz):
    largura = max(len(l) for l in matriz)
    if largura < 2 or len(matriz) < 2:
        return "\n".join(" ".join(l) for l in matriz)
    corpo = [l + [""] * (largura - len(l)) for l in matriz]
    cab = corpo[0] if len(set(len(l) for l in matriz)) > 1 else corpo[0]
    linhas = ["| " + " | ".join(cab) + " |", "|" + "---|" * largura]
    linhas += ["| " + " | ".join(c) + " |" for c in corpo[1:]]
    return "\n".join(linhas)


def gerar(doc, arquivo, titulo, ini, fim, manter_prosa):
    partes = [f"# {titulo}", "", f"> Livro do Jogador (2024), p. {ini}–{fim}.", ""]
    em_regra = manter_prosa
    for pagina, linhas in extrair.paginas_marcadas(doc, ini, fim):
        for tipo, grupo in blocos(linhas):
            texto = " ".join(l["texto"] for l in grupo)
            if tipo.startswith("h"):
                nivel = int(tipo[1])
                if INICIO_REGRA.match(texto):
                    em_regra = True
                partes += ["", "#" * min(nivel + 1, 6) + f" {texto}", ""]
            elif tipo == "tabela":
                partes += ["", markdown_tabela(extrair.montar_tabela(grupo)), ""]
            elif em_regra:
                partes.append(texto_do_paragrafo(grupo))
    conteudo = re.sub(r"\n{3,}", "\n\n", "\n".join(partes)).strip() + "\n"
    return conteudo


def main():
    doc = pymupdf.open(RAIZ / extrair.PDF)
    alvo = sys.argv[1] if len(sys.argv) > 1 else "todos"
    escolhidos = DOMINIOS if alvo == "todos" else {alvo: DOMINIOS[alvo]}
    for nome, (pasta, secoes, prosa) in escolhidos.items():
        destino = RAIZ / "docs" / pasta
        destino.mkdir(parents=True, exist_ok=True)
        for arquivo, titulo, ini, fim in secoes:
            conteudo = gerar(doc, arquivo, titulo, ini, fim, prosa)
            caminho = destino / f"{arquivo}.md"
            caminho.write_text(conteudo, encoding="utf-8")
            print(f"{caminho.relative_to(RAIZ)}\t{len(conteudo):>7} bytes")


if __name__ == "__main__":
    main()
