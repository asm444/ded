<div align="center">

<img src="assets/ded.png" alt="DED" width="340">

# DED

**D**ata · **E**thics · **D**efense · **I**ntegrity · **D**ecision

A table paladin for D&D 2024, in Brazilian Portuguese.

[Português](README.md) · [Rules base](docs/README.md) · [Agent guide](AGENTS.md)

</div>

---

## What this is

An environment where an AI agent walks you through D&D 2024: builds a character, turns a loose
idea into a playable sheet, plans a campaign and runs the table. Rules come from the book, with
the page cited. When the agent cannot find a rule, it says so instead of making one up.

Built with free models, through [opencode](https://opencode.ai). That is the point: playing
D&D should not require an AI subscription or memorizing 397 pages first.

The rules base and the skills are written in Portuguese, since that is the language of the
book this was built for.

## What you can do

| You want | Say | What happens |
|---|---|---|
| A new character | `/criar-personagem` | The 5 official steps, ending in a sheet that passes the validator |
| An idea made playable | `/gerar-historia` | Backstory anchored in the multiverse, turned into skill, feat and spell choices |
| A rule answered | `/consultar-regra` | The answer, with the citation |
| A progression planned | `/planejar-build` | Level by level, with numbers where numbers apply |
| To run the game | `/mestrar` | Routes you to the right altitude: campaign, adventure, session or table |

## The Dungeon Master circuit

Table prep goes wrong when you work at the wrong scale, detailing the session-1 tavern before
knowing what the campaign is about. The circuit keeps each decision at its own altitude.

```
   /planejar-campanha        premise, tone, factions, how it ends
            │
            ▼
   /planejar-aventura  ◄──────────────┐        the problem and who causes it
            │                         │
            ▼                         │
   /planejar-sessao                   │        the scenes of the next session
            │                         │
            ▼                         │
        /mesa                         │        the game, happening
            │                         │
            ▼                         │
     /pos-sessao ─────────────────────┘        what changed feeds the plan back
```

Components any altitude can call: `/montar-encontro`, `/criar-pnj`, `/criar-local`,
`/gerar-eventos`.

The loop closes on purpose. Planning that never receives the table's outcome becomes fiction
running parallel to the actual game.

## How the rules base is built

The book is typeset with one font per semantic role, so the extractor decides what is a
heading, a table or body text from **typography**, not from guessing at the text:

| Font in the PDF | Role |
|---|---|
| `WolpePegasus 64pt` | Class name |
| `MrsEavesOT-Roman 12pt` | Spell name |
| `TTJenevers-BoldItalic 9pt` | Run-in heading inside a paragraph |
| `ScalaSans-BoldLF 9pt` | Table cell label |

That makes extraction verifiable by counting. If the table of contents promises 48 subclasses
and 47 come out, the defect announces itself:

```
classes .......... 12    matches the table of contents
subclasses ....... 48    4 per class
spells ........... 391   zero alphabetical inversions
conditions ....... 15    one occurrence each
progression ...... 20 levels × 6 columns, uniform width
```

The alphabetical order of spells is the most useful oracle of all: any inversion means the
reading flow between the two columns broke, and text may have landed under the wrong name.

## Getting started

You need your own copy of the 2024 Player's Handbook as a PDF, in the project root.

```bash
pip install --user pymupdf
python3 tools/gerar_docs.py todos      # builds docs/ from your PDF
```

Then just ask. To check a sheet at any point:

```bash
python3 tools/validar_ficha.py fichas/exemplo-thorin.json
```

The validator checks what is decidable by arithmetic: proficiency bonus against level, hit
points possible for the hit die and Constitution, the 27-point ceiling on point buy.

## Layout

```
tools/           extrair.py, gerar_docs.py, validar_ficha.py
.claude/skills/  the 15 skills
docs/            the rules base (generated from your PDF, not versioned)
fichas/          characters as JSON
mesa/            your campaign (created when you start running one)
```

## About the book

This repository does not distribute the Player's Handbook. `docs/` is generated from **your**
copy and stays out of version control. Dungeons & Dragons and the Player's Handbook belong to
Wizards of the Coast; the Brazilian translation used here is by the Heróis Anônimos team.

The tools and skills are free to use and modify.
