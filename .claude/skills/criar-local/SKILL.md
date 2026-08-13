---
name: criar-local
description: Cria um lugar explorável (masmorra, cidade, ruína, covil) com o que há para descobrir, o que oferece perigo e por que alguém iria lá. Acionar com /criar-local, a partir do planejamento, ou quando o usuário pedir um cenário para o grupo explorar.
---

# Criar local

Um lugar existe para gerar decisão. Se atravessá-lo não exige escolha nenhuma, ele é um
corredor com descrição — corte e vá direto ao que importa.

## O mínimo

1. **Por que o grupo vem aqui.** Sem motivo, o local não entra em jogo.
2. **A primeira impressão**, em três linhas: o que se vê, ouve e cheira. Só isso — o resto sai
   quando perguntarem.
3. **Três a seis áreas**, cada uma com uma coisa: algo para descobrir, algo que ameaça, ou
   algo que decide. Área sem nenhuma das três é enchimento.
4. **Uma verdade escondida.** O que o lugar não conta de cara e recompensa quem investigar.
5. **Como se sai.** Inclusive a saída ruim: o que acontece se fugirem no meio.

## Ligue à mecânica

Sem isso o local vira texto. Use o que já está definido em `docs/regras/`:

- **Luz** — Escuridão e Meia-luz mudam quem enxerga; Visão no Escuro está em
  `docs/regras/glossario.md` e várias espécies a têm.
- **Terreno difícil** — cada metro custa o dobro; muda perseguição e recuo.
- **Cobertura** — parcial (+2 CA), três quartos (+5), total (não pode ser alvo).
- **Riscos** — queda, combustão, asfixia, desidratação e desnutrição estão definidos no
  glossário com dano e CD.
- **Testes esperados** — diga qual perícia e qual CD para as descobertas prováveis, para não
  ter que arbitrar no susto.

## Escalas

- **Masmorra ou covil**: as áreas acima, com um mapa em texto (o que liga a quê).
- **Assentamento**: quem manda, do que vive, qual é a tensão e três lugares com nome.
- **Região**: o que se atravessa, quanto tempo leva (`docs/regras/exploracao.md` traz viagem) e
  o que se encontra no caminho.

## Saída

Local recorrente vai para `mesa/locais/<slug>.md`, em formato de consulta — você vai ler isso
com o grupo esperando, então a informação que se usa primeiro vem primeiro.
