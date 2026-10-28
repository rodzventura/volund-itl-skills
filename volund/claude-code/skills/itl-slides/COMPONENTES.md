# Componentes do design system In The Loop

Gerado por `itl.py componentes` a partir de `design-system.css` (v1.1.0). Não editar à mão.

## Slide

`<section class="itl">` · `data-limpo` (sem masthead, grade e paginação) · `data-agenda="Nome"`.

Animação genérica: `data-a="sobe"` · `"surge"` · `"linhas"` (título por máscara de linha; `data-linhas="2"` limita as linhas). Números: `data-conta` conta até o valor; `data-de="4"` num `.itl-numero` inteiro de até 2 dígitos vira odômetro.

Modificadores aceitos (sem prefixo): `base`, `branco`, `centro`, `destaque`, `fim`, `g`, `m`, `meio`, `meta`, `rolagem`.

Em `style` só entram as variáveis `--div`, `--foco`, `--n`, `--v`, `--zoom` (número ou token) e propriedades de layout: align-items, align-self, flex, gap, grid-column, grid-row, height, justify-content, justify-self, margin-top, max-width, min-height, order, text-align, width.

Imagem que ainda não existe: `<div data-pedido="o que é preciso" data-referencia="img/foto-enviada.jpg"></div>`.

## Componentes

- slide · <section class="itl">. data-limpo = sem masthead, grade e paginação (capa, abertura, prêmio, polos). data-agenda="Nome" marca o slide que abre um bloco na agenda.
- masthead, grade e paginação · gerados pelo motor em todo slide sem data-limpo
- itl-area · a caixa de conteúdo do slide (margem 100, topo 190, acima da paginação). Todo texto mora aqui dentro ou num componente de tela cheia. .centro · .base (conteúdo no pé)
- itl-corpo · ocupa o espaço que sobra abaixo do cabeçalho. .base alinha o conteúdo no pé; .centro no meio
- itl-colunas · duas colunas (--div = largura da 1ª, padrão 1fr) com .itl-col dentro. .fim alinha a coluna à direita; .base empurra para o pé
- itl-grid-2/3/4 · colunas iguais
- itl-cab · cabeçalho: kicker + título (+ subtítulo)
- itl-kicker · rótulo em DM Mono crimson, caixa-alta, acima do título
- itl-titulo · título do slide (96px). .g = editorial 150 (até 2 linhas) · .m = 64 · data-linhas="N" limita as linhas (o motor encolhe até caber)
- itl-gigante · título monumental de uma linha (236px), encolhe sozinho para caber na largura
- itl-palavra · palavra gigante de produto (320px), uma linha, encolhe para caber; o slide com palavra começa mais alto (topo 96)
- itl-sub · subtítulo (44px, cinza) · itl-texto · corpo (26px) · itl-cap · legenda mono caixa-alta (20px)
- itl-filete · linha de 1px que se desenha da esquerda
- itl-numero · número em DM Mono crimson; encolhe para caber na largura do container. Tamanho por --n (padrão 240px). Com data-conta conta até o valor; com data-de="4" e valor inteiro de até 2 dígitos vira odômetro
- itl-apoio · lista curta de números de apoio com filetes (número mono + frase)
- itl-metricas · 2 a 4 .itl-metrica lado a lado, todas do mesmo tamanho; uma .itl-metrica.destaque vira o número principal (grande, crimson, primeira coluna larga) e as outras ficam brancas
- itl-barras · barras horizontais em percentual: .itl-barra com --v (0–100), rótulo, <small> detalhe e <b> valor. .meta = linha de meta tracejada
- itl-topicos · 2 a 4 tópicos editoriais lado a lado (.itl-topico com h3 e p); o motor numera 01, 02… e desenha os filetes
- itl-lista · lista numerada com fios (3 a 6 itens)
- itl-fluxo · etapas ligadas por uma linha que um pacote de luz percorre (3 a 5 <li> com <small> quando, <b> nome, <span> descrição)
- itl-numeros · fileira de números de resultado abaixo de um fluxo (mesmas colunas): <div class="itl-numeros"><div><b data-conta>411</b><span>legenda</span></div>…</div>
- itl-citacao · frase centralizada com o ∞ luminoso atrás (tela cheia). <blockquote class="itl-citacao"><p class="itl-kicker">…</p><p class="itl-frase">…</p><cite>Autor · cargo</cite></blockquote>
- itl-tiras · o time em tiras verticais (2 a 6 .itl-pessoa: foto + <b> nome, <span> papel, <small> detalhe). A foto entra em P&B e ganha cor
- itl-captura · moldura de tela de produto que entra em perspectiva 3D. Altura por height (padrão: a da imagem)
- itl-captura.rolagem · tela de produto mais alta que a moldura, que rola sozinha de cima para baixo, do início ao fim, dentro da moldura. Exige height na captura; a imagem ocupa a largura da moldura e a rolagem acompanha a altura real dela. Sem animação (PDF, ?estatico) mostra o topo
- itl-imagens · 1 a 3 .itl-figura lado a lado (imagem inteira, sem corte, com legenda opcional em <figcaption>)
- itl-lateral · imagem sangrada na metade direita do slide; a itl-area encolhe para a esquerda
- pedido de imagem · <div data-pedido="o que é preciso" data-referencia="img/foto-enviada.jpg"></div> no lugar de uma imagem que o design vai produzir
- itl-capa · capa do evento: logo In the loop, Shape e Volund vêm do motor; o conteúdo é o bloco de tópicos <ul class="itl-capa"><li>Balanço trimestral</li><li><b>Q3</b> · Outubro · 2026</li><li>Recife — São Paulo</li></ul>
- itl-abertura · abertura de bloco: <div class="itl-abertura"><h1 class="itl-gigante">Squad Alfa</h1><p class="itl-sub">linha de apoio</p><p class="itl-quem"><b>Nome</b><span>Cargo</span></p></div>. O número do bloco (01, 02…) é contado pelo motor. Retrato recortado (só design): <img class="itl-retrato">
- itl-fecho · frase de encerramento de bloco em tipografia gigante (2 linhas) + legenda; o glow vem do motor
- itl-agenda · agenda do dia: <ol class="itl-agenda" data-atual="1"><li><b>Bloco</b><span>quem apresenta</span></li>…</ol>. Sem contagem de slides. data-atual acende um item e apaga os outros
- itl-polos · tela dividida com duas cidades: <div class="itl-polos"><figure class="itl-polo"><img src style="--foco:50% 0%;--zoom:1.5"><figcaption><b>Recife</b><span>Pernambuco</span></figcaption></figure>…</div>
- itl-premio · abertura de premiação: <h1 class="itl-premio">Nome do Prêmio</h1>. Traço de luz, anéis que colidem, clarão e letras vêm do motor. Sem tremor
- itl-vencedor · revelação de quem venceu: <div class="itl-vencedor" data-premio="Nome do Prêmio"><b>Nome</b><img src="retrato.png"><b>Sobrenome</b></div>. Nome atrás da foto, sobrenome crimson na frente, o prêmio vazado ao fundo; a foto sobe escura e ganha cor
