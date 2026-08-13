# Projeto ded

Ambiente de mesa para D&D 2024 (PT-BR): base de regras extraída do livro, ferramentas de
cálculo e skills para criar personagem, desenvolver build e conduzir sessão.

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
| `tools/` | `extrair.py` (PDF → estrutura), `gerar_docs.py` (estrutura → docs) |
| `fichas/` | Personagens salvos, um arquivo por personagem |

## Regra de citação

Toda afirmação sobre regra cita a origem: `docs/<dominio>/<arquivo>.md` e a página do livro
que o cabeçalho do arquivo declara. Regra que você não localizou no `docs/` você marca como
não verificada — nunca preenche de memória, porque a versão 2024 mudou o que a de 2014 dizia.

## O que os docs contêm e o que não contêm

Os `docs/` trazem mecânica: valores, tabelas, características, condições, descrições de
efeito. A prosa literária, a ficção e a arte do livro ficam de fora — para essas, o PDF é a
fonte. Ao responder sobre ambientação e sabor, diga que o `docs/` não cobre isso.

## Regenerar a base

    python3 tools/extrair.py sumario           # índice do livro, com páginas
    python3 tools/extrair.py texto 51 57       # texto marcado de um intervalo
    python3 tools/gerar_docs.py todos          # reescreve docs/ inteiro

`extrair.py` decide o papel de cada linha pela fonte do PDF, não por heurística de texto.
Alterar `HEADINGS`, `RUNIN` ou `ROTULO` muda a estrutura de todos os documentos de uma vez.

### Invariantes que provam a extração

Depois de mexer no extrator, estas contagens têm de continuar valendo:

    python3 -c "print(len(open('docs/magias/descricoes.md').read().split(chr(10)+'##### '))-1)"  # 391 magias
    ls docs/classes/*.md | wc -l                                                                  # 12 classes
    grep -c '^##### Nível' docs/classes/barbaro.md                                                 # características por nível

As magias saem em ordem alfabética: qualquer inversão indica que a ordem de leitura entre as
duas colunas quebrou, e que texto pode estar sob o nome errado.

## Convenções

- Medidas em metros e quilogramas, como no livro em PT-BR.
- Moedas: PC, PP, PE, PO, PL.
- Nomes de regra em maiúscula inicial quando são termo do jogo (Fúria, Vantagem, Descanso Longo).
- Ficha de personagem é JSON em `fichas/`; a renderização é derivada, nunca a fonte.
