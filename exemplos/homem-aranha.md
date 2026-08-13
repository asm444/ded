# Exemplo — "quero jogar o Homem-Aranha"

<table>
<tr>
<td width="50%" align="center"><img src="../assets/homem-aranha.jpg" alt="Homem-Aranha" width="290"><br><sub><b>Entrou:</b> a referência —
<a href="https://pt.wikipedia.org/wiki/Homem-Aranha">Homem-Aranha</a></sub></td>
<td width="50%" align="center"><img src="../assets/tecelao.svg" alt="Teodoro Vasques, o Tecelão" width="250"><br><sub><b>Saiu:</b> Teodoro Vasques, o Tecelão</sub></td>
</tr>
</table>

Skill: `/criar-personagem`. O que este exemplo mostra: traduzir um herói de fora da mesa em
ficha de D&D 2024 sem citar o herói no resultado, e sem inventar regra para imitá-lo.

---

## Você diz

```
/criar-personagem quero jogar o Homem-Aranha
```

## O agente responde

> Dá para fazer, e não como piada: esse conceito traduz bem. Antes de escolher a classe, vou
> separar o que é **poder** do que é **nome**. O nome fica fora da mesa; os poderes eu procuro
> em `docs/`, um por um. O que eu não achar, eu digo que não achei.
>
> Três coisas, em um lote só. No que você não responder, eu assumo e digo o que assumi:
>
> 1. Qual é o nível inicial? (assumo 1, com o caminho até o 4 desenhado)
> 2. O grupo já existe? (assumo grupo novo)
> 3. Ele é um herói de rua, preso a uma cidade, ou o conceito fica solto em qualquer cenário?
>    (assumo herói de cidade)

### O mapa: poder → mecânica

| O que ele faz | Como isso existe em 2024 | Onde |
|---|---|---|
| Anda em parede e teto | Monge, **Movimento Acrobático** (nível 9): move-se por superfícies verticais no próprio turno sem cair | `docs/classes/monge.md`, p. 159–165 |
| Anda em parede *antes* do nível 9 | Talento **Atleta** (nível 4+, For ou Des 13+): Deslocamento de Escalada igual ao Deslocamento | `docs/talentos/talentos.md`, p. 199–211 |
| Prende o inimigo com teia | **Rede** (1 PO): na ação Atacar, substitui um dos ataques; o alvo faz uma salvaguarda de Destreza CD 8 + mod Des + BP ou fica **Contido** | `docs/equipamento/equipamento.md`, p. 213–233 |
| Sentido de perigo | Talento **Alerta**: Bônus de Proficiência na Iniciativa, e troca de Iniciativa com um aliado | `docs/talentos/talentos.md`, p. 199–211 |
| Desviar do golpe que vem | Monge, **Defletir Ataques** (nível 3): uma Reação reduz o dano em 1d10 + mod Des + nível de Monge, e por 1 Ponto de Foco redireciona a força contra outro alvo | `docs/classes/monge.md` |
| Cair do alto e levantar | Monge, **Queda Lenta** (nível 4): uma Reação reduz o dano da queda em 5 × nível de Monge | `docs/classes/monge.md` |
| Bater rápido, sem arma | Monge, **Artes Marciais** (nível 1): Ataque Desarmado como Ação Bônus, dano 1d6, e ataques com Destreza em vez de Força | `docs/classes/monge.md` |
| Empurra, derruba, desorienta | Subclasse **Combatente da Mão Espalmada** (nível 3): Derrubar, Desorientar ou Empurrar 4,5 m ao acertar com a Torrente de Golpes | `docs/classes/monge.md` |
| O cientista por trás da máscara | Antecedente **Escriba**: Destreza, Inteligência, Sabedoria; talento Habilidoso; Investigação e Percepção | `docs/especies/antecedentes.md`, p. 177–185 |

