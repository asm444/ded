"""Extrai estrutura e texto do Livro do Jogador (2024) pela tipografia do PDF.

O papel de cada linha e' decidido pela fonte, nao por heuristica sobre o texto.
Uso: `extrair.py sumario` | `extrair.py texto <pag_inicial> <pag_final>`.
"""
import re
import sys
import unicodedata

import pymupdf

PDF = "DnD 5.5 - Livro do Jogador (2024)(Fundo Branco) - Erratas Agosto (1).pdf"
OFFSET = 6          # pagina impressa + OFFSET = indice fisico 0-based + 1
MEIO = 290.0        # vale entre as duas colunas do miolo (esq ~40-80, dir ~300-350)
PAG_SUMARIO = 8

# (fonte, corpo arredondado) -> nivel de heading
HEADINGS = {
    ("WolpePegasus-Regular", 64): 1,
    ("WolpePegasus-Regular", 38): 1,
    ("MrsEavesOT-Roman", 18): 2,
    ("ModestoW01-LiteCond", 18): 2,
    ("MrsEavesOT-Roman", 15): 3,
    ("ScalaSansCaps-Bold", 13): 3,
    ("MrsEavesOT-Roman", 13): 4,
    ("MrsEavesOT-Roman", 12): 4,
    ("ScalaSansCaps-Bold", 11): 5,
    ("ScalaSansCaps-Bold", 10): 5,
}
RUNIN = {("TTJenevers-BoldItalic", 9)}                    # titulo embutido no paragrafo
ROTULO = {("ScalaSans-BoldLF", 9), ("ScalaSans-BoldLF", 10)}   # rotulo de celula de tabela


def descartavel(fonte, corpo, texto):
    """Cabecalho corrido, numero de pagina, credito de arte e rotulo de capitulo."""
    if fonte.startswith("DaiVernon"):      # titulo decorativo, defasado em uma pagina
        return True
    if fonte == "MrsEavesOT-Bold" or corpo <= 5:
        return True
    if fonte == "WolpePegasus-Regular" and corpo == 15:
        return True
    if re.fullmatch(r"(CAP[IÍ]TULO|AP[EÊ]NDICE)\s+[A-Z0-9]+.*", texto, re.I):
        return True
    return texto.isupper() and "|" in texto


def linhas_da_pagina(doc, fisica):
    """Linhas em ordem de leitura: coluna esquerda inteira, depois a direita."""
    saida = []
    for bloco in doc[fisica].get_text("dict")["blocks"]:
        for linha in bloco.get("lines", []):
            texto = re.sub(r"\s+", " ", "".join(s["text"] for s in linha["spans"])).strip()
            if not texto:
                continue
            span = linha["spans"][0]
            x0, y0 = linha["bbox"][0], linha["bbox"][1]
            trechos = []
            for s in linha["spans"]:
                bruto = re.sub(r"\s+", " ", s["text"])
                if bruto.strip():
                    trechos.append((bruto, "Bold" in s["font"]))
            saida.append({
                "texto": texto, "fonte": span["font"], "corpo": round(span["size"]),
                "x": round(x0), "y": round(y0), "coluna": 0 if x0 < MEIO else 1,
                "trechos": trechos,
            })
    saida.sort(key=lambda l: (l["coluna"], l["y"], l["x"]))
    vistos, unicas = set(), []
    for linha in saida:                    # a arte repete texto em camadas sobrepostas
        chave = (linha["texto"], linha["y"], linha["x"], linha["fonte"])
        if chave not in vistos:
            vistos.add(chave)
            unicas.append(linha)
    return unicas


def papel(linha):
    """h1..h5, runin, tabela, corpo — ou None para descartar."""
    fonte, corpo, texto = linha["fonte"], linha["corpo"], linha["texto"]
    if descartavel(fonte, corpo, texto):
        return None
    nivel = HEADINGS.get((fonte, corpo))
    if nivel:
        return f"h{nivel}"
    if (fonte, corpo) in RUNIN:
        return "runin"
    if (fonte, corpo) in ROTULO or (fonte.split("-")[0] in ("ScalaSans", "ScalaSansCaps") and corpo <= 9):
        return "tabela"
    return "corpo"


