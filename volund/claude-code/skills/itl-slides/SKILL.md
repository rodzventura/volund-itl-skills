---
name: "itl-slides"
description: "Use esta skill para montar, editar ou gerar slides do In The Loop, o evento trimestral da Volund. Traz o formato do deck (.itl.html), o design system (classes itl-*), as composições de referência e a ferramenta itl.py (verificar, gerar, pendências, pacote, montar)."
---

# In The Loop · slides

O deck do In The Loop é um arquivo-fonte `.itl.html` com uma `<section class="itl">` por slide.
**Não existe catálogo fechado de layouts**: cada slide é composto livremente, a partir do conteúdo,
**só com as peças do design system** (`design-system.css`). O `itl.py` verifica as regras e gera um
HTML único, animado, com notas, tela sempre ativa e PDF.

Leia junto: `COMPONENTES.md` (lista gerada das classes), `composicoes.md` (exemplos prontos de cada
composição) e a skill `itl-marca` (papel, roteiro, escrita, números, imagens).

## Fluxo

```bash
ITL=<pasta desta skill>/scripts/itl.py
python3 $ITL verificar parte.itl.html            # regras do design system + avisos de texto longo
python3 $ITL gerar parte.itl.html -o parte.html  # HTML final (roda a verificação antes)
python3 $ITL pendencias parte.itl.html           # PENDENTE:, PARA O DESIGN:, imagens pedidas
python3 $ITL pacote parte.itl.html --versao 1 -o saida/   # apresentador: o que vai para o Slack (skill itl-entrega)
python3 $ITL montar a.itl.html b.itl.html -o deck.itl.html --trimestre Q4 --mes Janeiro --ano 2027   # designer
```

Depois de gerar, **abra o HTML e rode a verificação visual**: tecla **V** (ou `ITL.verificar()` no
console). Ela acusa texto fora do container, fora da `itl-area`, fora do slide e título que não coube
nem no menor tamanho. **Tudo tem de caber**: se acusar, reescreva mais curto ou recomponha.

Teclas do deck: ← → espaço/clique navegam · F tela cheia · G visão geral · N notas · R repete
animação · V verifica. No endereço: `#5` abre o slide 5 · `?estatico` sem animação (revisão) ·
`?reserva` mostra como fica numa máquina sem Helvetica Neue. O ponto no canto inferior esquerdo fica
verde quando a tela está travada acesa (tela sempre ativa).

## Parte do apresentador (perfil "minha parte")

O apresentador traz o material do bloco dele; você devolve **uma parte**, que o designer junta às
outras. Siga a skill `itl-marca` (identidade fixa, estrutura livre, conversa inicial, roteiro).

1. Faça a **conversa inicial** (`itl-marca/entrevista-inicial.md`).
2. Pergunte de forma aberta o que a pessoa quer apresentar; leia o material e proponha a lista de
   slides (título e composição de cada um). Espere o ok.
3. Escreva `parte.itl.html` com o cabeçalho abaixo e as `<section class="itl">`. Se o bloco tiver
   abertura, marque-a com `data-agenda="Nome do bloco"`. Notas em todo slide. Imagens em `img/`, com
   caminho relativo.
4. `verificar`, `gerar -o parte.html`, tecla V no navegador, `pendencias`.
5. Entregue pela skill `itl-entrega` (canal do Slack, com versão).

```html
<!-- itl:parte bloco="Squad Exemplo" apresentador="Nome Sobrenome" cargo="Head de Produto" edicao="2026-Q4" -->
<section class="itl" data-limpo data-agenda="Squad Exemplo">
  <div class="itl-abertura">…</div>
  <aside class="itl-notas">…</aside>
</section>
<section class="itl">
  <div class="itl-area">
    <div class="itl-cab"><p class="itl-kicker" data-a="surge">Rótulo</p><h2 class="itl-titulo" data-a="linhas" data-linhas="2">Título que afirma</h2></div>
    <div class="itl-corpo base">…</div>
  </div>
  <aside class="itl-notas">O que o apresentador fala aqui.</aside>
</section>
```

## Formato

- `<section class="itl">` = um slide. `data-limpo` tira masthead, grade e paginação (capa, abertura,
  polos, prêmio, vencedor). `data-agenda="…"` marca a abertura de um bloco.
- `itl-area` é a caixa de conteúdo (margem 100, topo 190); todo texto mora nela ou num componente de
  tela cheia (`itl-capa`, `itl-abertura`, `itl-citacao`, `itl-polos`, `itl-premio`, `itl-vencedor`, `itl-fecho`).
