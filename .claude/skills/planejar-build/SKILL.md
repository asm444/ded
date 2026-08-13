---
name: planejar-build
description: Planeja a progressão de um personagem do nível atual até o 20, ou compara caminhos alternativos para o mesmo conceito. Acionar com /planejar-build, ou quando o usuário perguntar "vale a pena multiclassar?", "qual talento pegar no 4?", "como fica essa build no 11?", "qual das duas dá mais dano?".
---

# Planejar build

Traça o caminho nível a nível e mostra o que cada escolha custa e entrega. O que é calculável
vira número; o que é preferência fica declarado como preferência, não disfarçado de fato.

## Entradas

Personagem (ficha em `fichas/` ou conceito), nível atual, nível-alvo e o objetivo: dano
sustentado, dano de pico, controle, resistência, suporte ou versatilidade. Sem objetivo
declarado, pergunte — é ele que decide toda a comparação, e assumir errado invalida o plano
inteiro.

## Como montar

1. Leia a progressão em `docs/classes/<classe>.md`. A tabela de características dá, por
   nível, o que entra automaticamente e onde há escolha.
2. Marque os **pontos de decisão**: subclasse (nível 3), aumento de valor de atributo ou
   talento (4, 8, 12, 16, e mais em algumas classes), dádiva épica (19). Só esses precisam de
   análise; o resto é automático.
3. Em cada ponto de decisão, apresente as opções reais — do `docs/talentos/` e do
   `docs/classes/` — com o efeito concreto no objetivo declarado.
4. Multiclasse (`docs/personagem/multiclasse.md`) tem pré-requisito de atributo e muda espaço
   de magia e bônus de proficiência. Se entrar na conversa, mostre o que se perde: atraso da
   característica de nível alto da classe principal.

## Comparação entre caminhos

Compare com número onde dá: bônus de ataque, dano médio por rodada, CA, PV, CD de magia.
Diga a premissa junto do número (alvo com CA 15, sem vantagem, dois ataques por turno) — dano
médio sem premissa declarada não é comparável.

Onde não dá número (diversão, encaixe na mesa, complexidade de operação), diga que é
julgamento e recomende uma opção, sem fingir que a medida decidiu.

## Saída

Uma tabela nível a nível com o que entra e o que foi escolhido, seguida das decisões abertas
que o jogador precisa tomar.

## Armadilhas

- Pré-requisito de talento e de multiclasse é atributo mínimo: confira antes de sugerir.
- A edição 2024 mudou onde a subclasse entra (nível 3 para todas as classes). Não use a
  progressão de 2014 de memória.
- Aumento de atributo tem teto 20 sem magia ou item; talento que dá +1 esbarra nele.
