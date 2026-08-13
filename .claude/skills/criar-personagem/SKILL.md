---
name: criar-personagem
description: Cria um personagem de D&D 2024 completo, do conceito à ficha validada, seguindo os 5 passos oficiais do livro. Acionar com /criar-personagem, ou quando o usuário pedir um personagem novo, quiser "rolar um PC", ou trouxer um conceito ("quero um anão clérigo de guerra") para virar ficha.
---

# Criar personagem

Conduz os 5 passos do capítulo 2 e entrega uma ficha em `fichas/<nome>.json` que passa em
`tools/validar_ficha.py`. Cada escolha oferecida vem de `docs/`, com o arquivo citado — nunca
de memória, porque a versão 2024 mudou classe, origem e talento em relação à de 2014.

## Antes de começar

Pergunte só o que muda o trabalho, e em UM lote: nível inicial, se o grupo já existe (para
equilibrar papéis) e se há conceito de partida. Sem resposta, assuma nível 1, grupo novo e
conceito livre, e diga o que assumiu.

## Os 5 passos

Um passo por vez. Ao fim de cada um, mostre o que ficou decidido e o que ainda falta.

### Passo 1 — Classe (`docs/classes/`)

Apresente as classes que servem ao conceito, com o que cada uma entrega no nível pedido: dado
de vida, atributo primário, proficiências, e a característica que define o jogo dela. Se o
personagem começa acima do nível 3, a subclasse entra aqui, não depois.

Anote: classe, nível, dado de vida, bônus de proficiência, treinamento com armadura.

### Passo 2 — Origem (`docs/especies/`)

Antecedente primeiro, porque é ele que carrega os aumentos de atributo e o talento de origem.
Depois espécie, depois idiomas. O antecedente concede +3 distribuídos: ou +2/+1 em dois
atributos, ou +1/+1/+1 em três — a escolha é do jogador, dentro dos três atributos que o
antecedente lista.

Anote: antecedente, talento de origem, proficiências, equipamento inicial, espécie, traços,
idiomas.

### Passo 3 — Valores de atributo (`docs/personagem/criacao.md`)

Ofereça os três métodos e recomende um: compra por pontos (27 pontos, controlado), conjunto
padrão (15, 14, 13, 12, 10, 8) ou rolagem (4d6 descartando o menor, aleatório). Aplique só
depois os aumentos do antecedente — a ordem importa, porque o teto de 15 vale antes deles.

Anote: os seis valores finais, modificadores, PV máximo, CA, iniciativa, CD de magia.

### Passo 4 — Alinhamento

Uma linha. Não trave a criação aqui.

### Passo 5 — Detalhes, via `gerar-historia`

Não preencha nome, vínculo e motivação a seco: invoque a skill `gerar-historia` com as
escolhas dos passos 1 a 4. Ela ancora o passado no multiverso e devolve, junto da narrativa,
as derivações que fecham a ficha — perícias e ferramentas ainda abertas, talento sugerido,
magias temáticas, equipamento com significado, vínculo e ideal, e ganchos para o Mestre.

Chega tarde de propósito: classe e origem já estão fixadas, então a história tem o que
explicar, e o que resta em aberto ela ajuda a decidir em vez de decorar.

Traga as sugestões ao jogador como sugestões, aplique as aceitas e feche a ficha.

## Saída

Grave `fichas/<slug>.json` com: identidade, classe e nível, origem, atributos, PV, CA,
proficiências, equipamento, magias (se houver) e a lista de características por nível com a
página de origem. Rode a validação e cole a saída:

    python3 tools/validar_ficha.py fichas/<slug>.json

Ficha que não passa não é entregue como pronta: mostre o que falhou e corrija.

## O que não fazer

- Não invente característica, talento ou magia que você não localizou em `docs/`.
- Não decida por atributo, classe ou conceito do jogador; ofereça e deixe escolher.
- Não pule a validação porque "está óbvio" — pré-requisito de talento e espaço de magia por
  multiclasse erram em silêncio.
