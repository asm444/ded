# Exemplos

Como pedir, e o que esperar de volta. Os exemplos aqui são de conversa em mesa, não de código.

## A regra da imersão

Toda mesa recebe referência de fora — um herói de quadrinhos, um bicho de desenho, um
personagem de filme. O agente aceita a referência como **pedido**, e nunca como **resposta**:

1. **A referência entra como comportamento, não como nome.** "Anda em parede", "prende gente
   com teia", "pressente o golpe" é o que serve. O nome de fora fica na conversa de
   planejamento e não aparece no que vai à mesa.
2. **A mecânica vem do `docs/`, citada.** Nada de característica inventada para imitar o
   original. O que a referência faz e as regras não fazem, o agente diz que não faz.
3. **O personagem ganha nome, lugar e razão no mundo.** Sem isso, é fantasia com outra roupa,
   e a mesa sente.

## O procedimento

```
   referência                o que ela FAZ            mecânica que já existe
   (fora da mesa)   ───►     em uma linha    ───►     em docs/, com citação
                                                              │
                              nome, lugar e razão   ◄─────────┘
                              dentro do mundo
                                     │
                                     ▼
                        o que não tem equivalente,
                        dito na cara
```

## Os exemplos

| Exemplo | Skill | O pedido | O que ele ensina |
|---|---|---|---|
| [homem-aranha.md](homem-aranha.md) | `/criar-personagem` | [Homem-Aranha](https://pt.wikipedia.org/wiki/Homem-Aranha) | Traduzir poder em característica de classe, talento e equipamento — e recusar o que não existe |
| [bode-japeth.md](bode-japeth.md) | `/criar-pnj` | [Japeth, de *Deu a Louca na Chapeuzinho*](https://pt.wikipedia.org/wiki/Deu_a_Louca_na_Chapeuzinho) | Usar o limite honesto do projeto: sem bestiário, o bloco vem do apêndice B e a adaptação é declarada |

Cada exemplo abre com as duas imagens lado a lado: **a referência que entrou** e **o personagem
que saiu**. O retrato do lado direito é vetorial (`assets/*.svg`), feito para o repositório —
troque pelo que você quiser trocando o `src` da imagem.

### Resumo do primeiro

O agente nunca escreve "Homem-Aranha" na resposta final. Ele separa os cinco comportamentos do
conceito, acha cada um em `docs/` — Monge para agilidade e reação, Rede do equipamento para a
teia, talento Alerta para o pressentimento, talento Atleta para a escalada — e devolve
**Teodoro Vasques, o Tecelão**, com o que ainda falta escolher e o que a regra não concede.

### Resumo do segundo

O agente cria **Japeth**, o bode que responde tudo cantando, com o que ele quer, o que sabe e
sob qual condição conta. As estatísticas saem do bloco Cabra Gigante do apêndice B, e as duas
coisas que o bloco não tem — falar e cantar — vão marcadas como adaptação do Mestre, não como
regra.

## Como usar estes exemplos

Não copie a ficha. Copie o **caminho**: comportamento em uma linha, busca em `docs/`, citação,
e a lista honesta do que ficou de fora. O conceito da sua mesa vai ser outro; o procedimento é
o mesmo.
