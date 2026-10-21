# In The Loop · agentes de apresentação

O In The Loop é o evento trimestral da Volund: cada área apresenta os resultados do trimestre e para
onde vai. Dois agentes montam a apresentação, sempre na identidade do evento:

| Agente | Quem usa | Skills | Integrações |
|---|---|---|---|
| **In The Loop · Apresentação** ([texto](agentes/apresentacao.md)) | apresentadores e gestores | `itl-marca`, `itl-slides`, `itl-entrega` | Slack |
| **In The Loop · Montagem** ([texto](agentes/montagem.md)) | time de design | `itl-marca`, `itl-slides`, `itl-montagem`, `itl-entrega` | Slack, Figma (MCP) |

## Como funciona

```
APRESENTADOR + agente Apresentação
  conversa inicial → material → lista de slides (ok) → parte.itl.html → verificar · gerar · V
  "pode enviar" → resumo → confirmação → itl.py pacote → canal do Slack: ITL-2026-Q4-squad-alfa-v1
                                                            (versões seguintes na thread)
DESIGNER + agente Montagem
  lê a última versão de cada bloco → revisa → ✅ aprovado / 🔁 volta (o que corrigir, na thread)
  itl.py montar (capa + agenda) → acabamento no fonte (retratos, imagens, Figma) → final no canal
```

- **Identidade fixa, estrutura livre.** O design system (`itl-slides/design-system.css`, componentes
  `itl-*`) é fixo; cada slide é composto livremente com ele. O `itl.py verificar` reprova o que sai
  da identidade (cor solta, fonte, classe estranha, imagem externa) e a tecla V confere se tudo cabe.
- **Nunca inventar dado.** Faltou: `PENDENTE:` nas notas. Imagem que falta: pedido ao design
  (`data-pedido`, com a foto de referência). Retratos do time são padronizados pelo design.
- **Arquivo único.** O HTML gerado tem fontes, imagens e motor embutidos; abre offline, mantém a
  tela acesa e imprime em PDF (um slide por página).

## Onde está cada coisa

| Caminho | O quê |
|---|---|
| `../claude-code/skills/itl-marca/` | Guardião: papel, conversa inicial, escrita, números, imagens, checklist |
| `../claude-code/skills/itl-slides/` | Design system, motor, `itl.py`, componentes e composições de referência |
| `../claude-code/skills/itl-entrega/` | Entrega e leitura no Slack (nomes, versões, reações, plano B) |
| `../claude-code/skills/itl-montagem/` | Designer: revisão, montagem, acabamento, Figma, propostas de componente |
| `../claude-code/commands/` | `/itl-parte` e `/itl-montar` (Claude Code) |
| `agentes/` | Textos dos dois agentes, prontos para colar na plataforma |
| `exemplos/edicao-exemplo/` | Edição fictícia: 3 partes + cerimonial + deck montado (fontes `.itl.html`; gere o HTML com `itl.py gerar`) |

## Publicar na plataforma

1. Importar cada skill do repositório público `rodzventura/volund-itl-skills`, pasta
   `volund/claude-code/skills/<skill>` (uma importação por skill).
2. Criar os dois agentes com os textos de `agentes/`, preenchendo o canal do Slack e o arquivo do
   Figma nos campos `<COLE AQUI…>` (esses dados não ficam no repositório).
3. Testar com um apresentador de verdade: conversa → parte → envio no canal → revisão → nova versão
   na thread → montagem → final.

Molde e lições: `PLAYBOOK-AGENTE.md` da Difusão Recorrente (repositório `rodzventura/beyond-dr-skills`).
