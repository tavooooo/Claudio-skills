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

## Gestión

- Pausar: pedir "pausa el loop diario" (deshabilita el trigger sin borrarlo).
- Cambiar hora/frecuencia: pedir el cambio con la nueva hora (se guarda en UTC).
- El loop registra cada corrida como una fila en `metricas/sesiones.csv`
  (proyecto = `loop-diario`).
