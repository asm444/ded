---
name: criar-pnj
description: Cria um PNJ jogável em mesa — o que quer, como fala, o que sabe e só as estatísticas que a cena exige. Acionar com /criar-pnj, a partir do planejamento, ou quando o usuário pedir um personagem do mundo (taverneiro, vilão, patrono, contato).
---

# Criar PNJ

Um PNJ existe para ser interpretado em mesa, não para ser lido. O que decide se ele funciona é
o que ele **quer**, porque desejo produz comportamento em qualquer situação — inclusive nas que
você não previu.

## O mínimo

1. **Nome** pronunciável, e uma imagem em uma linha.
2. **O que quer**, e o que está disposto a fazer para conseguir.
3. **Como fala** — um traço só, reproduzível: fala devagar, responde com pergunta, usa termos
   náuticos, nunca diz o nome de ninguém. Um traço executável vale mais que um parágrafo de
   personalidade.
4. **O que sabe** que o grupo pode querer, e sob qual condição conta.
5. **Atitude inicial** — Amigável, Indiferente ou Hostil (`docs/regras/glossario.md`). É ela
   que define se o grupo tem Vantagem ou Desvantagem ao tentar Influenciar.

## Estatísticas: só se a cena pedir

Taverneiro que serve cerveja não precisa de bloco. Capitão que vai lutar precisa. Quando
precisar, use o limite honesto: o projeto não tem bestiário nem blocos de humanoides — use um
animal do apêndice B quando couber, peça o bloco ao Mestre, ou improvise e **declare que
improvisou**.

Para PNJ que luta e é importante, o mínimo jogável é: CA, PV, um ataque com bônus e dano, e
uma coisa que ele faz que ninguém mais faz.

## Vilões

Além do acima: por que ele acha que está certo, o que o faria parar, e o que acontece com o
mundo se ele vencer. Vilão sem razão própria vira alvo, e alvo não sustenta uma campanha.

## Ligações

Ligue o PNJ a algo que já existe: uma facção da campanha, um gancho de `gerar-historia` de
algum personagem, um lugar de `criar-local`. PNJ solto é PNJ esquecido.

## Saída

PNJ recorrente vai para `mesa/pnjs/<slug>.md`. PNJ descartável fica na sessão. Se ele
sobreviver e o grupo se importar, promova-o ao arquivo próprio.
