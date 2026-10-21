---
name: "itl-montagem"
description: "Use esta skill quando quem fala é o designer do In The Loop: receber as partes dos apresentadores no Slack, revisar, montar o deck final, dar o acabamento no arquivo-fonte (retratos padronizados, imagens finais, enquadramento), pedir telas ao Figma via MCP e propor componentes novos ao design system sem sair da identidade."
---

# In The Loop · montagem (perfil designer)

Você apoia o designer que fecha a apresentação do In The Loop. Valem as regras de `itl-marca`
(guardião da identidade; estrutura livre) e a ferramenta de `itl-slides`. Aqui está o que é
específico do designer.

## 1. Receber e revisar as partes

Faça antes a **conversa inicial** (`itl-marca/entrevista-inicial.md`). As partes chegam **pelo
canal do Slack** (skill `itl-entrega`): use a **versão mais alta** de cada bloco e descompacte o zip.
Para cada parte:

1. `itl.py verificar parte.itl.html`. Erros voltam ao apresentador com a lista exata do que mudar;
   avisos de texto longo você resolve ou devolve.
2. Abra a prévia `.html` e rode a tecla **V**.
3. Revise com o checklist de `itl-marca` e procure **inconsistências entre partes**: o mesmo número
   com formatos diferentes, o mesmo produto com nomes diferentes, períodos diferentes, densidade muito
   diferente entre blocos, tom de escrita destoando.
4. Parecer por parte: **pronta** (✅) · **acabamento do design** · **volta para o apresentador** (🔁,
   com a lista numerada do que pedir, escrita na thread da entrega). Peça confirmação ao designer
   antes de reagir ou escrever no canal. Não corrija o conteúdo do apresentador por conta própria:
   dado, nome e número são dele.

## 2. Montar o deck final

A ordem dos blocos é **do designer**: proponha pela ordem de entrega e ajuste ao que ele pedir.

```bash
python3 $ITL montar parte-1.itl.html parte-2.itl.html parte-3.itl.html -o deck.itl.html --trimestre Q4 --mes Janeiro --ano 2027
# opções: --sem-capa  --sem-agenda  --linha1 "Balanço trimestral"  --polos "Recife — São Paulo"
python3 $ITL gerar deck.itl.html -o ITL-2027-Q4-final-v1.html
```

O `montar` gera a capa e a agenda (nome do bloco + quem apresenta, até 8 blocos, sem contagem de
slides), acerta o caminho das imagens e o motor numera as aberturas (01, 02…). Momentos de
cerimonial (polos, intervalos, premiações) entram como uma parte do próprio design (`composicoes.md`,
"Só design"). Para repetir a agenda entre blocos, copie o slide e marque `data-atual`.

## 3. Acabamento: sempre no arquivo-fonte

Edite `deck.itl.html`, **nunca o HTML gerado** (ele é refeito a cada `gerar`). Pedidos típicos:

- **Retratos do time:** `itl.py pendencias deck.itl.html` lista os pedidos com a foto de referência
  (que vem em `img/` dentro do zip da parte). O design gera os retratos padronizados (mesmo
  enquadramento, luz e fundo) e você troca cada `<div data-pedido=…>` por `<img src="img/…" alt="…">`.
- trocar outros pedidos de imagem pelas finais (prints em alta, fotos de evento);
- enquadrar uma foto: `style="--foco:50% 20%"` (e `--zoom:1.2` nos polos);
- retrato recortado na abertura institucional: `<img class="itl-retrato">` (só design);
- reordenar slides, dividir ou juntar, trocar a composição.

Depois de cada rodada: `verificar`, `gerar` e tecla **V**. Mostre o que mudou.

## 4. Figma (via MCP)

O arquivo **Volund | In The Loop** é a fonte da identidade (`figma-estilos.md`; o fileKey vem nas
instruções do agente). Antes de qualquer escrita, carregue a skill `figma-use` do plugin do Figma.

**Regras de segurança (valem sempre):**
- **Nunca edite as páginas existentes** do arquivo. Elas são a referência.
- **Escreva só numa página de trabalho nova**, `In The Loop · <AAAA-MM>` (crie se não existir).
  Antes de escrever, confirme com o designer o arquivo e a página.
- Use **só os estilos do arquivo** (cores por estilo, não hex; Helvetica Neue e DM Mono). Frames de 1920×1080.

**Do deck para o Figma** ("crie no Figma o slide X"): leia a `<section>`, monte o frame na página de
trabalho com as mesmas peças e devolva o link do frame.

**Do Figma para o deck** ("traga esta tela"): leia o frame (`get_design_context`, `get_screenshot`) e
**recomponha com os componentes `itl-*`**; não copie o CSS gerado pelo Figma. Imagens finais feitas
no Figma (retratos, montagens) entram como arquivo em `img/`.

## 5. Componente novo: proposta, nunca CSS solto

1. Componha com o que existe e registre `PARA O DESIGN: <o que faltou>`.
2. Se o designer quiser resolver, escreva a proposta em `propostas/<nome>.md` seguindo
   `propostas/_modelo.md` (para que serve, onde apareceu, frame do Figma, HTML de uso, CSS só com
   tokens, limites de texto).
3. Aprovada, a proposta vai ao responsável pelo repositório para entrar no `design-system.css`
   (comentário `@componente`, versão nova, `CHANGELOG.md`, `itl.py componentes`). Até lá, a edição
   segue com a composição provisória.
4. Você **não altera o design system** por conta própria nem põe CSS no deck.

## 6. Entrega final e ensaio

- Entregue no canal pela skill `itl-entrega`: `ITL-<ano>-<Q#>-final-vN.html`, o zip do fonte e o relatório.
- No computador do evento: abrir o HTML offline, tela cheia (F), tecla V, conferir o ponto verde de
  tela ativa. Se não for Mac, abrir antes com `?reserva`. Como garantia no Mac, deixe rodando no
  Terminal durante o evento: `caffeinate -d`.
- PDF de reserva: Cmd/Ctrl+P, 1 slide por página, "gráficos de fundo" ligado.
