---
description: Monta o deck final do In The Loop (Volund) a partir das partes dos apresentadores (perfil designer)
model: opus
argument-hint: "[edição, ex.: Q4 · Janeiro 2027]"
---

Você vai **montar o deck final** do **In The Loop** com o designer. Leia antes as skills `itl-marca`, `itl-slides` e `itl-montagem` (fluxo completo, retratos, regras do Figma e proposta de componente).

Edição: $ARGUMENTS

1. **Conversa inicial** (`itl-marca/entrevista-inicial.md`) e **leia as partes no canal do Slack** (skill `itl-entrega`; versão mais alta de cada bloco). A ordem dos blocos é do designer; nada vem de edições anteriores.
2. **Revise cada parte:** `itl.py verificar`, tecla V na prévia e o checklist de `itl-marca`. Parecer por parte (pronta · acabamento do design · volta para o apresentador) e inconsistências entre partes.
3. **Monte:** `itl.py montar parte-1.itl.html parte-2.itl.html … -o deck.itl.html --trimestre <Q#> --mes <mês> --ano <ano>`, depois `itl.py gerar deck.itl.html -o ITL-<ano>-<Q#>-final-v1.html`.
4. **Acabamento no arquivo-fonte** (`deck.itl.html`, nunca no HTML gerado): retratos padronizados no lugar dos pedidos (`itl.py pendencias`), imagens finais, enquadramento. Para telas no Figma, siga as regras de segurança de `itl-montagem` (página de trabalho `In The Loop · <AAAA-MM>`, só estilos do arquivo, nunca editar as páginas existentes).
5. **Componente novo** só por proposta (`itl-montagem/propostas/_modelo.md`), nunca CSS solto.
6. **Entregue** no canal (skill `itl-entrega`, depois de confirmar) o HTML final, o fonte com `img/` e o relatório.
