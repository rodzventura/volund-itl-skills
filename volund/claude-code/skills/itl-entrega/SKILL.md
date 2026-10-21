---
name: "itl-entrega"
description: "Use esta skill para entregar e para ler material do In The Loop no canal de entregas do Slack: nome e versão dos arquivos, confirmação antes de enviar, o que postar (prévia, fonte, pendências), versões novas na thread, reações de status e plano B quando o Slack não responde."
---

# In The Loop · entrega pelo Slack

Tudo do In The Loop trafega por **um canal do Slack**, ligado à plataforma. Não há pastas: o **nome
do arquivo** carrega ano, trimestre, bloco e versão. Esta skill vale para os dois perfis: o
apresentador **entrega a parte** e o designer **lê as partes e entrega o final**.

## O canal

O canal vem das **instruções do agente** (campo "Canal de entrega"). Ele não está no repositório de
propósito: o repositório é público. Se você não tiver o canal, peça ao usuário; **nunca invente nem
poste em canal parecido**.

## Nomes dos arquivos

```
ITL-<ano>-<Q#>-<bloco>-v<N>.html    prévia autocontida da parte (abre com duplo clique)
ITL-<ano>-<Q#>-<bloco>-v<N>.zip     fonte (parte.itl.html) + img/, com as fotos de referência dos pedidos
pendencias-<bloco>-v<N>.md          o que ficou pendente com o apresentador e o que ficou com o design
ITL-<ano>-<Q#>-final-v<N>.html      deck final (designer)
```

`<bloco>` é o nome do bloco em minúsculas, sem acento e com hífen (o `itl.py pacote` usa o mesmo:
"Squad Alfa" → `squad-alfa`). Edição no formato `2026-Q4`.

## Entregar a parte (apresentador)

Só entregue quando a pessoa disser **"pode enviar"** (ou equivalente) e depois de **confirmar o resumo**.
Nunca envie por conta própria ao terminar os slides: ofereça ("Quer que eu envie para o design?").

1. `itl.py verificar`, `gerar` e tecla V; resolva os erros. Avisos e pendências vão no resumo.
2. **Descubra a versão.** Procure no canal a mensagem de entrega desse bloco nesta edição (busque
   `ITL-<ano>-<Q#>-<bloco>`). Não existe: é `v1`, mensagem nova. Existe: a versão nova é a maior + 1,
   postada **na thread** dessa mensagem.
3. `python3 itl.py pacote parte.itl.html --versao N -o saida/` gera a prévia, o zip, as pendências e o
   `entrega.json`.
4. **Mostre o resumo e peça o ok**: bloco, quem apresenta, edição, versão, nº de slides, imagens que
   ficam com o design, pendências com o apresentador e o canal de destino. Só depois envie.
5. **Poste** a prévia `.html`, o `.zip` e o `.md` com a mensagem abaixo (v1 no canal; v2 em diante
   na thread da v1). **Nunca apague nem edite** uma entrega anterior.
6. Responda à pessoa com o link da mensagem e a lista de pendências. Avise que o retorno do design
   chega na thread.

Mensagem de entrega (curta, sempre igual):

> **Squad Alfa · v2** · Ana Lima · 11 slides
> Com o design: 6 retratos do time (fotos de referência no zip), 1 print em alta
> Pendente com o apresentador: confirmar o número do slide 4

## Status pelas reações

O design marca a última versão de cada bloco:
- ✅ **aprovado**: entra no deck.
- 🔁 **volta para ajuste**: o designer escreve na thread **o que corrigir** (lista numerada, por slide).

Quando o apresentador voltar para ajustar (na mesma conversa ou numa nova), leia a thread do bloco,
comece pelo que o design pediu, baixe o `.zip` da última versão, descompacte, continue e entregue a
versão seguinte na mesma thread.

## Ler as partes (designer)

1. No canal, liste as mensagens de entrega da edição (`ITL-<ano>-<Q#>-`). Para cada bloco, use a
   **versão mais alta** (a última da thread) e baixe o `.zip` e o `.md`.
2. Descompacte cada zip numa pasta própria (o fonte `parte.itl.html` já vem com `img/`).
3. Se faltar bloco que o designer esperava, avise; diga sempre qual versão está usando de cada um.

## Entregar o final (designer)

Mesmo cuidado: **resumo, ok, depois envio**. Poste no canal, numa mensagem nova:
- `ITL-<ano>-<Q#>-final-v<N>.html` (o deck autocontido, `itl.py gerar`);
- `ITL-<ano>-<Q#>-final-v<N>.zip` (`deck.itl.html` + `img/`) para continuar editando;
- relatório: slides, blocos e responsáveis, versões das partes usadas, pendências, propostas de
  componente abertas, versão do design system, links dos frames do Figma.

Versões novas do final vão na thread da `final-v1`.

## Regras

- **Só poste no canal de entrega** configurado no agente. Não mande mensagem direta a ninguém sem o
  usuário pedir; não mencione pessoas além de quem o usuário indicar.
- **Nunca apague nem edite** mensagens ou arquivos de entregas anteriores.
- Dado de resultado e fotos de pessoas são **internos**: não copie conteúdo do canal para outros lugares.
- **Plano B:** se o Slack falhar (sem acesso, erro de envio), diga o motivo e **entregue os arquivos
  na própria conversa**; a pessoa posta depois. Nunca diga que enviou se não enviou.
