---
name: mesa
description: Apoio ao Mestre durante a sessão — montar encontro, gerar PNJ, arbitrar situação, controlar iniciativa e condições. Acionar com /mesa, ou quando o usuário estiver conduzindo o jogo ("preciso de um encontro para 4 personagens de nível 5", "cria um taverneiro", "quem age primeiro?", "o orc tenta agarrar").
---

# Mesa

CLASSE: procedimento
IMPORTA: consultar-regra, montar-encontro, criar-pnj

Ferramenta de Mestre em sessão. Prioriza resposta rápida e jogável: a mesa está esperando.

## O que entrega
Uma decisão aplicável na hora (teste, CD, efeito) com a citação em `docs/`, ou a marca
explícita de que foi arbitrada sem confirmar. Verificação: toda resposta traz a citação ou a
marca, nunca nenhuma das duas.

## Arbitrar uma situação

Resolva na ordem: qual teste, qual CD, o que acontece em sucesso e em falha.

- Teste de atributo, salvaguarda ou jogada de ataque — os três são Teste de D20
  (`docs/regras/fundamentos.md`).
- CD padrão: 10 fácil, 15 médio, 20 difícil. Influenciar monstro usa CD 15 ou a Inteligência
  do monstro, o que for maior (`docs/regras/glossario.md`).
- Condição imposta: leia o efeito exato no glossário antes de aplicar. Várias condições da
  edição 2024 mudaram, e Exaustão agora é acumulativa em níveis, com −2 por nível em todo
  Teste de D20.

Responda com a regra e a citação, depois siga o jogo. Caso de borda que o livro delega ao
Mestre: diga que é decisão dele e ofereça uma opção padrão.

## Precisa de encontro ou de PNJ

SE o pedido for um encontro → chamar `montar-encontro`.
SE for um PNJ → chamar `criar-pnj`.
SE a mesa estiver esperando e não houver tempo → resolva com o que sabe e diga que resolveu
assim, sem abrir a skill.

## Controlar combate

Mantenha a ordem de iniciativa e, por criatura, PV atual, condições ativas e concentração.
Ao aplicar dano em quem concentra, cobre a salvaguarda de Constituição: CD 10 ou metade do
dano, o que for maior.

## Regra de ouro

Se a consulta demorar mais que a cena aguenta, decida com o que sabe, diga que decidiu assim
e confira depois. Marque explicitamente quando arbitrou sem confirmar no `docs/`.
