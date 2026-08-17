---
name: mestrar
description: Porta de entrada do circuito de Mestre — descobre em que altura o trabalho está (campanha, aventura, sessão, mesa ou pós-sessão) e encaminha para a skill certa. Acionar com /mestrar, ou quando o usuário disser que vai mestrar, que quer montar uma mesa, ou pedir ajuda de Mestre sem dizer em qual escala.
---

# Mestrar

Roteia o trabalho de Mestre para a altura certa. Existe porque o erro mais caro do
planejamento de mesa é trabalhar na escala errada: detalhar a taverna da sessão 1 quando
ainda não se sabe do que a campanha trata, ou querer decidir o clímax do nível 15 antes da
primeira sessão.

## As seis alturas

| Altura | Skill | Pergunta que ela responde | Quando |
|---|---|---|---|
| Mundo | `mundo` | Em que mundo isso se passa, e como ele vira regra? | Só quando a mesa usa um mundo de fora |
| Campanha | `planejar-campanha` | Do que essa história trata, e onde termina? | Uma vez, no começo |
| Aventura | `planejar-aventura` | Qual é o problema deste arco e como ele se resolve? | A cada 3–6 sessões |
| Sessão | `planejar-sessao` | O que acontece no próximo encontro do grupo? | Antes de cada sessão |
| Mesa | `mesa` | O que acontece agora, com o grupo esperando? | Durante o jogo |
| Fechamento | `pos-sessao` | O que mudou, e o que isso abre? | Depois de cada sessão |

Componentes chamados por qualquer altura: `criar-pnj`, `criar-local`, `montar-encontro`.

## Como rotear

Pergunte só o que não dá para inferir: existe campanha em andamento? Quando é a próxima
sessão? Qual o nível do grupo?

- O usuário nomeou um mundo de fora do D&D (série, jogo, filme, livro) e não existe
  `references/<slug>/` para ele → `mundo` primeiro. Se a pasta existe, leia e siga para a
  altura seguinte. Campanha montada antes do mundo fixado retrabalha inteira quando o mundo
  contradiz o que já foi decidido.
- Sem campanha definida → `planejar-campanha`. Não pule: sem premissa e tom, toda sessão vira
  improviso desconexo.
- Campanha existe, arco atual terminou ou não existe → `planejar-aventura`.
- Aventura em curso e sessão marcada → `planejar-sessao`.
- Está jogando agora → `mesa`. Nesse caso responda rápido e não abra planejamento.
- Sessão acabou → `pos-sessao`.

Quando o pedido couber em duas alturas, escolha a **mais alta ainda indefinida**. Planejar a
sessão 4 sem saber para onde a aventura vai produz trabalho que será jogado fora.

## O circuito

```
mundo  (só se a mesa usa um mundo de fora)
        │
        ▼
planejar-campanha
        │
        ▼
planejar-aventura ◄─────────────┐
        │                       │
        ▼                       │
planejar-sessao                 │
        │                       │
        ▼                       │
      mesa  (jogo acontecendo)  │
        │                       │
        ▼                       │
   pos-sessao ──────────────────┘
     consequências realimentam a aventura;
     aventura encerrada devolve à campanha
```

O circuito fecha: o que o grupo fez na mesa muda a aventura, e aventura concluída atualiza a
campanha. Planejamento que não recebe o resultado da mesa vira ficção paralela ao jogo real.

## Onde os artefatos moram

    references/<slug>/         o mundo de fora, se houver, versionado e compartilhável
    mesa/campanha.md           premissa, tom, facções, arco
    mesa/aventuras/<slug>.md   um arquivo por arco
    mesa/sessoes/<n>.md        preparo e, depois, o que aconteceu
    mesa/pnjs/<slug>.md        PNJs recorrentes
    mesa/locais/<slug>.md      locais recorrentes

## Limite do material

O projeto tem o Livro do **Jogador**: regras, classes, magias, equipamento e os animais do
apêndice B. Não tem bestiário nem as tabelas de construção de encontro do Guia do Mestre.
Onde isso for necessário, as skills pedem que você traga o monstro ou trabalham com o que há.
Diga isso ao usuário em vez de inventar estatística de monstro.
