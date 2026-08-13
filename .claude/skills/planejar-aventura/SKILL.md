---
name: planejar-aventura
description: Estrutura um arco de 3 a 6 sessões (problema, atores, cenas, obstáculos e recompensas) sem roteirizar o que o grupo vai fazer. Acionar com /planejar-aventura, no roteamento do /mestrar, ou quando o arco atual terminar e o usuário precisar do próximo.
---

# Planejar aventura

Produz `mesa/aventuras/<slug>.md`. Uma aventura é um **problema com atores**, não um roteiro:
se o documento descreve o que os personagens vão fazer, ele será desmentido na primeira sessão.

## Estrutura

1. **O problema.** O que está errado no mundo, quem causou e o que acontece se ninguém agir.
   Esse "se ninguém agir" é o relógio da aventura — sem ele, nada pressiona o grupo.
2. **Gancho.** Por que ESTE grupo se envolve. Puxe dos vínculos e ganchos que
   `gerar-historia` deixou nas fichas; aventura que engata no passado de um personagem vale
   por três.
3. **Atores.** Três a cinco, com o que cada um quer e o que faz se for contrariado. Use
   `criar-pnj` para os que vão falar mais de uma vez.
4. **Lugares.** Dois a quatro, com o que há neles de interessante. Use `criar-local` para os
   que o grupo vai explorar.
5. **Obstáculos, não caminhos.** Liste o que dificulta — guardas, um rio, um segredo, um
   prazo. Não liste a solução: o grupo inventa a dele.
6. **Recompensas.** Tesouro, informação, aliado, título. Diga também o que muda no mundo se
   eles vencerem, e o que muda se falharem — aventura sem consequência de falha não tem tensão.

## Ritmo e níveis

Uma aventura costuma render um nível ou dois. Confira em `docs/personagem/avanco-de-nivel.md`
onde o grupo estará no fim e o que isso destrava — se todos ganham a subclasse no nível 3
durante este arco, o clímax pode contar com isso.

## Os três pilares

Cheque explicitamente se a aventura oferece os três (`docs/regras/`): **combate**, **exploração**
e **interação social**. Arco só de combate cansa e desperdiça metade das fichas — o Bardo com
Persuasão treinada não tem o que fazer numa masmorra sem ninguém para convencer.

## Encontros

Marque onde combate é provável e chame `montar-encontro` para cada um. Lembre o limite: o
projeto tem os animais do apêndice B, não um bestiário — para monstros, o Mestre traz o bloco
de estatísticas.

## Saída

Grave o arquivo e liste as pontas que ficaram abertas de propósito. Pergunte se o usuário quer
seguir para `planejar-sessao` da primeira sessão do arco.
