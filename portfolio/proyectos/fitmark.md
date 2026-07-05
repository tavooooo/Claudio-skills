# FitMark / Biohack AI — Ficha de proyecto

> Actualizado: 2026-07-05
> **Nombre en transición**: Gustavo está evaluando renombrar el producto a
> "Biohack AI", pero no lo convence del todo. FitMark sigue siendo el nombre
> del repo/código. Ver `IDEAS.md` para el brainstorm de nombres.

**Qué es**: tracker de entrenamiento de fuerza mobile-first (iPhone-first). Registro de
sesiones y PRs, rutinas, base de 152 ejercicios, mapa muscular SVG/3D interactivo,
logros, y **Wallace**, coach IA (Claude API). En español. Deploy: Vercel (auto en `main`).

**Stack**: Next.js 16.2 · React 19 · Tailwind 4 · Zustand + Zod · GSAP/three.js/recharts
· Supabase (Postgres + Auth con Google OAuth, RLS verificada) · Prisma · Vitest (32 tests) + Playwright.

## Estado (actualizado 2026-07-05 por el loop, desde HANDOFF main — 85%)

- ✅ Núcleo maduro: tracker, rutinas, ejercicios, mapa muscular, coach IA, landing con scroll-video, onboarding progresivo.
- ✅ **05-jul**: PRs con celebración de récords, plantillas de rutina y peso corporal,
  guía de primeros pasos, admin de usuarios, y **QA profundo con 5 auditores paralelos
  (48 hallazgos, ~25 arreglados: bucle de redirects, falsos récords, TZ Chile, seguridad admin)**.
  El chat de dev declara la app "funcional de punta a punta y auditada".
- 🎯 Próximo hito (según HANDOFF): **definir free vs premium**.
- 🟡 `/logros` "en construcción"; `/store` es solo vitrina visual (sin checkout).
- 🟡 **Rama `claude/features-review` (415 commits divergentes)**: decisión de Gustavo
  (2026-07-05) — contiene solo algunas cosas útiles; plan = **rescate selectivo pronto
  (cherry-pick de lo útil) y luego descartar la rama**. Ya no es reconciliación completa,
  pero el rescate sigue teniendo fecha objetivo: antes del Sprint 4 (sep).
- 🟡 Wallace KB RAG (`wallace-kb/`, 262 artículos) sin conectar.
- ❌ **Monetización: nada** — sin Stripe, "premium" es solo copy.
- ❌ **Analytics: nada.**

## Brechas para comercializar

1. Analytics + funnel (¿la gente termina el onboarding? ¿usa Wallace?).
2. Rate-limit `/api/chat` (Upstash) — sin esto el coach IA es un costo sin techo.
3. Modelo de precios freemium + Stripe subscripciones.
4. `ADMIN_EMAILS` en Vercel y quitar fallback hardcodeado en `src/lib/admin.ts`.
5. Reconciliar `features-review` (diagnóstico primero: 415 commits divergentes, no un merge trivial).
6. Cerrar nombre definitivo del producto (ver brainstorm en `IDEAS.md`).

## Competencia — fierro.app (vigilancia activa)

Investigación de Gustavo (2026-07-05, probando la app directamente):

- **También está en construcción**: sin planes de pago, todo gratis por ahora.
- **Rutinas precargadas flojas**: mal manejo de descansos, explicaciones de
  ejercicios pobres.
- **Librería de ejercicios rota**: da error 404 — no existe todavía.

**Nuestras ventajas hoy**: librería de 152 ejercicios funcionando, mapa muscular
SVG/3D, coach IA (Wallace) operativo, deploy estable en Vercel.

**Implicancia estratégica**: hay una VENTANA — salir públicamente antes de que
fierro complete su producto. La carrera es por la librería + experiencia de
entrenamiento, no por el precio (ellos son gratis). Revisar fierro.app en cada
loop semanal para detectar sus avances.

**Docs internas**: `HANDOFF.md` (actualizado 2026-07-04), `docs/STACK.md`, `AGENTS.md` (reglas UI de contraste y overlays — respetar siempre).