- Animação: `data-a="sobe"` · `"surge"` · `"linhas"` (título por máscara de linha; `data-linhas="2"`
  é o máximo de linhas, e o motor encolhe a fonte até caber). Os componentes têm coreografia própria.
- Números: `.itl-numero` com `data-conta` conta até o valor (formato brasileiro preservado); com
  `data-de="4"` e valor inteiro de até 2 dígitos vira odômetro. Tamanho por `--n`.
- Destaque em crimson: `<em>` dentro do título ou da frase.
- Imagem: `<img src="img/arquivo.jpg" alt="…">`. Imagem que ainda não existe:
  `<div data-pedido="o que é preciso" data-referencia="img/foto-enviada.jpg"></div>`.
- Notas: `<aside class="itl-notas">` em todo slide. `PENDENTE:` para dado que falta,
  `PARA O DESIGN:` para pedido visual.

## Regras (o `itl.py verificar` reprova)

- Só classes `itl-*` existentes e os modificadores documentados (`g`, `m`, `centro`, `base`, `fim`,
  `meio`, `destaque`, `branco`, `meta`).
- Nada de `<style>`, `<script>`, `font-family`, cor em hex/rgb, imagem externa, lorem ipsum.
- `style` só aceita as variáveis `--n`, `--v`, `--div`, `--foco`, `--zoom` (número ou token) e
  propriedades de **layout** (width, max-width, height, flex, gap, margin-top, align-self, text-align…).
- Texto acima dos limites gera **aviso** (título ~70 caracteres, `.g` 30, abertura 16, palavra de
  produto 12, frase 100, itens de lista 70, agenda 24): encurte em vez de ignorar.

## Composições de referência (não são limites)

Exemplos prontos de cada uma em `composicoes.md`. Use como ponto de partida e crie composições novas
quando o conteúdo pedir, sempre com as mesmas peças.

| Composição | Peças | Quem usa |
|---|---|---|
| Abertura de bloco | `itl-abertura` (`itl-gigante` + `itl-sub` + `itl-quem`) | apresentador |
| Número em destaque | `itl-colunas` com cabeçalho + `itl-texto` + `itl-apoio` / `itl-numero` (odômetro) + `itl-cap` | apresentador |
| Métricas (1 destaque + apoio) | `itl-metricas` com `itl-metrica.destaque` | apresentador |
| Comparativo (4 iguais) | `itl-metricas` com 4 `itl-metrica` e `itl-cap` | apresentador |
| Barras | `itl-barras` + `itl-barra` (`--v`), `.meta` | apresentador |
| Tópicos editoriais | título `.g` + `itl-topicos` (2–4) | apresentador |
| Fluxo / roadmap | `itl-fluxo` (+ `itl-numeros`) | apresentador |
| Frase | `itl-citacao` + `itl-frase` (∞ atrás) | apresentador |
| Lista | `itl-colunas` com cabeçalho + `itl-lista` | apresentador |
| Time | `itl-tiras` + `itl-pessoa` (retratos pedidos ao design) | apresentador |
| Produto | `itl-palavra` + `itl-colunas` com `itl-captura` | apresentador |
| Número + imagem | `itl-colunas` com `itl-numero` / `itl-captura` | apresentador |
| Imagens | `itl-imagens` + `itl-figura` (1–3) | apresentador |
| Texto + imagem lateral | `itl-lateral` + `itl-area` | apresentador |
| Encerramento de bloco | `itl-fecho` | apresentador |
| Capa · agenda | `itl-capa` · `itl-agenda` (gerados pelo `montar`) | designer |
| Polos | `itl-polos` + `itl-polo` | designer |
| Prêmio · vencedor | `itl-premio` · `itl-vencedor` | designer |

Quando nenhuma peça resolver, **não invente CSS**: componha com o que existe e registre
`PARA O DESIGN: …` nas notas. Componente novo só por proposta (`itl-montagem`).

## Erros comuns

- Título longo em `itl-titulo.g` ou na abertura: sai pequeno. Encurte; use `itl-titulo` normal.
- Esquecer `data-linhas` num título longo: o motor permite até 3 linhas; peça 1 ou 2 quando o layout pedir.
- Dois números principais no mesmo slide: escolha um para `.destaque`.
- Foto de pessoa colocada direto no time ou na abertura: no time vai como pedido com referência; na
  abertura não vai.
