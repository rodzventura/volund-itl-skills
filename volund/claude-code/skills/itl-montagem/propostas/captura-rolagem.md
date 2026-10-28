# Proposta de componente · captura-rolagem

- **Status:** aprovada pelo designer em 28/out/2026; aplicada no design system v1.1.0 (branch feature/captura-rolagem, aguardando revisão do responsável pelo repositório)
- **Pedido por:** designer · **Edição:** 2026-10

## Para que serve
Mostrar uma tela de produto mais alta que a moldura (formulário longo, página inteira) rolando sozinha de cima para baixo, do início ao fim, sem sair da moldura. O `itl-captura` atual só mostra um recorte fixo (`--foco`) e não tem rolagem.

## Onde apareceu
Slide 9 da parte Squad Li (`PARA O DESIGN` nas notas do slide). Frame do Figma: `Squad Li · 09 · Geolocalização do barramento` (nó 460:40, página "In The Loop · 2026-10"). Moldura de 693 x 907 px; o print (395 x 812 px) tem 1424 px de altura quando ocupa a largura da moldura, então o percurso é de 517 px.

## Uso (HTML só com classes itl-*)
```html
<div class="itl-captura rolagem" style="height:907px;margin-top:-103px"><img src="img/cadastro-geolocalizacao.png" alt="Tela de cadastro do barramento com mapa e localizador"></div>
```
Novo modificador: `rolagem`. Sem ele, o `itl-captura` segue como hoje.

## CSS proposto (só tokens, sem hex, sem font-family)
```css
/* @componente itl-captura.rolagem · tela de produto mais alta que a moldura que rola sozinha de cima para baixo, do início ao fim, dentro da moldura. A imagem ocupa a largura da moldura; a rolagem acompanha a altura real da imagem */
.itl-captura.rolagem img{position:absolute;left:0;top:0;width:100%;height:auto;object-fit:initial}
@keyframes itlRola{from{top:0;transform:translateY(0)}to{top:100%;transform:translateY(-100%)}}
.run .itl-captura.rolagem img{animation:itlRola 6s cubic-bezier(.45,.05,.4,1) 1.2s both}
```
Como funciona: no fim da animação a imagem fica com `top:100%` (altura da moldura) e `translateY(-100%)` (altura da própria imagem), então a base da imagem encosta na base da moldura. Isso vale para qualquer altura de imagem, sem número fixo no CSS. O `.run` mantém a regra do design system: o estado padrão (PDF, `?estatico`) mostra o topo da tela.

- Tempo: a rolagem começa 1,2 s depois do slide abrir (ainda durante a entrada da captura) e dura 6 s, com aceleração e frenagem suaves. Sem pausa nas pontas. Ajustável pelo designer (versão inicial: 14 s com atraso de 2,2 s; reduzida a pedido em 29/out/2026).
- Testada no motor em 28/out/2026 (Squad Li, slide 9): entra, rola até a base e para.

## Limites
- Imagem com largura menor que a moldura sobe de escala e perde nitidez. Ideal: largura >= 1400 px para uma moldura de 693 px a 2x.
- Imagem tem de ser mais alta que a moldura; se for menor, a animação não anda (fica parada no topo).
- Um por slide. Não combinar com `--foco` (ignorado quando há `rolagem`).
- O print do slide 9 hoje tem 395 px de largura e fica suave a 693 px; melhor trocar por um print em alta antes de usar a rolagem.

## Alternativa sem componente novo
Manter o print parado no topo (como está no Figma hoje) ou trocar por `itl-imagens` com a tela inteira, sem corte, e perder o tamanho da moldura. Duas capturas em sequência (topo e base, em dois slides) também resolvem, ao custo de um slide a mais.
