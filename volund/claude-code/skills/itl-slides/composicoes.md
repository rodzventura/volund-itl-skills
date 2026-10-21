# Composições de referência

Exemplos prontos, com dados **fictícios**, de cada composição do In The Loop. Copie o trecho, troque
o conteúdo pelo do apresentador e ajuste. Não são limites: componha outras quando o conteúdo pedir,
sempre com as mesmas peças. Todo slide termina com `<aside class="itl-notas">…</aside>`.

## Abertura de bloco (sem foto)

```html
<section class="itl" data-limpo data-agenda="Squad Alfa">
  <div class="itl-abertura">
    <h1 class="itl-gigante">Squad Alfa</h1>
    <p class="itl-sub">Seis pessoas, dois produtos em produção</p>
    <p class="itl-quem"><b>Ana Lima</b><span>Head de Produto</span></p>
  </div>
  <aside class="itl-notas">Abrir com o contexto do squad.</aside>
</section>
```
O número do bloco (01, 02…) é contado pelo motor. Retrato recortado é só do design:
`<img class="itl-retrato" src="img/retrato.png" alt="…">` dentro da `itl-abertura` (a linha de apoio some).

## Número em destaque (odômetro)

```html
<section class="itl">
  <div class="itl-area">
    <div class="itl-colunas" style="--div:700px">
      <div class="itl-col">
        <div class="itl-cab"><p class="itl-kicker" data-a="surge">Crescimento</p><h2 class="itl-titulo" data-a="linhas" data-linhas="2">De 4 para 12<br>clientes ativos</h2></div>
        <p class="itl-texto" data-a="sobe" style="max-width:620px">Em fevereiro eram quatro clientes. Oito meses depois, triplicou sem aumentar o time.</p>
        <ul class="itl-apoio" style="margin-top:auto">
          <li><b data-conta>8</b><span>contratos novos no trimestre</span></li>
          <li><b data-conta>0</b><span>cancelamentos</span></li>
        </ul>
      </div>
      <div class="itl-col fim">
        <div class="itl-numero" data-de="4" style="--n:640px;margin-top:-40px">12</div>
        <p class="itl-cap" data-a="surge">clientes ativos · fev → set</p>
      </div>
    </div>
  </div>
  <aside class="itl-notas">…</aside>
</section>
```
Número que não é inteiro de até 2 dígitos (`R$ 2,4 mi`, `1.280`): troque `data-de="4"` por `data-conta`.

## Métricas (um destaque + dois de apoio)

```html
<div class="itl-area">
  <div class="itl-colunas" style="--div:1100px;flex:none">
    <div class="itl-cab"><p class="itl-kicker" data-a="surge">Resultados do trimestre</p><h2 class="itl-titulo" data-a="linhas" data-linhas="2">Números de produção, não estimativa</h2></div>
    <p class="itl-texto" data-a="sobe" style="margin-top:20px">Os dois produtos rodam na mesma esteira e com o mesmo time enxuto.</p>
  </div>
  <div class="itl-corpo base">
    <div class="itl-metricas">
      <div class="itl-metrica destaque"><div class="itl-numero" data-conta>R$ 2,4 mi</div><p>em contratos sob gestão no Produto Alfa</p></div>
      <div class="itl-metrica"><div class="itl-numero" data-conta>6</div><p>pessoas no squad</p></div>
      <div class="itl-metrica"><div class="itl-numero" data-conta>2</div><p>produtos em produção</p></div>
    </div>
  </div>
</div>
```

## Comparativo (quatro números do mesmo peso)

```html
<div class="itl-corpo base">
  <div class="itl-metricas">
    <div class="itl-metrica"><p class="itl-cap">Antes</p><div class="itl-numero" data-conta>12 dias</div><p>para fechar o mês</p></div>
    <div class="itl-metrica"><p class="itl-cap">Agora</p><div class="itl-numero" data-conta>3 dias</div><p>para fechar o mês</p></div>
    <div class="itl-metrica"><p class="itl-cap">Antes</p><div class="itl-numero" data-conta>60%</div><p>de chamados no dia</p></div>
    <div class="itl-metrica"><p class="itl-cap">Agora</p><div class="itl-numero" data-conta>92%</div><p>de chamados no dia</p></div>
  </div>
</div>
```

## Barras com meta

