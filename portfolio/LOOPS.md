# 🔁 Loops autónomos

> Definido con Gustavo el 2026-07-05.

## Loop diario — torre de control

- **Trigger**: `trig_01TFHhGouJWbbPKjoS9JQz1H` · cron `0 20 * * *` (20:00 UTC = 08:00 NZST)
- **Dispara en**: la sesión torre de control (este chat de Claudio-skills)
- **Alcance aprobado por Gustavo** (los 3 niveles):
  1. **Revisar y avisar**: fetch de los 5 repos, detectar commits/ramas nuevas,
     actualizar dashboard + `sesiones.csv`, regenerar el artifact visual si cambió algo.
  2. **Coordinación**: tareas chicas en `portfolio/` (fichas, fechas, ideas).
  3. **Avance autónomo en proyectos EN PAUSA**: Easy Courts (`/home/user/Padel`) y
     Navaja Suiza (`/home/user/La-Suiza`), avances pequeños y testeados según sus
     roadmaps, en la rama `claude/project-portfolio-tracking-ib0574`.
- **Regla dura**: NUNCA tocar código de Kiwiano ni fitmark — se desarrollan en
  otros chats en paralelo; tocarlos generaría conflictos.
- **Notificación**: push al teléfono solo si hay algo urgente (deadline vencido o
  a ≤3 días, riesgo nuevo); siempre queda el resumen escrito en el chat.

## Fuentes de datos (en este orden)

Cómo el loop determina "en qué va" cada proyecto:

1. **Git = verdad dura** (`git fetch` + `git log` de main y ramas): qué se
   commiteó realmente, cuándo, y qué ramas divergen. Los commits no mienten.
2. **HANDOFF.md = verdad narrativa**: `Kiwiano/docs/HANDOFF.md` y
   `fitmark/HANDOFF.md` son los documentos que Gustavo y sus otros chats
   mantienen al día (estado, decisiones, pendientes, convenciones). El loop los
   lee SIEMPRE y son la fuente principal para "fase, avance y próximo paso".
3. **Roadmaps**: `docs/ROADMAP_PREMIUM.md` (Kiwiano), `ROADMAP.md` (Padel),
   specs de La-Suiza — para contrastar plan vs realidad.

Si HANDOFF y git se contradicen (ej: HANDOFF dice "hecho" pero no hay commit),
el loop lo marca como inconsistencia en el resumen — no adivina.

**Acuerdo con Gustavo (2026-07-05)**: los chats de desarrollo actualizan el
HANDOFF al final de cada sesión y lo commitean/pushean — así el loop de la
mañana siguiente lo ve. Formato sugerido al inicio de cada HANDOFF para
lectura directa del dashboard:

```markdown
## Torre de control
- Fase: F4 (70%) · Próximo hito: <hito> · Fecha objetivo: <yyyy-mm-dd>
- Bloqueadores: <lista corta o "ninguno">
- Última sesión: <yyyy-mm-dd> · <qué se hizo en una línea>
```

## Gestión

- Pausar: pedir "pausa el loop diario" (deshabilita el trigger sin borrarlo).
- Cambiar hora/frecuencia: pedir el cambio con la nueva hora (se guarda en UTC).
- El loop registra cada corrida como una fila en `metricas/sesiones.csv`
  (proyecto = `loop-diario`).
