# Volund · skills do In The Loop

Skills e agentes que montam a apresentação do **In The Loop**, o evento trimestral da Volund, sempre
na identidade do evento: design system fixo (componentes `itl-*`), composição livre, arquivo único
animado com PDF de reserva.

- Projeto, fluxo e agentes: [`volund/in-the-loop/README.md`](volund/in-the-loop/README.md)
- Skills: [`volund/claude-code/skills/`](volund/claude-code/skills/) (`itl-marca`, `itl-slides`, `itl-entrega`, `itl-montagem`)
- Tokens da marca: [`volund/volund-brand/volund-tokens.json`](volund/volund-brand/volund-tokens.json)

## Importar na plataforma de agentes

Uma importação por skill: repositório `rodzventura/volund-itl-skills`, pasta
`volund/claude-code/skills/<skill>`. Cada skill é autocontida (fontes, glows e logos ficam dentro de
`itl-slides`).

## Usar no Claude Code

```bash
git clone https://github.com/rodzventura/volund-itl-skills.git ~/volund-itl-skills
ln -s ~/volund-itl-skills/volund/claude-code/skills/itl-* ~/.claude/skills/
ln -s ~/volund-itl-skills/volund/claude-code/commands/itl-*.md ~/.claude/commands/
```

Comandos: `/itl-parte` (apresentador) e `/itl-montar` (designer). Ferramenta:
`python3 volund/claude-code/skills/itl-slides/scripts/itl.py` (Python 3 + Pillow).

Os exemplos usam **dados fictícios**. Canal de entrega, arquivo do Figma e qualquer dado real ficam
na configuração dos agentes na plataforma, nunca neste repositório.
