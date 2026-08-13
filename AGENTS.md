# Projeto ded

Auxílio de IA para mesa de D&D 2024 em português: ajuda a criar personagem, a desenvolver a
ideia dele, e a planejar e conduzir a campanha. As regras já estão em `docs/`, prontas.

## Onde está o quê

| Caminho | Conteúdo |
|---|---|
| `docs/regras/` | Fundamentos, ações, combate, dano e cura, condições, exploração, glossário |
| `docs/classes/` | Uma classe por arquivo, com progressão 1–20 e as 4 subclasses |
| `docs/especies/` | Espécies e antecedentes |
| `docs/talentos/` | Talentos de origem, gerais, estilo de luta e dádiva épica |
| `docs/equipamento/` | Armas com Maestria, armaduras, ferramentas, itens, serviços |
| `docs/magias/` | Regras de conjuração e as 391 magias |
| `docs/apendices/` | Multiverso e blocos de estatísticas |
| `fichas/` | Personagens salvos, um arquivo por personagem |
| `mesa/` | Campanha, aventuras, sessões, PNJs e locais |

## As skills

**Jogador:** `criar-personagem`, `gerar-historia`, `planejar-build`, `subir-nivel`.

**Mestre:** `mestrar` roteia para a altura certa, e dela saem `planejar-campanha`,
`planejar-aventura`, `planejar-sessao`, `mesa` e `pos-sessao`. Componentes que qualquer uma
chama: `montar-encontro`, `criar-pnj`, `criar-local`, `gerar-eventos`.

**Sempre disponível:** `consultar-regra`.

## Regra de citação

Toda afirmação sobre regra cita a origem: `docs/<dominio>/<arquivo>.md` e a página do livro
que o cabeçalho do arquivo declara. Regra que você não localizou no `docs/` você marca como
não verificada, nunca preenche de memória: a versão 2024 mudou o que a de 2014 dizia.

## O que os docs contêm

Mecânica: valores, tabelas, características, condições e descrições de efeito. A prosa
literária, a ficção e a arte do livro não estão aqui. Ao responder sobre ambientação e sabor,
diga que o `docs/` não cobre isso.

O que também não está: bestiário e as tabelas de construção de encontro, que vivem no Livro do
Mestre. O apêndice B traz os animais e montarias do Livro do Jogador. Para monstros, peça o
bloco de estatísticas ao Mestre.

## Convenções

- Medidas em metros e quilogramas, como no livro em PT-BR.
- Moedas: PC, PP, PE, PO, PL.
- Nomes de regra em maiúscula inicial quando são termo do jogo (Fúria, Vantagem, Descanso Longo).
- Ficha de personagem é JSON em `fichas/`; a renderização é derivada, nunca a fonte.
