#!/usr/bin/env bash
# Prova que tools/valida-referencia.sh detecta cada regra, e que cada quebra cai NO caso dela.
# Uso: tools/test/valida-referencia.test.sh
set -uo pipefail

RAIZ="$(cd "$(dirname "$0")/../.." && pwd)"
VALIDA="$RAIZ/tools/valida-referencia.sh"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

falhou=0
ok()   { printf 'PASSA  %s\n' "$1"; }
nok()  { printf 'FALHA  %s\n     %s\n' "$1" "$2"; falhou=1; }

montar() {  # montar <dir> => referencia valida
  local d="$1"; mkdir -p "$d"
  cat > "$d/mundo.md" <<'EOF'
---
mundo: Ermo Radiante
origem: Franquia Exemplo
slug: exemplo
---

# Ermo Radiante

## Premissa
Sobreviventes de um abrigo saem ao deserto envenenado atrás de água limpa.

## Evento fundador
As bombas caíram duzentos anos atrás e o céu ficou amarelo.

## Tom e limites
Sombrio com humor seco. Sem violência contra crianças.

## A lei do mundo
O que ali ocupa o lugar da magia é a radiação, que muda corpo e mente.

## Escala e geografia
Um deserto de trinta dias de caminhada entre dois abrigos.

## Povos
Abrigados, ermitões e transformados pela radiação.

## Economia e escassez
A moeda é a tampinha; o recurso escasso é água limpa.

## Perigos do ambiente
Tempestade de radiação, sede, ruína instável.

## Estética
- Ferrugem em tudo
- Rádio tocando música velha
- Placas de propaganda antiga
- Cheiro de ozônio antes da tempestade
- Silêncio absoluto à noite

## O que não existe
Não existe cura instantânea, nem lei escrita, nem governo.

## Faixa de níveis
Do nível 1 ao 8: o mundo não sustenta heroísmo cósmico.

## Facções
- Os Abrigados querem manter a porta fechada
- A Caravana quer rota segura
- Os Filhos do Átomo querem que todos se transformem

## Ganchos
- Um abrigo parou de responder
- A caravana sumiu no desfiladeiro
- Alguém vende água limpa demais
- Um mapa antigo aponta uma usina
- O pregador quer um refém
- Uma criança nasceu sem marca da radiação

## Origem e fontes
Derivado de Franquia Exemplo.
- https://exemplo.org/a
- https://exemplo.org/b
- https://exemplo.org/c
EOF
  cat > "$d/traducao.md" <<'EOF'
---
mundo: Ermo Radiante
origem: Franquia Exemplo
slug: exemplo
---

# Tradução — Ermo Radiante

## Povos
| No mundo | Em D&D 2024 | O que muda | Fonte |
|---|---|---|---|
| Transformado | Humano | só descrição | docs/especies/especies.md |

## Arquétipos
| No mundo | Em D&D 2024 | O que muda | Fonte |
|---|---|---|---|
| Batedor do ermo | Guardião | só nome | docs/classes/guardiao.md |

## Sem equivalente
- Rifle automático: o mais próximo é a besta pesada (docs/equipamento/equipamento.md); a diferença é não haver rajada.
EOF
}

# Caso 0 - referencia valida passa
montar "$TMP/valido"
saida="$("$VALIDA" "$TMP/valido" 2>&1)"; cod0=$?
if [ "$cod0" -eq 0 ]; then ok "R0 referência válida passa"; else nok "R0 referência válida passa" "$saida"; fi

# aceita <nome> <comando de mutacao> => a mutacao NAO pode reprovar
aceita() {
  local nome="$1" mut="$2" d="$TMP/a$RANDOM$RANDOM"
  montar "$d"
  ( cd "$d" && eval "$mut" )
  local out cod
  out="$("$VALIDA" "$d" 2>&1)"; cod=$?
  if [ "$cod" -eq 0 ]; then ok "$nome"; else nok "$nome" "reprovou indevidamente: $out"; fi
}

# a URL da fonte contem o nome da franquia, e citar a fonte nao pode reprovar
aceita "R5 URL com o nome da franquia passa" \
  'awk "/^## Premissa\$/{print; getline; print \$0 \" [fonte: https://franquiaexemplo.org/lore]\"; next} {print}" mundo.md > t && mv t mundo.md'

# quebra <nome> <regra> <comando de mutacao>
quebra() {
  local nome="$1" regra="$2" mut="$3" d="$TMP/q$RANDOM$RANDOM"
  montar "$d"
  ( cd "$d" && eval "$mut" )
  local out cod
  out="$("$VALIDA" "$d" 2>&1)"; cod=$?
  if [ "$cod" -eq 0 ]; then
    nok "$nome" "passou apesar da quebra"
  elif printf '%s' "$out" | grep -q "$regra"; then
    local outros
    outros="$(printf '%s' "$out" | grep -oE '\bR[0-9]\b' | grep -v "^$regra$" | sort -u | tr '\n' ' ')"
    if [ -n "$outros" ]; then
      nok "$nome" "caiu em $regra mas também em: $outros (colateral)"
    else
      ok "$nome (cai em $regra)"
    fi
  else
    nok "$nome" "esperava $regra, veio: $out"
  fi
}

quebra "R1 arquivo faltando"            R1 'rm traducao.md'
quebra "R2 seção ausente"               R2 'grep -v "^## Evento fundador$" mundo.md > t && mv t mundo.md'
quebra "R2 seção vazia"                 R2 'awk "/^## Economia e escassez\$/{print; getline; print \"\"; next} {print}" mundo.md > t && mv t mundo.md'
quebra "R3 tradução sem fonte"          R3 'printf "| Ferramenta | Kit de ferramentas | nome |  |\n" >> traducao.md'
quebra "R4 dano inventado no mundo"     R4 'printf "\nA tempestade causa 4d6 de dano.\n" >> mundo.md'
quebra "R4 CD inventada na tradução"    R4 'printf "\n- Salvaguarda contra a radiação: CD 15.\n" >> traducao.md'
quebra "R5 franquia fora da seção"      R5 'awk "/^## Premissa\$/{print; getline; print \"Isto é Franquia Exemplo.\"; next} {print}" mundo.md > t && mv t mundo.md'
quebra "R5 franquia na tradução"        R5 'printf "\nComo em Franquia Exemplo.\n" >> traducao.md'
quebra "R5 franquia colada sem espaço"  R5 'printf "\nIgual em FranquiaExemplo.\n" >> traducao.md'
quebra "R5 franquia com hífen"          R5 'printf "\nIgual em franquia-exemplo.\n" >> traducao.md'
quebra "R6 facções de menos"            R6 'grep -v "^- A Caravana" mundo.md > t && mv t mundo.md'
quebra "R6 ganchos de menos"            R6 'grep -v "^- Um mapa antigo" mundo.md > t && mv t mundo.md'
quebra "R6 estética de menos"           R6 'grep -v "^- Ferrugem" mundo.md > t && mv t mundo.md'
quebra "R6 fontes de menos"             R6 'grep -v "exemplo.org/c" mundo.md > t && mv t mundo.md'
quebra "R7 lacuna aberta"               R7 'printf "\n- Moedas: A DEFINIR\n" >> traducao.md'
quebra "R7 não se aplica sem motivo"    R7 'printf "\n- Náutica: NÃO SE APLICA\n" >> mundo.md'
quebra "R8 mecânica não verificada"     R8 'printf "\n- A armadura de energia protege [não verificado].\n" >> traducao.md'

[ "$falhou" -eq 0 ] && { echo; echo "todos os casos passaram"; exit 0; }
echo; echo "há caso falhando"; exit 1
