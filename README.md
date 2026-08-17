<div align="center">

<img src="assets/ded.png" alt="DED" width="340">

# DED

**D**ados · **É**tica · **D**efesa · **I**ntegridade · **D**ecisão

*Ninguém precisa ler 397 páginas para sentar à mesa.*

[English](README.en.md) · [Base de regras](docs/README.md) · [Guia para agentes](AGENTS.md)

</div>

---

## O que é

Um agente de IA que senta na mesa com você. Do lado do jogador, ele cria personagem e ajuda a
transformar uma ideia solta em ficha jogável. Do lado do Mestre, ele planeja campanha, prepara
sessão e ajuda a conduzir o jogo.

As regras já estão aqui, prontas, e ele responde citando a página. Quando não acha a regra, diz
que não achou em vez de inventar.

Feito com modelos gratuitos, via [opencode](https://opencode.ai). Quem quer jogar D&D não
deveria precisar de assinatura de IA nem decorar 397 páginas para começar.

## Se você joga

| Você quer | Diga | O que acontece |
|---|---|---|
| Um personagem novo | `/criar-personagem` | Os 5 passos oficiais, do conceito à ficha fechada |
| Uma ideia virar personagem | `/gerar-historia` | O passado sai ancorado no multiverso e vira escolha de perícia, talento e magia |
| Planejar a evolução | `/planejar-build` | Nível a nível, com número onde dá para medir |
| Subir de nível | `/subir-nivel` | Aplica o que entra e conduz só as escolhas novas |
| Saber uma regra | `/consultar-regra` | A resposta, com a citação |

## Se você mestra

Comece por `/mestrar`: ele descobre em que altura está seu trabalho e encaminha. Planejar mesa
erra quando se trabalha na escala errada, detalhando a taverna da sessão 1 antes de saber do
que a campanha trata.

```
   /mundo                    só se a mesa roda num mundo de fora
            │
            ▼
   /planejar-campanha        premissa, tom, facções, onde termina
            │
            ▼
   /planejar-aventura  ◄──────────────┐        o problema e quem o causa
            │                         │
            ▼                         │
   /planejar-sessao                   │        as cenas do próximo encontro
            │                         │
            ▼                         │
        /mesa                         │        o jogo acontecendo
            │                         │
            ▼                         │
     /pos-sessao ─────────────────────┘        o que mudou realimenta o plano
```

Em qualquer ponto: `/montar-encontro`, `/criar-pnj`, `/criar-local`, `/gerar-eventos`.

O circuito fecha de propósito. Planejamento que não recebe o resultado da mesa vira ficção
paralela ao jogo real.

## Se você quer jogar num mundo que você gosta

`/mundo` pesquisa a identidade de um mundo de fora do D&D e devolve ele jogável. Ele entrevista
você primeiro, porque você escolheu esse mundo por uma razão que nenhuma wiki registra, e só
depois vai atrás das fontes.

```
/mundo    quero jogar num mundo tipo Fallout
/mundo    a mesa toda gosta de Ben 10
```

O que volta são dois arquivos em `references/<slug>/`: a **identidade** do mundo (o evento que
o fundou, o que ali ocupa o lugar da magia, as facções, o que não existe lá) e a **tradução**,
que diz qual regra de `docs/` sustenta cada povo, cada arquétipo, cada item e cada poder.

Nenhum número é inventado. Uma arma de energia é uma arma que já existe no livro, com outro
nome e outra descrição, e o que a regra não faz vem escrito na seção do que não tem equivalente.
Um script confere isso antes de você confiar no arquivo:

```
tools/valida-referencia.sh references/<slug>
```

Enquanto sobrar lacuna, a skill pesquisa de novo, focada só naquele buraco, e pergunta a você
quando a fonte não resolve. Ela fecha quando não sobra nenhuma.

Tem um pronto no repositório para você ver o formato antes de rodar o seu:
[**A Confraria dos Vis**](references/meu-malvado-favorito/mundo.md), tirado de *Meu Malvado
Favorito*. Nele o aparelho que encolhe é a magia Aumentar/Reduzir com manopla e cano, os miúdos
do porão são Pequeninos (o traço Sorte é o que explica eles saírem inteiros de tudo), e "roubar
a lua" está na lista do que **não** tem equivalente, em vez de ter virado regra nova.

### Mande o seu mundo para cá

Passou na validação, cabe um PR. A ideia é que ninguém precise pesquisar o mesmo mundo duas
vezes: quem já mapeou Ben 10 poupa a próxima mesa que quiser jogar lá. Os cinco critérios de
aceite estão em [`references/README.md`](references/README.md), e a própria skill oferece o PR
quando termina.

## A base de regras

Pronta em [`docs/`](docs/README.md), organizada por domínio:

```
docs/regras/        fundamentos, ações, combate, dano e cura, condições, glossário
docs/classes/       as 12 classes, com progressão 1–20 e 4 subclasses cada
docs/especies/      10 espécies e 16 antecedentes
docs/talentos/      origem, gerais, estilo de luta, dádiva épica
docs/equipamento/   armas com Maestria, armaduras, ferramentas, itens
docs/magias/        as 391 magias
docs/apendices/     multiverso e blocos de estatísticas
```

São as mecânicas: valores, tabelas, características e descrições de efeito. A prosa literária e
a arte do livro ficam de fora.

## Como usar

Abra o projeto no seu agente e peça. Não precisa instalar nada.

```
/criar-personagem     quero um anão clérigo que perdeu a fé
/mestrar              vou começar uma campanha
/consultar-regra      agarrar provoca ataque de oportunidade?
```

Seus personagens ficam em `fichas/`, sua campanha em `mesa/`.

## Exemplos

Conversas inteiras, com o que você pede e o que volta, em [`exemplos/`](exemplos/README.md):

| Exemplo | A referência que entrou | O que ele mostra |
|---|---|---|
| [Teodoro Vasques, o Tecelão](exemplos/homem-aranha.md) | [Homem-Aranha](https://pt.wikipedia.org/wiki/Homem-Aranha) | Cada poder achado em `docs/` e citado; o que a regra não concede, dito na cara |
| [Japeth, o bode da Garganta de Corvo](exemplos/bode-japeth.md) | [Japeth, de *Deu a Louca na Chapeuzinho*](https://pt.wikipedia.org/wiki/Deu_a_Louca_na_Chapeuzinho) | Bloco do apêndice B, e a adaptação marcada como adaptação |

Referência de fora entra como comportamento e sai como personagem do mundo. O nome que veio do
cinema ou do quadrinho não aparece na mesa, e nenhuma regra é inventada para imitar o original.

## Créditos

Dungeons & Dragons e o Livro do Jogador pertencem à Wizards of the Coast. A tradução brasileira
é da equipe Heróis Anônimos. As skills são livres para usar e modificar.