```html
<div class="itl-area">
  <div class="itl-cab"><p class="itl-kicker" data-a="surge">Produto Alfa</p><h2 class="itl-titulo" data-a="linhas" data-linhas="1">O número que eu mais acompanho</h2><p class="itl-cap" data-a="surge">Fechamento mensal no prazo</p></div>
  <div class="itl-corpo base">
    <div class="itl-barras">
      <div class="itl-barra" style="--v:62"><p>Julho</p><b data-conta>62%</b></div>
      <div class="itl-barra" style="--v:78"><p>Agosto</p><b data-conta>78%</b></div>
      <div class="itl-barra" style="--v:91"><p>Setembro<small>parcial</small></p><b data-conta>91%</b></div>
      <div class="itl-barra meta" style="--v:100"><p>Meta do ano<small>até dezembro</small></p><b data-conta>100%</b></div>
    </div>
  </div>
</div>
```

## Tópicos editoriais

```html
<div class="itl-area">
  <div class="itl-colunas" style="--div:1120px;flex:none">
    <div class="itl-cab"><p class="itl-kicker" data-a="surge">Aprendizados</p><h2 class="itl-titulo g" data-a="linhas" data-linhas="2">Crescer sem<br>baixar a barra</h2></div>
    <p class="itl-texto" data-a="sobe" style="margin-top:20px">O que aprendemos ao triplicar a base sem aumentar o time.</p>
  </div>
  <div class="itl-corpo base">
    <div class="itl-topicos">
      <div class="itl-topico"><h3>Automatizar o repetitivo</h3><p>Tudo o que se repete toda semana virou agente.</p></div>
      <div class="itl-topico"><h3>Medir o que importa</h3><p>Um número por produto, acompanhado toda semana.</p></div>
    </div>
  </div>
</div>
```

## Fluxo (processo) e roadmap

```html
<div class="itl-area">
  <div class="itl-cab"><p class="itl-kicker" data-a="surge">Produto Beta · Como funciona</p><h2 class="itl-titulo" data-a="linhas" data-linhas="1">Do chamado à solução</h2></div>
  <div class="itl-corpo" style="gap:56px;margin-top:20px">
    <ol class="itl-fluxo">
      <li><b>Entrada</b><span>Chamado chega por e-mail ou portal</span></li>
      <li><b>Triagem</b><span>Classificado automaticamente</span></li>
      <li><b>Atribuição</b><span>Vai para a pessoa certa</span></li>
      <li><b>Solução</b><span>Resposta com histórico completo</span></li>
    </ol>
    <div class="itl-numeros">
      <div><b data-conta>1.280</b><span>chamados no trimestre</span></div>
      <div><b data-conta>92%</b><span>resolvidos no mesmo dia</span></div>
    </div>
  </div>
</div>
```
Roadmap: `<li><small>Out</small><b>Piloto</b><span>…</span></li>` e, sem `itl-numeros`, `<div class="itl-corpo centro">`.

## Frase (∞ atrás)

```html
<section class="itl">
  <blockquote class="itl-citacao">
    <p class="itl-kicker" data-a="surge">O que ouvimos</p>
    <p class="itl-frase" data-linhas="3">“Pela primeira vez o fechamento saiu <em>antes do prazo</em>.”</p>
    <cite data-a="surge">Cliente fictício · Diretor de operações</cite>
  </blockquote>
  <aside class="itl-notas">…</aside>
</section>
```

## Lista

```html
<div class="itl-area">
  <div class="itl-colunas" style="--div:640px">
    <div class="itl-cab"><p class="itl-kicker" data-a="surge">Próximo trimestre</p><h2 class="itl-titulo" data-a="linhas" data-linhas="3">O que vem pela frente</h2></div>
    <ol class="itl-lista">
      <li>Levar o Produto Alfa para mais dois clientes</li>
      <li>Fechar 100% dos meses dentro do prazo</li>
      <li>Abrir o Produto Beta para clientes externos</li>
    </ol>
  </div>
</div>
```

## Time (retratos pedidos ao design)

```html
<div class="itl-area">
  <div class="itl-cab"><p class="itl-kicker" data-a="surge">O time</p><h2 class="itl-titulo" data-a="linhas" data-linhas="1">Seis pessoas, dois produtos</h2></div>
  <div class="itl-corpo base">
    <div class="itl-tiras">
      <figure class="itl-pessoa"><div data-pedido="Retrato padronizado de Ana Lima" data-referencia="img/ana.jpg"></div><figcaption><b>Ana Lima</b><span>Owner Técnica</span><small>Alfa + Beta</small></figcaption></figure>
      <figure class="itl-pessoa"><div data-pedido="Retrato padronizado de Bruno Melo" data-referencia="img/bruno.jpg"></div><figcaption><b>Bruno Melo</b><span>Product Builder</span><small>Alfa</small></figcaption></figure>
    </div>
  </div>
</div>
```
O design troca cada pedido por `<img src="img/retrato-ana.jpg" alt="Ana Lima">`.

## Produto

