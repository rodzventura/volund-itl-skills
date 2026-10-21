---
description: Monta a parte de um apresentador do In The Loop (Volund), na identidade do evento
model: opus
argument-hint: "[bloco e edição, ex.: Squad Alfa · Q4 2026]"
---

Você vai montar **a parte de um apresentador** do **In The Loop**, o evento trimestral da Volund. Leia antes as skills `itl-marca` (você é guardião da identidade; a estrutura é livre) e `itl-slides` (formato, design system, `composicoes.md`, seção "Parte do apresentador").

Pedido: $ARGUMENTS

1. **Conversa inicial** (`itl-marca/entrevista-inicial.md`): quem é a pessoa, qual bloco vai preencher, como traz o conteúdo. Pergunte só o que faltar, numa mensagem curta.
2. **Pergunte de forma aberta** o que a pessoa quer apresentar neste trimestre e peça o material (textos, planilhas, prints e uma foto de cada pessoa do time). A estrutura de slides **não é fixa**: não liste assuntos de edições passadas.
3. **Derive os slides do material** e proponha a lista (título e composição de cada slide). Espere o ok.
4. **Componha** `parte.itl.html` com o cabeçalho `itl:parte`, só com classes `itl-*`, `data-agenda` na abertura do bloco, notas em todos. Imagens em `img/`. Nunca invente dado: `PENDENTE:` e `data-pedido` (retratos do time sempre como pedido, com a foto em `data-referencia`).
5. **Verifique e gere:** `python3 <skill itl-slides>/scripts/itl.py verificar parte.itl.html` e `… gerar parte.itl.html -o parte.html`. Abra o HTML, tecla V até dar "Tudo cabe", passe pelos slides.
6. **Entregue** pela skill `itl-entrega`: `itl.py pacote` e envio ao canal do Slack, depois de confirmar com a pessoa.
