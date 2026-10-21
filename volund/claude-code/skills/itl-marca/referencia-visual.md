# In The Loop 2026 — sistema visual dos slides

Guia do visual aprovado em outubro de 2026 (direção **"Escala"**: tipografia monumental e cinética,
máscaras de linha, camadas de profundidade). A fonte de verdade é o `itl-slides/design-system.css`
(componentes em `itl-slides/COMPONENTES.md`). Este documento explica o sistema para quem revisa,
compõe e propõe componentes novos.

## Contexto de exibição

TV/LED grande e transmissão online. Por isso: movimento nítido e com começo, meio e fim; nada de
ruído fino nem gradiente grande atrás de texto (vira artefato no stream); contraste alto. Entrega em
**HTML animado** (o evento) + **PDF estático** (backup e envio).

## Tokens (fixos — vêm do Figma `Volund | In The Loop`)

| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#160307` | Fundo de todo slide. Nunca preto puro. |
| `--crimson` | `#EC3E61` | Kicker, números, destaques, linha de progresso, sobrenome do vencedor. |
| `--amber` | `#FC9155` | Só no gradiente das barras (255°, âmbar → crimson) e no clarão do prêmio. |
| `--w50` | `#F5F5F5` | Títulos e texto principal. |
| `--g300` | `#ABABAB` | Texto de apoio, legendas mono. |
| `--g500` / `--g600` | `#7A7A7A` / `#626262` | Itens apagados da agenda; masthead e paginação. |
| `--g800` | `#313131` | Reserva. |

**Tipografia:** Helvetica Neue (títulos e corpo, peso 500 nos títulos) + DM Mono (kicker, rótulos,
números, numerais de seção). Sem Helvetica Neue na máquina, entra a **"ITL Reserva"** (Arimo,
embutida, mesmas medidas) — teste com `?reserva` no endereço. DM Mono é embutida.

**Glows** (imagens, nunca gradiente CSS): `Shape 1` (capa, aberturas, encerramento), `Ellipse 1`
(anéis do prêmio), ∞ luminoso `dex` (citação). São superfícies aprovadas **só nos slides**. No
máximo um glow por slide.

## Grade e estrutura

- Palco fixo **1920×1080**, escalado para a tela.
- **Grade de 12 colunas** com margem de 100 px (linhas verticais quase invisíveis, que se desenham
  na entrada). Conteúdo alinha em `left:100px`; títulos gigantes podem ir a `84px` (compensa o
  recuo óptico).
- **Masthead** "IN THE LOOP · ano · logo Volund" no topo (y=40), **paginação** "07 — 24" no canto
  inferior direito e a grade: o motor põe em todo slide sem `data-limpo` (capa, abertura, polos,
  prêmio e vencedor são limpos).
- Escala tipográfica (fechada): kicker 22 · legenda mono 20 · corpo 26 · subtítulo 44 · título 96
  (`.m` 64, `.g` 150) · frase 100 · abertura 236 · produto 320 · vencedor 300 · números por `--n`
  (até 640 no odômetro).

## Vocabulário de movimento

| Peça | O que faz |
|---|---|
| Máscara de linha (`data-a="linhas"`) | Cada linha de título sobe de trás de uma máscara, em escada. |
| `data-a="sobe"` / `"surge"` | Sobe e aparece / só aparece. O motor escalona os atrasos na ordem de leitura. |
| Filete (`itl-filete`) | Linha de 1 px que se desenha da esquerda. |
| Contagem (`data-conta`) | Número conta do zero preservando o formato brasileiro (`1.280`, `92%`, `R$ 2,4 mi`). |
| Odômetro (`data-de`) | Inteiro de até 2 dígitos rola de `data-de` até o valor. |
| Pacote de luz | Ponto branco com halo crimson percorre o fluxo e acende cada etapa (anel que expande). |
| Perspectiva (`itl-captura`) | Capturas de tela entram inclinadas em 3D e assentam. |
| Tiras do time | Foto entra por cortina, em P&B, e ganha cor. |
| Prêmio | Traço de luz → anéis colidem → clarão com ondas de choque → título letra a letra. **Sem tremor.** |
| Vencedor | Tela entra só com o nome do prêmio vazado deslizando; ~1,3 s depois a foto sobe **quase preta** e ganha cor; nome atrás da foto, sobrenome crimson na frente. |

**Regra de ouro do código:** o CSS padrão de cada elemento é o **estado final** (é o que sai no
PDF). Animação só existe sob `section.itl.run` e parte de `from`. Por isso PDF, "repetir" e `?estatico`
funcionam sem código extra.

## Composição

Não há catálogo fechado: cada slide é composto com os componentes `itl-*` (lista em
`itl-slides/COMPONENTES.md`, exemplos em `itl-slides/composicoes.md`). O que garante a identidade:

- Todo texto mora numa `itl-area` (margem 100, topo 190) ou num componente de tela cheia (capa,
  abertura, citação, polos, prêmio, vencedor, encerramento).
- Cabeçalho = kicker + título. Título é afirmação curta; títulos com `data-a="linhas"` sobem por
  máscara de linha e encolhem até caber no número de linhas pedido.
- Um ponto focal por slide. Números lado a lado do mesmo tamanho; o principal em `.destaque`.
- Cor e fonte nunca no slide: só classes e as variáveis `--n` (tamanho de número), `--v` (barra),
  `--div` (largura da 1ª coluna), `--foco` e `--zoom` (enquadramento de foto).
- Componente novo só por proposta (`itl-montagem/propostas/_modelo.md`), com comentário `@componente`,
  versão nova e entrada no `CHANGELOG.md` quando aprovado.

## Não fazer (testado e rejeitado)

- Número gigante atrás da foto; tremor de tela; glow cortado em linha reta (não escalar imagem de
  glow dentro de caixa com `overflow:hidden` — pulsar só opacidade).
- Texto crimson sobre glow crimson (some).
- Efeito de matriz de pontos/LED; direção "terminal"; retratos P&B fixos; vencedor numa cor só.
- Nome do vencedor encostando no logo In the loop.
- Gradiente grande atrás de texto; ruído/grão fino.
