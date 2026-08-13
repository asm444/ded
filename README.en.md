<div align="center">

<img src="assets/ded.png" alt="DED" width="340">

# DED

**D**ata · **E**thics · **D**efense · **I**ntegrity · **D**ecision

An AI companion for playing D&D 2024 in Brazilian Portuguese.

[Português](README.md) · [Rules base](docs/README.md) · [Agent guide](AGENTS.md)

</div>

---

## What this is

An AI agent that sits at the table with you. On the player side, it builds characters and turns
a loose idea into a playable sheet. On the DM side, it plans the campaign, preps the session and
helps run the game.

The rules are already here, and it answers citing the page. When it cannot find a rule, it says
so instead of making one up.

Built with free models, through [opencode](https://opencode.ai). Playing D&D should not require
an AI subscription or memorizing 397 pages first.

The rules base and the skills are in Portuguese, the language of the book this was built for.

## If you play

| You want | Say | What happens |
|---|---|---|
| A new character | `/criar-personagem` | The 5 official steps, from concept to finished sheet |
| An idea made playable | `/gerar-historia` | Backstory anchored in the multiverse, turned into skill, feat and spell choices |
| A progression planned | `/planejar-build` | Level by level, with numbers where numbers apply |
| To level up | `/subir-nivel` | Applies what comes in, walks you through the new choices |
| A rule answered | `/consultar-regra` | The answer, with the citation |

## If you run the game

Start with `/mestrar`: it works out which altitude your task belongs to and routes you. Table
prep goes wrong when you work at the wrong scale, detailing the session-1 tavern before knowing
what the campaign is about.

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

Available at any point: `/montar-encontro`, `/criar-pnj`, `/criar-local`, `/gerar-eventos`.

The loop closes on purpose. Planning that never receives the table's outcome becomes fiction
running parallel to the actual game.

## The rules base

Ready in [`docs/`](docs/README.md), organized by domain:

```
docs/regras/        fundamentals, actions, combat, damage and healing, conditions, glossary
docs/classes/       all 12 classes, levels 1-20, 4 subclasses each
docs/especies/      10 species and 16 backgrounds
docs/talentos/      origin, general, fighting style, epic boon feats
docs/equipamento/   weapons with Mastery, armor, tools, items
docs/magias/        all 391 spells
docs/apendices/     multiverse and stat blocks
```

These are the mechanics: values, tables, features and effect descriptions. The book's prose and
art are not included.

## Using it

Open the project in your agent and ask. Nothing to install.

```
/criar-personagem     I want a dwarf cleric who lost their faith
/mestrar              I'm starting a campaign
/consultar-regra      does grappling provoke an opportunity attack?
```

Your characters live in `fichas/`, your campaign in `mesa/`.

## Credits

Dungeons & Dragons and the Player's Handbook belong to Wizards of the Coast. The Brazilian
translation is by the Heróis Anônimos team. The skills are free to use and modify.
