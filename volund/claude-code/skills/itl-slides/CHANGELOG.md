# Design system In The Loop · versões

## 1.1.0 — 28/out/2026
- Novo modificador `itl-captura.rolagem`: tela de produto mais alta que a moldura rola sozinha de cima
  para baixo, do início ao fim, dentro da moldura (6 s, começando 1,2 s depois do slide abrir, ainda durante a entrada da captura). Estado sem animação (PDF, `?estatico`) mostra o topo. Proposta: `captura-rolagem`
  (primeiro uso: Squad Li, slide 9).
- `itl.py`: `rolagem` entra nos modificadores aceitos.

## 1.0.0 — 21/out/2026
- Migração para o molde da DR: sem catálogo fechado. Tokens fixos + componentes `itl-*`, composição livre.
- Visual "Escala" aprovado em out/2026 (exploração v4) portado inteiro: capa, abertura (título atrás do
  retrato, número do bloco contado pelo motor), odômetro, barras com meta, tópicos, fluxo com pacote de luz,
  citação com ∞, time em tiras, produto, imagens, imagem lateral, agenda, polos, prêmio e vencedor.
- Títulos com máscara de linha que encolhem até caber (`data-a="linhas"`, `data-linhas`); títulos
  gigantes, palavra de produto e números encolhem para caber na largura. Números lado a lado ficam do
  mesmo tamanho; métrica `.destaque` vira o número principal.
- Pedido de imagem ao design com foto de referência (`data-pedido` + `data-referencia`).
- `itl.py`: verificar, gerar, pendencias, pacote (nomes para o Slack), montar, componentes.
- Motor: visão geral (G), notas (N), repetir (R), verificar (V), tela sempre ativa com indicador,
  fonte de reserva embutida (`?reserva`), modo sem animação (`?estatico`), PDF no estado final.
