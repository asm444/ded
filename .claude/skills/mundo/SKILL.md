---
name: mundo
description: Pesquisa a identidade de um mundo de fora do D&D (série, jogo, filme, livro) e o traduz em referência jogável, com cada elemento achado em docs/ e citado. Acionar com /mundo, quando o usuário disser que quer jogar num mundo que ele gosta, ou quando o roteamento do /mestrar encontrar uma referência de fora sem pasta em references/.
---

# Mundo

Produz `references/<slug>/mundo.md` e `references/<slug>/traducao.md`: a identidade de um mundo
que o usuário gosta, e o mapa de como ele vira mesa de D&D 2024 sem uma regra inventada.

Vale a escala inteira do que `AGENTS.md` já manda para um personagem: a referência entra como
**comportamento**, a mecânica sai de `docs/` **citada**, e o que a regra não faz é dito na cara.
O que muda é o tamanho — em vez de um herói, um mundo.

## Regra zero: não presumir nada

Você não conhece o mundo do usuário melhor que ele. Nada entra no arquivo porque "parece" ou
porque "todo mundo sabe".

Cada afirmação em `mundo.md` sai marcada, e as quatro marcas não se misturam:

| Marca | Significa | Onde vale |
|---|---|---|
| `[fonte: <URL>]` | a fonte diz isso | os dois arquivos |
| `[fonte: você]` | resposta literal do usuário, registrada em `entrevista.md` | só `mundo.md` |
| `[derivado: entrevista]` | conclusão sua a partir das respostas dele | só `mundo.md` |
| `[não verificado]` | ninguém confirmou | só `mundo.md` |

**`[fonte: você]` sem a frase do usuário em `entrevista.md` é falsificação de evidência**, e é
pior que presumir: transforma o palpite em prova. O validador reprova por R9, e o que você
concluiu sozinho vai como `[derivado: entrevista]`, que é honesto e continua rastreável.

Não sabe? Pergunte. Perguntar custa uma linha; presumir custa uma campanha inteira montada no
mundo errado.

## Fase 1 — Entrevista

O usuário é fonte primária, e quase sempre a melhor: ele escolheu esse mundo por alguma razão
que nenhuma wiki registra. Pergunte **em lote**, nunca uma de cada vez (se o seu agente tiver
seleção de opções, use; se não, numere as perguntas e espere a resposta).

Lote 1, sempre:

1. Que mundo é, e em qual obra dele você pensa (qual jogo, qual temporada, qual filme)?
2. Se você fecha os olhos, quais **três** cenas desse mundo aparecem?
3. O que nesse mundo você **não** quer na mesa?
4. Você quer jogar *nesse* mundo, ou num mundo com o **clima** dele?

A pergunta 4 decide o resto: mundo fiel amarra o grupo à linha do tempo da obra; mundo com o
clima dele fica livre e costuma jogar melhor.

Lote 2, depois da pesquisa, só com o que ficou em aberto — no máximo quatro perguntas por lote,
sempre com o que você já descobriu ao lado, para o usuário corrigir em vez de redigitar.

**Grave `references/<slug>/entrevista.md` com a pergunta e a resposta de cada lote, na hora.**
É o arquivo que sustenta toda marca `[fonte: você]`, e sem ele o resto da referência não passa
na validação.

## Fase 2 — Pesquisa

Com busca disponível: três fontes independentes no mínimo, e URL por afirmação. Prefira a obra
e a wiki dedicada; desconfie de resumo de segunda mão, que apaga justamente o detalhe que dá
identidade.

Sem busca disponível: diga isso ao usuário na cara, trabalhe com o que ele traz, e marque tudo
o que não deu para conferir como `[não verificado]`. Um mundo feito só com a memória do usuário
é legítimo; um mundo feito com a sua memória fingindo pesquisa, não.

## Fase 3 — A grade

Quatorze critérios. Cada um fica preenchido com fonte, ou `NÃO SE APLICA — <motivo>`. Nenhum
fica em branco.

| # | Critério | Por que ele decide mesa |
|---|---|---|
| 1 | Premissa em uma frase | Se não cabe numa frase, o mundo ainda não foi entendido |
| 2 | Evento fundador | Quase todo mundo tem um antes e um depois; é dele que sai o tom |
| 3 | Linha do tempo em três marcos | Antes, a ruptura e o agora. É o que dá passado para o grupo mexer, em vez de cenário parado |
| 4 | Tom e limites de conteúdo | Decide o que é apropriado mais do que qualquer regra |
| 5 | A lei do mundo | O que ali ocupa o lugar da magia: radiação, tecnologia, dobra, fé, engenhoca de porão. Sem isso a magia de `docs/` entra sem fachada e o mundo some |
| 6 | Escala e geografia | Decide viagem (`docs/regras/exploracao.md`) e o tamanho do arco |
| 7 | Povos e o que os separa | Vira o mapa povo→espécie |
| 8 | Economia e recurso escasso | O que substitui a moeda de ouro |
| 9 | Perigos do ambiente | Viram riscos de `docs/regras/exploracao.md` |
| 10 | Estética: cinco imagens, sons ou cheiros | O que você fala em mesa para o jogador saber onde está |
| 11 | O que **não** existe ali | Tão identitário quanto o que existe: sem cura mágica? sem mortos-vivos? |
| 12 | Faixa de níveis que o mundo aguenta | Mundo de sucata não sustenta nível 20 |
| 13 | Facções, três no mínimo, com o que cada uma quer | Motor de aventura mais barato que existe |
| 14 | Seis ganchos tirados das facções | É o que `planejar-aventura` consome direto |

