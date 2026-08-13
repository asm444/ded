---
name: consultar-regra
description: Responde qualquer dúvida de regra de D&D 2024 a partir do docs/ do projeto, sempre com a citação de onde a regra está. Acionar com /consultar-regra, ou sempre que aparecer uma pergunta de regra em mesa ("agarrar provoca ataque de oportunidade?", "como funciona Fúria?", "quanto cura um descanso curto?").
---

# Consultar regra

A resposta sai do `docs/`, com citação. Responder de memória é o erro que essa skill existe
para evitar: a edição 2024 reescreveu condições, ações e criação de personagem, e o texto
lembrado é quase sempre o de 2014.

## Onde procurar, nesta ordem

1. `docs/regras/glossario.md` — é o índice canônico. Condições, ações, áreas de efeito,
   descanso, cobertura, imobilizar e a maioria dos termos estão definidos ali, em uma entrada
   por termo.
2. `docs/regras/<assunto>.md` — combate, dano e cura, exploração, quando a pergunta é do
   procedimento e não do termo.
3. O domínio específico — `docs/classes/`, `docs/magias/`, `docs/equipamento/`.

    grep -rn "Imobilizado" docs/regras/glossario.md

## Formato da resposta

Primeiro a resposta direta, em uma ou duas frases. Depois a citação: arquivo e página do
livro (o cabeçalho de cada `.md` declara o intervalo). Depois, só se mudar a decisão em mesa,
a exceção ou o caso de borda.

Quando a regra depende de arbitragem do Mestre, diga isso explicitamente em vez de inventar
um número: o livro delega vários casos ("a critério do Mestre").

## Quando não achar

Diga que não achou e onde procurou. Não preencha a lacuna com a regra de 2014 nem com o que
"costuma ser". Se o assunto for ambientação, ficção ou sabor, avise que o `docs/` cobre
mecânica e que a fonte é o PDF.
