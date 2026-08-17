---
name: montar-encontro
description: Monta um encontro de combate ou desafio jogável — oposição, terreno, objetivo, condição de fim e o que acontece se o grupo fugir ou negociar. Acionar com /montar-encontro, a partir do planejamento de aventura ou sessão, ou quando o usuário pedir um encontro para um grupo de nível X.
---

# Montar encontro

Um encontro é oposição **mais** situação. Oposição sozinha é uma lista de monstros num quarto
vazio, e é o que torna combate monótono.

## Entradas

Número e nível dos personagens, o que o encontro faz na aventura (obstáculo, revelação,
clímax) e o tom desejado (rotina, desafio, ameaça séria).

## Os cinco elementos

1. **Oposição.** Quem se opõe e quantos. O Nível de Desafio compara a ameaça com um grupo de
   quatro personagens (`docs/regras/glossario.md`), mas o número de inimigos e o terreno mudam
   mais o resultado do que o ND isolado. Dois inimigos de ND baixo com posição boa dão mais
   trabalho que um de ND alto no meio da sala.
2. **Terreno com efeito mecânico.** Cobertura, terreno difícil, luz, altura, água — cada um
   está definido em `docs/regras/` e muda decisões. Terreno sem efeito é cenário, não terreno.
3. **Objetivo além de "matar".** Proteger alguém, alcançar algo antes do inimigo, aguentar até
   a porta abrir, capturar em vez de matar. Muda completamente como o grupo joga.
4. **Condição de fim.** Quando acaba, e o que os inimigos fazem quando estão perdendo. Inimigo
   que sempre luta até morrer é inimigo que não pensa — e joga fora as chances de recuo,
   rendição e negociação.
5. **As três saídas.** O que acontece se o grupo lutar, se fugir e se negociar. Encontro com
   uma saída só é um corredor.

## Estatísticas

O projeto tem os animais e montarias do apêndice B (`docs/apendices/criaturas.md`) — úteis
para feras, montarias e invocações. **Não tem bestiário**: para monstros, peça o bloco de
estatísticas ao Mestre ou use o Livro dos Monstros. Nunca invente estatística de monstro e
apresente como oficial; se improvisar um bloco, diga que é improvisado.

Num mundo de fora (`mesa/campanha.md` com a linha `Mundo:`), a oposição sai das facções de
`references/<slug>/mundo.md`, e o que ela usa sai de `traducao.md`, que já aponta a regra de
cada arma e efeito daquele mundo. Encontro que ignora as facções vira monstro genérico com
outro nome.

## Saída

Entregue em formato de mesa: lista de criaturas com PV e CA, iniciativa, o mapa em três linhas,
o objetivo, a condição de fim e as reações previstas. Some as regras que a cena vai puxar, com
o link para `docs/regras/`.
