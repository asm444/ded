---
name: planejar-campanha
description: Define a camada macro de uma campanha — premissa, tom, cenário, facções, arco de níveis e condição de fim. Acionar com /planejar-campanha, no roteamento do /mestrar, ou quando o usuário quiser começar uma campanha nova ou disser que não sabe do que a mesa vai tratar.
---

# Planejar campanha

Produz `mesa/campanha.md`: o documento que decide o que entra e o que não entra em todas as
sessões seguintes. Uma página, não um livro — campanha detalhada demais morre no contato com
as escolhas do grupo.

## O que precisa ficar decidido

1. **Premissa em uma frase.** O que o grupo enfrenta e por quê. Se não couber numa frase,
   ainda não está decidido.
2. **Tom.** Heroico, sombrio, intriga política, exploração, humor. O tom decide o que é
   apropriado em mesa mais do que qualquer regra.
3. **Cenário.** Um dos quatro do livro (Forgotten Realms, Greyhawk, Dragonlance, Eberron), um
   mundo próprio, um plano (Faéria e Sombral estão em `docs/apendices/multiverso.md`), ou um
   mundo de fora já traduzido em `references/<slug>/`. O projeto não tem ambientação detalhada:
   fixe só o necessário e diga que o resto é seu. Se o usuário citar um mundo de fora que ainda
   não tem pasta em `references/`, pare aqui e chame `mundo`. Usando uma referência, grave no
   arquivo a linha `Mundo: references/<slug>/`, que é como as outras skills sabem que ela existe.
4. **Faixa de níveis e duração.** Do nível 1 ao 5 em dez sessões é uma campanha; do 1 ao 20 é
   outra coisa. Isso decide o ritmo de tudo.
5. **Três facções ou forças** com o que cada uma quer. Elas geram conflito sem que você precise
   escrever enredo — é o motor mais barato de aventura que existe.
6. **Condição de fim.** O que precisa acontecer para a campanha terminar. Sem isso a campanha
   não acaba, se arrasta.

## Sessão zero

`docs/personagem/criacao.md` traz a Sessão Zero. Trate-a como parte do planejamento, não como
formalidade: alinhe expectativas, limites de conteúdo, se o grupo quer combate ou intriga, e
como os personagens se conhecem. Decisão tomada aqui evita atrito na sessão 6.

Ofereça-se para criar os personagens do grupo com `criar-personagem` e `gerar-historia`,
amarrando os vínculos entre eles enquanto a campanha ainda é maleável.

## O que NÃO decidir agora

Não escreva o clímax, não detalhe cidades que o grupo talvez nunca visite, não crie PNJ que
ainda não tem função. Deixe buracos de propósito: o grupo vai preenchê-los com escolhas que
você não previu, e isso é o jogo funcionando.

## Saída

Grave `mesa/campanha.md` com as seis decisões, a sessão zero e uma lista de ganchos abertos.
Termine perguntando se o usuário quer seguir para `planejar-aventura` do primeiro arco.
