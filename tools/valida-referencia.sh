#!/usr/bin/env bash
# Valida uma referencia de mundo em references/<slug>/.
# Uso: tools/valida-referencia.sh references/<slug>
# Saida: uma linha por falha, no formato arquivo:linha: <codigo> <mensagem>.
# Exit 0 = pronto para PR.
set -uo pipefail

SECOES=(
  "## Premissa"
  "## Evento fundador"
  "## Tom e limites"
  "## A lei do mundo"
  "## Escala e geografia"
  "## Facções"
  "## Povos"
  "## Economia e escassez"
  "## Perigos do ambiente"
  "## Estética"
  "## O que não existe"
  "## Faixa de níveis"
  "## Ganchos"
  "## Origem e fontes"
)
MECANICA='[0-9]+d[0-9]+|\bCD ?[0-9]+|\bCA ?[0-9]+|\b[0-9]+ PV\b'

falhas=0
erro() { printf '%s: %s\n' "$1" "$2"; falhas=$((falhas + 1)); }

dir="${1:-}"
[ -n "$dir" ] || { echo "uso: $0 references/<slug>" >&2; exit 2; }

mundo="$dir/mundo.md"
trad="$dir/traducao.md"

# R1 - os dois arquivos existem
for f in "$mundo" "$trad"; do
  [ -f "$f" ] || erro "$f:0" "R1 arquivo ausente"
done
[ "$falhas" -eq 0 ] || { echo "$falhas falha(s)"; exit 1; }

# R2 - as 14 secoes existem e nenhuma esta vazia
for s in "${SECOES[@]}"; do
  ini=$(grep -n -x -F "$s" "$mundo" | head -1 | cut -d: -f1)
  if [ -z "$ini" ]; then
    erro "$mundo:0" "R2 seção ausente: $s"
    continue
  fi
  corpo=$(awk -v i="$ini" 'NR>i { if ($0 ~ /^## /) exit; if ($0 ~ /[^[:space:]]/) { print; exit } }' "$mundo")
  [ -n "$corpo" ] || erro "$mundo:$ini" "R2 seção vazia: $s"
done

# R3 - toda linha de corpo de tabela em traducao.md cita docs/
while IFS=: read -r n resto; do
  [ -n "$n" ] || continue
  case "$resto" in *docs/*) continue ;; esac
  # linha separadora (|---|---|) e cabecalho de tabela nao carregam tradução
  [[ "$resto" =~ ^[\|[:space:]:-]+$ ]] && continue
  case "$resto" in
    "| No mundo"*|"| Efeito"*|"| Item"*|"| Arquétipo"*|"| Papel"*|"| Origem"*) continue ;;
  esac
  erro "$trad:$n" "R3 linha de tradução sem citação de docs/: ${resto:0:60}"
done < <(grep -n '^|' "$trad")

# R4 - numero mecanico exige citacao de docs/ na mesma linha
for f in "$mundo" "$trad"; do
  while IFS=: read -r n resto; do
    [ -n "$n" ] || continue
    case "$resto" in *docs/*) continue ;; esac
    erro "$f:$n" "R4 número mecânico sem fonte: ${resto:0:60}"
  done < <(grep -n -E "$MECANICA" "$f")
done

# R5 - o nome da franquia fica confinado a '## Origem e fontes'
origem=$(grep -m1 -E '^origem:' "$mundo" | sed 's/^origem:[[:space:]]*//')
if [ -z "$origem" ]; then
  erro "$mundo:0" "R5 cabeçalho sem campo origem:"
else
  # compara sem espaco, ponto e hifen, para 'Ben 10', 'Ben10' e 'ben-10' caírem juntos;
  # URL sai da linha antes da comparação, senão a fonte citada acusaria a si mesma
  normal() { printf '%s' "$1" | sed -E 's#https?://[^ )]*##g' | awk '{print tolower($0)}' | tr -d ' ._-'; }
  alvo=$(normal "$origem")
  ini=$(grep -n -x -F "## Origem e fontes" "$mundo" | head -1 | cut -d: -f1)
  ini=${ini:-999999}
  n=0
  while IFS= read -r linha; do
    n=$((n + 1))
    [ "$n" -ge "$ini" ] && break
    case "$linha" in origem:*|mundo:*|slug:*) continue ;; esac
    case "$(normal "$linha")" in *"$alvo"*)
      erro "$mundo:$n" "R5 nome de origem fora de '## Origem e fontes': ${linha:0:60}" ;;
    esac
  done < "$mundo"
  n=0
  while IFS= read -r linha; do
    n=$((n + 1))
    case "$linha" in origem:*|mundo:*|slug:*) continue ;; esac
    case "$(normal "$linha")" in *"$alvo"*)
      erro "$trad:$n" "R5 nome de origem em traducao.md: ${linha:0:60}" ;;
    esac
  done < "$trad"
fi

# R6 - profundidade minima: 3 faccoes, 6 ganchos, 5 imagens de estetica, 3 fontes
conta() { awk -v s="$1" 'index($0,s)==1 && length($0)==length(s) {f=1; next} f && /^## / {exit} f && /^[-*|] / {n++} END {print n+0}' "$2"; }
[ "$(conta '## Facções' "$mundo")" -ge 3 ] || erro "$mundo:0" "R6 menos de 3 facções"
[ "$(conta '## Ganchos' "$mundo")" -ge 6 ] || erro "$mundo:0" "R6 menos de 6 ganchos"
[ "$(conta '## Estética' "$mundo")" -ge 5 ] || erro "$mundo:0" "R6 menos de 5 imagens em Estética"
[ "$(grep -c 'http' "$mundo")" -ge 3 ] || erro "$mundo:0" "R6 menos de 3 fontes com URL"

# R7 - lacuna aberta reprova; NAO SE APLICA so passa com motivo na mesma linha
for f in "$mundo" "$trad"; do
  while IFS=: read -r n resto; do
    [ -n "$n" ] || continue
    erro "$f:$n" "R7 lacuna aberta: ${resto:0:60}"
  done < <(grep -n -E '\b(LACUNA|TODO|A DEFINIR|\?\?\?)\b' "$f")
  while IFS=: read -r n resto; do
    [ -n "$n" ] || continue
    case "$resto" in *"NÃO SE APLICA —"*) continue ;; esac
    erro "$f:$n" "R7 'NÃO SE APLICA' sem motivo após —: ${resto:0:60}"
  done < <(grep -n -F 'NÃO SE APLICA' "$f")
done

# R8 - afirmacao de mecanica nunca fica sem verificacao
while IFS=: read -r n resto; do
  [ -n "$n" ] || continue
  erro "$trad:$n" "R8 mecânica marcada como não verificada: ${resto:0:60}"
done < <(grep -n -F '[não verificado]' "$trad")

if [ "$falhas" -eq 0 ]; then
  echo "OK $dir"
  exit 0
fi
echo "$falhas falha(s)"
exit 1