```html
<div class="itl-area">
  <h2 class="itl-palavra">Alfa</h2>
  <div class="itl-colunas" style="--div:560px;gap:100px">
    <div class="itl-col">
      <p class="itl-kicker" data-a="surge">Produto</p>
      <p class="itl-texto" data-a="sobe">Plataforma que automatiza o fechamento mensal e aponta só o que precisa de olho humano.</p>
      <div class="itl-captura" style="height:250px;margin-top:auto"><img src="img/site.jpg" alt="Site"></div>
    </div>
    <div class="itl-captura" style="height:520px;align-self:end"><img src="img/painel.png" alt="Painel"></div>
  </div>
</div>
```

## Número + imagem

```html
<div class="itl-area">
  <div class="itl-colunas" style="--div:780px">
    <div class="itl-col">
      <div class="itl-cab"><p class="itl-kicker" data-a="surge">Produto Beta</p><h2 class="itl-titulo" data-a="linhas" data-linhas="2">Chamados resolvidos sem fila</h2></div>
      <div class="itl-numero" data-conta data-a="sobe" style="margin-top:20px">1.280</div>
      <p class="itl-cap" data-a="surge">chamados no trimestre</p>
    </div>
    <div class="itl-captura" style="height:740px;margin-top:10px"><img src="img/painel.png" alt="Painel"></div>
  </div>
</div>
```

## Imagens (1 a 3, inteiras)

```html
<div class="itl-area">
  <div class="itl-cab"><p class="itl-kicker" data-a="surge">Entregas</p><h2 class="itl-titulo" data-a="linhas" data-linhas="1">Do site ao painel</h2></div>
  <div class="itl-imagens">
    <figure class="itl-figura"><img src="img/site.jpg" alt="Site"><figcaption>Site novo</figcaption></figure>
    <figure class="itl-figura"><div data-pedido="Print do painel em alta resolução"></div><figcaption>Painel</figcaption></figure>
  </div>
</div>
```

## Texto + imagem lateral

```html
<section class="itl">
  <div class="itl-lateral"><img src="img/time.jpg" alt="O time" style="--foco:50% 30%"></div>
  <div class="itl-area" style="gap:36px">
    <div class="itl-cab"><p class="itl-kicker" data-a="surge">Bastidores</p><h2 class="itl-titulo" data-a="linhas" data-linhas="3">Um time que nasceu construindo</h2></div>
    <p class="itl-texto" data-a="sobe">O squad começou com quatro pessoas e hoje responde por dois produtos em produção.</p>
    <p class="itl-texto" data-a="sobe"><em>A barra continua no mesmo lugar.</em></p>
  </div>
  <aside class="itl-notas">…</aside>
</section>
```

## Encerramento de bloco

```html
<section class="itl">
  <div class="itl-fecho">
    <h2 class="itl-titulo" data-linhas="2">O próximo trimestre já começou.</h2>
    <p class="itl-cap" data-a="surge">Squad Alfa · Q4 2026</p>
  </div>
  <aside class="itl-notas">…</aside>
</section>
```

## Só design: capa, agenda, polos, prêmio, vencedor

```html
<section class="itl" data-limpo>
  <ul class="itl-capa"><li>Balanço trimestral</li><li><b>Q4</b> · Janeiro · 2027</li><li>Recife — São Paulo</li></ul>
</section>

<section class="itl"><div class="itl-area">
  <p class="itl-kicker" data-a="surge">Agenda do dia</p>
  <ol class="itl-agenda" data-atual="2"><li><b>Institucional</b><span>Nome</span></li><li><b>Squad Alfa</b><span>Nome</span></li></ol>
</div></section>

<section class="itl" data-limpo>
  <div class="itl-polos">
    <figure class="itl-polo"><img src="img/recife.jpg" alt="Recife"><figcaption><b>Recife</b><span>Pernambuco</span></figcaption></figure>
    <figure class="itl-polo"><img src="img/sao-paulo.jpg" alt="São Paulo"><figcaption><b>São Paulo</b><span>São Paulo</span></figcaption></figure>
  </div>
  <div class="itl-area"><p class="itl-kicker" data-a="surge">Nossos polos de hoje</p></div>
</section>

<section class="itl" data-limpo><h1 class="itl-premio">Nome do Prêmio</h1></section>

<section class="itl" data-limpo>
  <div class="itl-vencedor" data-premio="Nome do Prêmio"><b>Nome</b><img src="img/vencedor.png" alt="Nome Sobrenome"><b>Sobrenome</b></div>
</section>
```
Capa e agenda saem prontas do `itl.py montar`. Foto com texto embutido nos polos: `style="--foco:50% 0%;--zoom:1.5"`.
Vencedor: retrato recortado em PNG sem fundo; nome e sobrenome curtos (até ~11 letras cada).
