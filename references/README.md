# Mundos de referência

Um mundo que você gosta, traduzido em mesa de D&D 2024. Cada pasta aqui é um mundo que alguém
pesquisou e mapeou: o que dá identidade a ele, e qual regra de [`docs/`](../docs/README.md)
sustenta cada elemento — sem uma mecânica inventada.

Quem produz isso é a skill [`/mundo`](../.claude/skills/mundo/SKILL.md). Quem confere é
[`tools/valida-referencia.sh`](../tools/valida-referencia.sh).

## Os mundos

| Mundo | Pasta | Faixa de níveis |
|---|---|---|
| A Confraria dos Vis | [meu-malvado-favorito](meu-malvado-favorito/) | 1 a 8 |

O primeiro serve de exemplo do formato: veja como o aparelho que encolhe vira a magia
Aumentar/Reduzir sem ganhar um número novo, e como "roubar a lua" desce para a seção do que não
tem equivalente em vez de virar regra.

## O que tem dentro de cada pasta

    references/<slug>/
    ├── mundo.md      identidade: premissa, evento fundador, tom, a lei do mundo,
    │                 geografia, facções, povos, economia, perigos, estética,
    │                 o que não existe, faixa de níveis, ganchos e fontes
    └── traducao.md   o mapa mecânico: povo→espécie, arquétipo→classe,
                      item→equipamento, efeito→magia — cada linha citando docs/

`mundo.md` é o que você lê antes de jogar. `traducao.md` é o que você consulta com o grupo
esperando.

## Como contribuir com um mundo

1. `/mundo` no seu agente, e responda o que ele perguntar. Ele é quem sabe a metodologia.
2. `tools/valida-referencia.sh references/<slug>` até sair `OK`.
3. Abra o PR com a saída do validador colada no corpo, e a linha do índice acima preenchida.

Um mundo por PR.

## Os cinco critérios de aceite

1. **Nenhuma mecânica inventada.** Toda linha de `traducao.md` cita `docs/<domínio>/<arquivo>.md`.
   O que a regra não faz vai em `## Sem equivalente`, com o mais próximo e a diferença. Reskin
   muda nome e descrição, nunca número.
2. **Nenhuma lacuna aberta.** Os treze critérios de `mundo.md` preenchidos, ou marcados
   `NÃO SE APLICA — <motivo>`. Sem "a definir".
3. **Fonte no texto.** Toda afirmação sobre o mundo marcada com `[fonte: <URL>]`,
   `[fonte: você]` ou `[não verificado]`. Mínimo de três fontes com URL. Em `traducao.md`,
   `[não verificado]` reprova: mecânica sem fonte não vai à mesa.
4. **Derivação, não reprodução.** Nada de texto copiado da obra, nada de arte, nada de tabela
   transcrita. O arquivo é um mapa de tradução com referência bibliográfica, e a obra original
   continua sendo de quem é.
5. **O nome da franquia fica em `## Origem e fontes`.** O material que vai à mesa usa os nomes
   derivados, como já manda a regra de imersão em [`AGENTS.md`](../AGENTS.md) e mostram os
   [`exemplos/`](../exemplos/README.md). O validador reprova o nome de origem fora dessa seção.

O critério 5 é o mesmo que faz o Homem-Aranha virar *Teodoro Vasques, o Tecelão*. O que muda
aqui é a escala: a franquia inteira vira um mundo com nome próprio, e a pasta guarda de onde
ele veio.

## O que o script não pega

Ele mede o que dá para medir, e quem revisa o PR cuida do resto. Medido em `tools/test/`:

- **Número solto passa.** `2d6`, `CD 15`, `CA 18` e `12 PV` sem fonte reprovam. "O talismã tem
  10 cargas" não reprova, porque exigir fonte para todo algarismo reprovaria "três facções".
- **Reskin honesto ele não distingue de reskin desonesto.** Citar `docs/equipamento/` numa linha
  que muda o dano da arma passa no script. Quem lê o PR confere se o número é o do livro.
- **Fonte fraca ele conta como fonte.** Três URLs quaisquer satisfazem o mínimo. Fonte de
  segunda mão é problema de revisão, não de sintaxe.

## Começar do zero

Copie [`MODELO.md`](MODELO.md) para `references/<slug>/mundo.md` e preencha, se preferir escrever
à mão em vez de conversar com a skill. O validador cobra o mesmo dos dois caminhos.