## Fase 4 — O teste da troca de nome

Antes de traduzir, troque **todos os nomes próprios** do `mundo.md` por outros e leia de novo.
Se a mesa não notaria diferença, você capturou estética e não identidade: volte à fase 2 e
puxe os critérios 2, 5, 11 e 13, que é onde a identidade mora.

Mundo capturado sobrevive à troca de nome. Mundo copiado, não.

## Fase 5 — A tradução

Sete tabelas em `traducao.md`, cada linha citando o arquivo de `docs/`:

| Eixo | O que entra | Onde achar |
|---|---|---|
| Povo | os povos do critério 7 | `docs/especies/especies.md` |
| Arquétipo | o papel reconhecível dali | `docs/classes/` |
| Subclasse | a variação do papel, que é onde o mundo aparece na ficha | `docs/classes/<classe>.md` |
| Habilidade | o que alguém dali sabe fazer, em perícia e talento | `docs/regras/acoes.md`, `docs/talentos/talentos.md` |
| Vida pregressa | de onde a pessoa daquele mundo vem | `docs/especies/antecedentes.md` |
| Item icônico | o objeto que diz o nome do mundo | `docs/equipamento/equipamento.md` |
| Efeito icônico | o poder que se vê na tela | `docs/magias/descricoes.md` |

A tabela de habilidade é a que mais rende: o talento costuma resolver o que parecia não ter
equivalente. Um exemplo verificado é o Artifista, cuja Fabricação Rápida monta um item que dura
até o próximo Descanso Longo, e por isso serve para qualquer mundo de engenhoca de uso único.

**A invariante: reskin muda nome e descrição, nunca número.** Uma pistola de energia é a besta
leve de `docs/equipamento/equipamento.md` com outro nome e outra descrição. Trocar o tipo de
dano é adaptação do Mestre, e vai escrita como adaptação. Criar um dado novo, uma CD nova ou
uma característica nova é o que essa skill existe para impedir.

Criaturas seguem o limite honesto do projeto: `docs/apendices/criaturas.md` tem o apêndice B do
Livro do Jogador, não um bestiário. O que faltar, peça ao Mestre ou marque como adaptação.

Tudo que não tem equivalente vai para `## Sem equivalente`, com o mais próximo e a diferença
exata. Essa seção é entrega, não fracasso: é o que impede a mesa de descobrir o buraco em jogo.

## Fase 6 — Fechar as lacunas

    valida ──► reprovou? ──► pesquisa focada SÓ na lacuna
      ▲                            │
      └──── pergunta ao usuário ◄──┘   (se a fonte não resolver)

Rode `tools/valida-referencia.sh references/<slug>`. Para cada falha, não reescreva o arquivo
inteiro: ataque **só aquela linha**, com busca dirigida ao critério que faltou, e se a fonte não
resolver, pergunte ao usuário. Repita até sair `OK`.

Duas saídas fecham uma lacuna, e só duas: o dado com fonte, ou `NÃO SE APLICA — <motivo>`.
Deixar em branco, escrever "a definir" ou preencher de memória não fecha, e o validador reprova.

## Fase 7 — Oferecer o PR

Com `OK` na mão, ofereça ao usuário mandar o mundo para este repositório:

> Sua referência passou na validação. Quer abrir um PR para que outras mesas usem?
> `references/README.md` tem os cinco critérios de aceite.

Ofereça, nunca faça sozinho: publicar é decisão do usuário.

## Modo lacuna

Chamado por `planejar-sessao` ou `mesa` quando a sessão precisa de um elemento que o mundo ainda
não traduziu. Não refaça o mundo: rode só as fases 2, 5 e 6 para **aquele item**, acrescente a
linha em `traducao.md` e siga. A referência cresce por uso, e não tenta nascer completa.

## Saída

`references/<slug>/mundo.md` e `references/<slug>/traducao.md`, com `OK` do validador colado na
conversa. Depois, ofereça seguir para `planejar-campanha`, que decide a premissa da **sua** mesa
dentro do mundo que você acabou de fixar.
