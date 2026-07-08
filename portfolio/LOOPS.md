# 🔁 Loops autónomos

> Definido con Gustavo el 2026-07-05.

## 💰 Tracking de tokens — AUTOMÁTICO por sesión (decidido 2026-07-06)

**Decisión de Gustavo (2026-07-06):** costos automáticos, sin reporte manual.
La captura ya funciona; el nudo era el transporte, y se resuelve **haciendo que
el CSV viaje en el commit de cierre que los chats de dev ya pushean** (el del
HANDOFF). Cero deploys extra, cero push por consulta.

### Cómo funciona (las 3 piezas)
1. **Captura (ya viva en main):** el hook `Stop` `log-tokens.py` lee el
   transcript tras cada respuesta, suma tokens de entrada (input + cache
   creation + cache read) y salida, y reescribe **una fila acumulativa por
   sesión** en `docs/metricas/tokens.csv`. Es un archivo diminuto (≈KB) — la
   memoria NUNCA fue el problema.
2. **Transporte (la pieza que faltaba):** el chat de dev, al cerrar la sesión,
   incluye `docs/metricas/tokens.csv` en el **mismo commit** con que ya sube el
   HANDOFF. Como ese push ya ocurría, **no añade ningún deploy nuevo**.
   → Regla para los chats de dev, ver más abajo.
3. **Horneado (lado del loop, este chat):** cada mañana el loop lee el CSV de
   cada repo y llena el array `COSTOS` del dashboard.

### Procedimiento del loop para llenar `COSTOS`
El hook está instalado en los **5 repos** (incluida esta torre). Ojo con la RAMA de donde se lee el CSV:
- **Kiwiano** y **fitmark** (dev activo en otros chats → van a main):
  `git show origin/main:docs/metricas/tokens.csv`
- **Padel (Easy Courts)** y **La-Suiza (Navaja Suiza)** (en pausa, se trabajan en su
  rama): `git show origin/claude/project-portfolio-tracking-ib0574:docs/metricas/tokens.csv`
- **Claudio-skills (esta torre)**: `docs/metricas/tokens.csv` en su rama de trabajo.
  Es el consumo de la COORDINACIÓN, no un proyecto del panel COSTOS (que tiene 4 filas) —
  sirve para saber cuánto gasta el propio loop; reportarlo aparte si algún día se quiere.

Si el archivo no existe todavía → aún no hubo cierre con el CSV → dejar el proyecto en `null`.
- **sesiones** = nº de filas (cada fila es una sesión distinta).
- **tin** = suma de `tokens_entrada_acum`; **tout** = suma de `tokens_salida_acum`.
- Cargar `{ sesiones, tin, tout }` en la entrada del proyecto en `COSTOS`
  (dashboard.html). El USD lo calcula solo el JS a tarifa Opus 4.8 ($5/$25 por M).
- Sin CSV → dejar `null`: el panel muestra "ESPERANDO 1ER CIERRE"; con datos, "AUTO ✓".

### ⚠️ Regla para los chats de dev de Kiwiano y fitmark (pegar en su rutina de cierre)
> Al cerrar la sesión, además de commitear/pushear el HANDOFF, incluí el CSV de
> tokens en el mismo commit:
> ```
> git add docs/HANDOFF.md docs/metricas/tokens.csv
> git commit -m "docs: HANDOFF + métricas de tokens de la sesión"
> git push
> ```
> (Kiwiano tiene el HANDOFF en `docs/HANDOFF.md`; fitmark en `HANDOFF.md` raíz —
> ajustar la ruta, el CSV siempre es `docs/metricas/tokens.csv`.)
> Best-effort: si la sesión muere sin cerrar, esa sesión no reporta. Es aceptable.

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

4. **Tokens automáticos**: hook `Stop` en Kiwiano y fitmark
   (`.claude/hooks/log-tokens.py`) — **ya en main de ambos** — tras cada
   respuesta suma los tokens y actualiza `docs/metricas/tokens.csv` (una fila
   acumulativa por sesión). El loop lo lee desde origin y hornea el panel de
   costos. El único requisito humano es que el chat de dev incluya el CSV en su
   commit de cierre (ver la sección "Tracking de tokens" arriba).

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

## Dashboard como PWA instalable (📱 acceso directo en el teléfono)

El dashboard vive en dos formas desde la misma fuente `dashboard.html`:
1. **Artifact de Claude** (para revisión rápida): se publica con la tool Artifact.
2. **PWA propia en `portfolio/dashboard/`** (para instalar en el teléfono como
   Kiwiano): `index.html` (documento completo con `<head>` de PWA) + `manifest.webmanifest`
   + `icon-180.png`/`icon-512.png` (torre de control en la paleta del HUD).

**Regla del loop**: después de copiar el `dashboard.html` nuevo al repo, correr
`python3 portfolio/dashboard/build-pwa.py` — regenera `index.html` envolviendo el
cuerpo con el `<head>` correcto. Así la app del teléfono se actualiza sola en cada corrida.

**Deploy**: Vercel sirve la carpeta `portfolio/dashboard/` como estática (Root
Directory = `portfolio/dashboard`, Production Branch = `claude/project-portfolio-tracking-ib0574`).
El icono se regenera desde `scratchpad/icon.html` con Playwright si hay que rediseñarlo.

## Obsidian (memoria compacta entre sesiones)

- `docs/obsidian/portfolio/context.md` = estado actual en ≤200 líneas. Toda
  sesión (incluido el loop) lo lee PRIMERO — ahorra tokens al no re-auditar.
- El loop lo sobreescribe al cerrar cada corrida y añade la nota del día en
  `docs/obsidian/portfolio/sessions/`.
- Gustavo lo ve en su vault haciendo `git pull` del repo Claudio-skills en su
  PC (convención de su skill `obsidian-context`).

## Gestión

- Pausar: pedir "pausa el loop diario" (deshabilita el trigger sin borrarlo).
- Cambiar hora/frecuencia: pedir el cambio con la nueva hora (se guarda en UTC).
- El loop registra cada corrida como una fila en `metricas/sesiones.csv`
  (proyecto = `loop-diario`).
