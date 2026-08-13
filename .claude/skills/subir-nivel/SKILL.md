---
name: subir-nivel
description: Sobe um personagem existente de nível, aplicando o que entra e conduzindo as escolhas do nível novo. Acionar com /subir-nivel, ou quando o usuário disser que o personagem subiu ("o Thorin chegou ao 6", "subimos de nível", "level up").
---

# Subir de nível

Aplica um nível a uma ficha de `fichas/`, atualiza os derivados e conduz só as escolhas que o
nível novo abre.

## Procedimento

1. Leia a ficha e confirme classe, nível atual e subclasse.
2. Em `docs/classes/<classe>.md`, leia a linha do nível-alvo na tabela de características.
3. Aplique o que é automático:
   - PV: role o dado de vida e some o modificador de Constituição, ou use o valor fixo
     (metade do dado + 1 + Con). Diga qual método usou.
   - Bônus de proficiência, se mudou (níveis 5, 9, 13, 17).
   - Espaços de magia e magias conhecidas ou preparadas, se a classe conjura.
4. Conduza o que é escolha: subclasse (nível 3), aumento de atributo ou talento, magias novas,
   opções de característica (manobras, invocações, metamagia, conforme a classe).
5. Grave a ficha e confira os derivados: PV somados com o modificador de Constituição, e
   bônus de proficiência acompanhando o nível.

## Cuidados

- Aumento de valor de atributo tem teto 20; se o personagem já está no teto, o talento é a
  única opção útil.
- Personagem multiclasse soma níveis para bônus de proficiência e espaços de magia, mas as
  características vêm do nível **naquela** classe. Confira em `docs/personagem/multiclasse.md`.
- Se o PV subir sem o modificador de Constituição, ou se o bônus de proficiência não
  acompanhar o nível, a ficha está errada. Corrija antes de entregar.
