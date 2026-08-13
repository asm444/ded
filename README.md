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

## Créditos

Dungeons & Dragons e o Livro do Jogador pertencem à Wizards of the Coast. A tradução brasileira
é da equipe Heróis Anônimos. As skills são livres para usar e modificar.