def juntar_headings(marcadas):
    """Titulo quebrado em varias linhas vira um heading so."""
    saida = []
    for linha in marcadas:
        ant = saida[-1] if saida else None
        continua = (
            ant and ant["papel"] == linha["papel"] and linha["papel"].startswith("h")
            and ant["fonte"] == linha["fonte"] and ant["corpo"] == linha["corpo"]
            and 0 < linha["y"] - ant["y"] <= linha["corpo"] * 1.9
        )
        if continua:
            ant["texto"] += " " + linha["texto"]
            ant["y"] = linha["y"]
        else:
            saida.append(dict(linha))
    return saida


def colunas_de(linhas, folga=12):
    """Posicoes x das colunas, agrupando inicios proximos."""
    eixos = []
    for x in sorted(l["x"] for l in linhas):
        if not eixos or x - eixos[-1] > folga:
            eixos.append(x)
    return eixos


def montar_tabela(linhas, tolerancia=4):
    """Matriz de celulas: y agrupa a linha, x define a coluna, faixa sem coluna 0 continua a anterior."""
    faixas = []
    for linha in sorted(linhas, key=lambda l: (l["y"], l["x"])):
        if faixas and abs(linha["y"] - faixas[-1][0]["y"]) <= tolerancia:
            faixas[-1].append(linha)
        else:
            faixas.append([linha])
    eixos = colunas_de(linhas)
    matriz = []
    for faixa in faixas:
        celulas = [""] * len(eixos)
        for item in faixa:
            idx = min(range(len(eixos)), key=lambda i: abs(eixos[i] - item["x"]))
            celulas[idx] = (celulas[idx] + " " + item["texto"]).strip()
        if matriz and not celulas[0]:                 # continuacao da linha anterior
            for i, valor in enumerate(celulas):
                if valor:
                    matriz[-1][i] = (matriz[-1][i] + " " + valor).strip()
        else:
            matriz.append(celulas)
    return matriz


def paginas_marcadas(doc, ini, fim):
    """Linhas das paginas impressas [ini, fim] com o papel ja atribuido."""
    for impressa in range(ini, fim + 1):
        fisica = impressa + OFFSET - 1
        if not 0 <= fisica < len(doc):
            continue
        marcadas = []
        for linha in linhas_da_pagina(doc, fisica):
            p = papel(linha)
            if p:
                linha["papel"] = p
                marcadas.append(linha)
        yield impressa, juntar_headings(marcadas)


def ler_sumario(doc):
    """Indice do livro: nivel, titulo e pagina, na ordem de leitura das tres colunas."""
    itens = []
    for bloco in doc[PAG_SUMARIO].get_text("dict")["blocks"]:
        for linha in bloco.get("lines", []):
            bruto = "".join(s["text"] for s in linha["spans"])
            texto = re.sub(r"[.\s]{2,}", " ", bruto).strip()
            casa = re.match(r"^(.*?)\s+(\d{1,3})$", texto)
            if not casa or texto == "Sumário":
                continue
            x = linha["bbox"][0]
            coluna = 0 if x < 230 else (1 if x < 396 else 2)
            base = (74, 240, 406)[coluna]
            itens.append({
                "nivel": 1 if linha["spans"][0]["font"].endswith("Medium") else (2 if x - base < 4 else 3),
                "titulo": casa.group(1).strip(), "pagina": int(casa.group(2)),
                "coluna": coluna, "y": round(linha["bbox"][1]),
            })
    itens.sort(key=lambda i: (i["coluna"], i["y"]))
    return itens


def slug(texto):
    base = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", base.lower())).strip("-")


def main():
    doc = pymupdf.open(PDF)
    modo = sys.argv[1] if len(sys.argv) > 1 else "sumario"
    if modo == "sumario":
        for item in ler_sumario(doc):
            print(f"{'  ' * (item['nivel'] - 1)}{item['titulo']}\t{item['pagina']}")
    elif modo == "texto":
        for impressa, linhas in paginas_marcadas(doc, int(sys.argv[2]), int(sys.argv[3])):
            print(f"\n@@@ p.{impressa}")
            for linha in linhas:
                print(f"[{linha['papel']:6s}] {linha['texto']}")


if __name__ == "__main__":
    main()
