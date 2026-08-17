<div align="center">

<img src="assets/ded.png" alt="DED" width="340">

# DED

**D**ata · **E**thics · **D**efense · **I**ntegrity · **D**ecision

*Nobody should have to read 397 pages before sitting at the table.*

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
   /mundo                    only if the table runs in an outside world
            │
            ▼
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

## If you want to play in a world you love

`/mundo` researches the identity of a world from outside D&D and hands it back playable. It
interviews you first, since you picked that world for a reason no wiki records, and only then
goes after the sources.

```
/mundo    I want to play in something like Fallout
/mundo    the whole table is into Ben 10
```

You get two files in `references/<slug>/`: the world's **identity** (its founding event, what
takes the place of magic there, the factions, what does not exist in it) and the **translation**,
naming which rule in `docs/` backs each people, archetype, item and power.

No number is invented. An energy weapon is a weapon the book already has, renamed and
redescribed, and whatever the rules cannot do is written down under what has no equivalent.
A script checks that before you trust the file:

```
tools/valida-referencia.sh references/<slug>
```

While a gap remains, the skill researches again, aimed only at that gap, and asks you when the
sources fall short. It closes when nothing is left open.

One is already in the repository, so you can see the format before running your own:
[**A Confraria dos Vis**](references/meu-malvado-favorito/mundo.md), derived from *Despicable
Me*. The shrink ray there is the Enlarge/Reduce spell with a grip and a barrel, the basement
crowd are Halflings (their Lucky trait is what explains them walking away from everything), and
"stealing the moon" sits in the list of what has **no** equivalent instead of becoming a new rule.

### Send your world here

Once it validates, it can be a PR, so nobody researches the same world twice. The five
acceptance criteria live in [`references/README.md`](references/README.md), and the skill
offers the PR itself when it finishes.

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
