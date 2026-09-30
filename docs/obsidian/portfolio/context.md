---
project: portfolio
date: 2026-07-05
session: 1
tags: [proyecto/portfolio, torre-de-control, nextjs, supabase]
---

# Portfolio (Torre de Control) — Estado actual

> Este archivo es el CONTEXTO COMPACTO que cualquier sesión de Claude lee
> primero para no re-auditar todo. Máx 200 líneas. Detalle completo en
> `portfolio/` del repo Claudio-skills.

## Quién / objetivo

Gustavo Farías, ing. en computación chileno, working holiday en NZ. Meta:
comercializar sus productos → ingreso pasivo → libertad financiera y jubilar
a su papá. Esta sesión (Claudio-skills) es la **torre de control**: coordina,
NO desarrolla — Kiwiano y FitMark se trabajan en otros chats en paralelo.

## Los 4 proyectos (estado 2026-07-05)

| Proyecto | Estado | Próximo hito | Deadline |
|---|---|---|---|
| **Kiwiano** (torneos pádel multi-club) | ✅ F4 completa (Vitrina mergeada 05-jul, 15 días antes) | F5 Stripe: saldo de pelotas + membresía | **10-ago** |
| **FitMark** (tracker fuerza + coach IA Wallace; nombre por definir) | 85% — funcional punta a punta + QA de 5 auditores (05-jul) | Definir free vs premium | 🎯 lanzamiento gratis **31-ago** |
| **Easy Courts** (repo Padel; arriendo canchas B2B) | Demo mock completa, en pausa | Etapa 1: DB real + auth | 15-dic |
| **Navaja Suiza** (repo La-Suiza; PWA personal) | Completa local, congelada | — | 2027 |

## Decisiones clave tomadas

- **Pipeline**: Kiwiano cobra primero (Stripe F5, beta comercial 15-ago) →
  FitMark lanza gratis 31-ago y monetiza en sep → Easy Courts en nov-dic.
- **Carrera competitiva**: fierro.app es competencia directa de FitMark pero
  está incompleta (librería 404, sin pagos, rutinas flojas — verificado por
  Gustavo 05-jul). Decisión: **salir primero**. Vigilancia semanal.
- **features-review (fitmark)**: solo rescate selectivo de lo útil, luego se
  descarta (415 commits divergentes; NO reconciliación completa).
- **Nombre FitMark**: aparcado (Ferro y Wallace no convencieron; Tensor/
  Fierro/Overload/Gymetric tomados). Deadline dura: 15-ago.
- **Contenido en redes**: parte semana del 06-jul. 1 contenido → 3 plataformas
  (IG principal, TikTok, YT Shorts), 3 pilares: build-in-public, demos del
  producto, tips de entrenamiento. Ver `portfolio/CONTENIDO.md`.

## Sistema montado

- **Docs fuente de verdad**: `portfolio/` en Claudio-skills (PERFIL, PORTFOLIO,
  PIPELINE, CONTENIDO, LOOPS, IDEAS, proyectos/*, metricas/sesiones.csv).
- **Dashboard visual**: artifact "Torre de Control" 🗼 (avance, calendario
  semanal 6 semanas, vigilancia fierro.app, costos). Regenerar a pedido.
- **Loop diario**: trigger `trig_01TFHhGouJWbbPKjoS9JQz1H`, 08:00 NZ. Revisa
  repos → actualiza dashboard → push al teléfono si urgente → puede avanzar
  código SOLO en proyectos en pausa (Padel, La-Suiza). NUNCA Kiwiano/fitmark.
- **Fuentes de estado**: git = verdad dura; bloque `## Torre de control` al
  inicio de cada HANDOFF (Kiwiano/docs/HANDOFF.md, fitmark/HANDOFF.md) =
  verdad narrativa. Ya creados en rama claude/project-portfolio-tracking-ib0574;
  los chats de dev deben adoptarlos en main.
- **Costos de tokens**: `portfolio/metricas/sesiones.csv` — Gustavo reporta el
  gasto de sus otros chats; aún sin datos.

## Convenciones de trabajo

- Rama de esta sesión en TODOS los repos: `claude/project-portfolio-tracking-ib0574`.
- Gustavo habla español; docs del portfolio en español.
- Ideas nuevas → `portfolio/IDEAS.md`, no interrumpen el sprint.
- Al cerrar sesión: actualizar este context.md + append en `sessions/`,
  fila en sesiones.csv, commit + push.

## Próximos pasos (para la siguiente sesión de torre de control)

1. ✅ Bloques "Torre de control" adoptados en main por ambos chats (verificado 05-jul).
2. ✅ Primera corrida del loop OK (05-jul): detectó merge de Vitrina y QA de FitMark.
3. Vigilar: backups Supabase Kiwiano (vence 20-jul), free vs premium FitMark.
4. Cuando Gustavo pase costos de tokens → llenar CSV y activar panel de costos.
5. Guiones de reels de la semana 1 cuando los pida (ver CONTENIDO.md).
6. Naming FitMark: retomar antes del 15-ago.
7. Trabajo autónomo hecho en Padel: .env.example creado (faltaba, docs lo referencian).