> **Duas observações honestas**, antes de você aprovar:
>
> - A **Rede** não é arma no material de 2024: ela está em Equipamento de Aventura, não usa
>   jogada de ataque e alcança 4,5 metros. Ela prende, e não balança ninguém pela cidade.
> - A magia **Teia** existe (2º Círculo, Invocação, Cubo de 6 m, `docs/magias/descricoes.md`),
>   mas é da lista de Feiticeiro e Mago. Monge não conjura, então ela só entra se você aceitar
>   multiclasse — e aí o personagem vira outro. Recomendo ficar com a Rede e narrar o efeito
>   como teia: a mecânica é a mesma, e a ficha continua limpa.

### A ficha, nível 1

> **Teodoro Vasques**, o **Tecelão** — Humano, Monge nível 1, antecedente Escriba.
>
> | Campo | Valor | De onde vem |
> |---|---|---|
> | Atributos (Custo de Pontos, 27) | Des 15, Sab 14, Con 13, Int 12, For 10, Car 8 | `docs/personagem/criacao.md` |
> | Depois dos aumentos do Escriba (+2 Des, +1 Int) | **Des 17 (+3)**, Sab 14 (+2), Con 13 (+1), Int 13 (+1), For 10 (+0), Car 8 (–1) | `docs/especies/antecedentes.md` |
> | PV | 9 (8 do d8 cheio, no nível 1, mais 1 de Constituição) | `docs/classes/monge.md` |
> | CA | **15** = 10 + Des + Sab, Defesa sem Armadura | `docs/classes/monge.md` |
> | Espécie | Humano: Eficiente, Hábil (1 perícia), **Versátil → talento Alerta** | `docs/especies/especies.md` |
> | Talento de origem | Habilidoso, do Escriba: 3 perícias ou ferramentas | `docs/talentos/talentos.md` |
> | Perícias e ferramentas | Investigação, Percepção e Suprimentos de Calígrafo (Escriba); Acrobacia e Furtividade (Monge); Atletismo, Intuição e Ferramentas de Ladrão (Habilidoso); mais 1 perícia do traço Hábil | — |
> | Equipamento notável | **3 Redes** (1 PO cada), Corda, Suprimentos de Calígrafo | `docs/equipamento/equipamento.md` |
>
> Conferido à mão: 15, 14, 13, 12, 10 e 8 custam exatamente 27 pontos, e o teto de 15 vale
> **antes** dos aumentos do antecedente, por isso a Destreza 17 é válida.
>
> O caminho daqui: no nível 3 entram Defletir Ataques e a Mão Espalmada. No 4, recomendo o
> talento **Atleta** em vez do aumento de atributo, porque é ele que dá a escalada cinco níveis
> antes do Monge. No 9, a escalada vira andar em parede, sem custo nenhum.

### O nome no mundo

> "Homem-Aranha" não vai à mesa. O que vai é isto: Teodoro perdeu o tio numa emboscada da
> Guilda dos Fiadores, no bairro dos tecelões, e passou a caçar a guilda mascarado, usando
> contra ela a rede que ela mesma fabrica. De dia trabalha como copista, porque é o emprego
> que lhe dá acesso aos registros da guilda.
>
> É a mesma história, com nomes que existem no mundo. Ninguém na mesa precisa ter lido
> quadrinho para entender quem ele é.

### O que ficou de fora

> - **Balançar de teia entre prédios** não tem mecânica: a Rede alcança 4,5 metros e prende, e
>   é só isso que ela faz. O resto é ficção de mesa, e quem decide é o Mestre. Nada em `docs/`
>   concede esse movimento.
> - **Grudar parado no teto** não é o que o Movimento Acrobático diz: ele vale no seu turno,
>   durante o movimento. Ficar pendurado é conversa com o Mestre.
>
> Fecho no passo 5 com `gerar-historia`, para amarrar a Guilda dos Fiadores a uma facção da
> campanha e devolver ganchos ao Mestre. Quer que eu siga, ou prefere ajustar o mapa antes?
