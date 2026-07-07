# Claudio-skills

Repositorio de skills globales para todos los proyectos.

## Convenciones de trabajo

- **Las skills se commitean y pushean directamente a `main`** (instrucción del dueño del repo, 2026-07-07). No usar ramas ni PRs para agregar o editar skills, salvo que el cambio toque algo más que `.claude/skills/`.
- Toda skill nueva o editada sigue el proceso TDD de `writing-skills` (baseline RED con subagente → escribir → GREEN → cerrar loopholes) antes de commitear.
- Las skills se escriben en inglés, con frontmatter `name` + `description` ("Use when..."), en `.claude/skills/<nombre>/SKILL.md`.
- No duplicar contenido entre skills: referenciar con `superpowers:<skill-name>`.
