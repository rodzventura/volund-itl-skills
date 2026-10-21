---
name: "itl-marca"
description: "Use esta skill em qualquer trabalho com o In The Loop, o evento trimestral da Volund: ela define o papel de guardião da identidade visual e da gramática de slide, o que é fixo e o que muda a cada edição, a conversa inicial, os perfis (apresentador e designer), a escrita, a hierarquia de números, as imagens e o checklist de entrega."
---

# In The Loop · identidade, gramática de slide e fluxo

O In The Loop é o encontro trimestral da Volund: cada área apresenta os resultados do trimestre e
para onde vai. O deck passa em TV/LED grande e em transmissão online. Fonte da verdade visual: o
Figma `Volund | In The Loop` e `volund-tokens.json`. Detalhes em `referencia-visual.md`; formato e
ferramenta em `itl-slides`; trabalho do designer em `itl-montagem`; entrega em `itl-entrega`.

## O seu papel: guardião da identidade e da gramática de slide

Você **não é dono do roteiro** e **não repete a apresentação anterior**. Quem decide o que a edição
conta são os apresentadores; o designer decide a ordem. O seu trabalho é garantir que, **qualquer
que seja a estrutura**, tudo saia na identidade do In The Loop.

**Fixo, e você defende** (a identidade):
- fundo `#160307`, crimson, âmbar só nas barras; Helvetica Neue + DM Mono; glows da marca (Shape,
  anéis, ∞) só pelos componentes; masthead "IN THE LOOP · ano · Volund" e paginação;
- os componentes `itl-*` e a grade (12 colunas, margem 100): a gramática é `itl-area` → cabeçalho
  (kicker + título) → corpo;
- um ponto focal por slide (um número ou uma ideia em destaque), texto curto que cabe no container;
- movimento com começo, meio e fim, nunca tremor; notas do apresentador em todo slide; nunca inventar dado.

**Livre, e vem da edição** (a estrutura):
- quais blocos existem, quantos, em que ordem, com que nomes e quem apresenta;
- quantos slides cada bloco tem, quais assuntos entram, qual composição usar;
- o formato da edição (mais curto, blocos intercalados, tema em vez de área). A identidade continua a mesma.

Os decks de edições passadas são **referência de composição visual**, não de conteúdo. Não proponha
nem pergunte assuntos de edições anteriores.

## Conversa inicial

Antes de tudo, faça a **conversa inicial** (`entrevista-inicial.md`): poucas perguntas, numa
mensagem só, para entender **quem está falando**, **qual bloco vai preencher**, **como traz o
conteúdo** e o que quer contar. Ela não define estrutura. Pergunte só o que ainda não estiver claro.

## Dois perfis

- **Apresentador / gestor** ("minha parte"): traz o material do seu bloco. Você propõe os slides,
  compõe a parte e entrega verificada no canal do Slack. Não exige conhecimento de design. Skills:
  `itl-slides` ("Parte do apresentador") e `itl-entrega`.
- **Designer** ("montagem"): lê as partes no canal, revisa, monta o deck final, dá o acabamento
  (retratos, imagens finais), pede telas ao Figma e entrega o final no canal. Skills: `itl-montagem`
  e `itl-entrega`.

## Como montar o roteiro de uma parte

1. Pergunte de forma **aberta**: "O que você quer apresentar neste trimestre?". Sem lista de slides
   nem assuntos prontos; se der exemplo, diga que é de edições passadas.
2. Leia o material (texto, planilha, prints, fotos) e **derive os slides dele**: um assunto = um ou
   mais slides, na ordem em que o apresentador contaria.
3. Proponha a lista (título e composição de cada slide) e espere o ok. Um bloco pode ter 2 slides ou 15.
4. A abertura do bloco (`itl-abertura`: nome do bloco gigante + quem apresenta) entra se o
   apresentador ou o designer quiserem; é o que aparece na agenda.
5. Dado que não veio: `PENDENTE:` nas notas. Nunca preencha com o que foi apresentado antes.
6. Terminada a parte, entregue pela skill `itl-entrega`.

## Escrita

- Português direto, frases curtas, sem jargão de consultoria. **Título é afirmação, não rótulo**:
  "Entregamos 3 vezes mais rápido" > "Velocidade". O kicker (mono crimson, acima) é o rótulo.
- Curto é melhor: a tipografia é monumental e os títulos encolhem para caber; um título longo sai
  pequeno. O `itl.py verificar` avisa quando passa do limite.
- Destaque em crimson (`<em>`) em 1 ou 2 palavras-chave por frase, não em frases inteiras.
- Corrija o texto do apresentador sem mudar o sentido. Sem ponto final em título, kicker e legenda.
- **Nunca invente dado, nome, cargo, cliente, data ou citação.** Faltou: pergunte. Não dá para saber
  agora: `PENDENTE: …` nas notas (e listado na entrega). Nada de lorem ipsum.
- Citação de pessoa só se for real, com autor real. Frase da própria área pode ir sem autor.
- Dado sensível (salário, dado pessoal, contrato confidencial) não vai para slide.

## Números

- Sempre há **um** número em destaque por slide; **dinheiro em geral é ele** (receita, contratos,
  valor sob gestão, economia). Em métricas, o principal leva `.destaque`.
- Formato brasileiro: `R$ 2,4 mi`, `12.400`, `92%`. Em destaque, arredonde e deixe o exato nas notas.
- Números lado a lado têm o mesmo tamanho (`itl-metricas` cuida disso).
- Número com contexto: unidade e período na legenda ("pessoas na operação · fev → jul").
- Odômetro (`data-de`) só com inteiro de até 2 dígitos ("de 4 para 19").
- Barras só com percentuais (0–100); meta vai como `.meta`. Confira somas e totais antes de pôr no slide.

## Imagens

- **Abertura de bloco não tem foto.** Retrato recortado na abertura é só do design (ex.: CEO no
  bloco institucional).
- **Retratos do time são feitos pelo design** (padronizados por IA a partir da foto de cada pessoa).
  Peça uma foto de cada integrante (rosto visível, boa luz, sem filtro) e use
  `<div data-pedido="Retrato padronizado de <nome>" data-referencia="img/<foto>"></div>`.
- Prints de produto: telas reais, sem dado pessoal visível, em boa resolução (ideal ≥ 1600 px). Print
  ruim → pedido ao design com o print como referência.
- Não usar imagem de banco genérica. Logos e glows já vêm do motor: **não** peça nem adicione.

## O que fazer quando a identidade não resolve

Se o conteúdo pede algo que os componentes não cobrem, **não invente CSS nem fuja da identidade**.
Componha com o que existe, registre `PARA O DESIGN: …` nas notas e siga. O designer decide se vira
componente novo (fluxo em `itl-montagem`).

## Checklist antes de entregar

1. `itl.py verificar` sem erros; avisos lidos e resolvidos ou justificados.
2. `itl.py gerar` e, no navegador, tecla **V**: "Tudo cabe".
3. Passar slide a slide em tela cheia (F) e na visão geral (G).
4. Números conferidos contra a fonte; o principal de cada slide em destaque.
5. `itl.py pendencias` entregue junto; nenhum `PENDENTE:` esquecido num slide final.
6. PDF de reserva: Cmd/Ctrl+P no navegador, 1 slide por página.
