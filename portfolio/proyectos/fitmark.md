# FitMark — Ficha de proyecto

> Actualizado: 2026-07-05

**Qué es**: tracker de entrenamiento de fuerza mobile-first (iPhone-first). Registro de
sesiones y PRs, rutinas, base de 152 ejercicios, mapa muscular SVG/3D interactivo,
logros, y **Wallace**, coach IA (Claude API). En español. Deploy: Vercel (auto en `main`).

**Stack**: Next.js 16.2 · React 19 · Tailwind 4 · Zustand + Zod · GSAP/three.js/recharts
· Supabase (Postgres + Auth con Google OAuth, RLS verificada) · Prisma · Vitest (32 tests) + Playwright.

## Estado

- ✅ Núcleo maduro: tracker, rutinas, ejercicios, mapa muscular, coach IA, landing con scroll-video, onboarding progresivo.
- 🟡 `/logros` "en construcción"; `/store` es solo vitrina visual (sin checkout).
- 🟡 Rama `claude/features-review` pausada (ranking, muro social, planes, coach) con colisión de migración `003`.
- 🟡 Wallace KB RAG (`wallace-kb/`, 262 artículos) sin conectar.
- ❌ **Monetización: nada** — sin Stripe, "premium" es solo copy.
- ❌ **Analytics: nada.**

## Brechas para comercializar

1. Analytics + funnel (¿la gente termina el onboarding? ¿usa Wallace?).
2. Rate-limit `/api/chat` (Upstash) — sin esto el coach IA es un costo sin techo.
3. Modelo de precios freemium + Stripe subscripciones.
4. `ADMIN_EMAILS` en Vercel y quitar fallback hardcodeado en `src/lib/admin.ts`.
5. Rescatar `features-review` (resolver migración 003).

**Docs internas**: `HANDOFF.md` (actualizado 2026-07-04), `docs/STACK.md`, `AGENTS.md` (reglas UI de contraste y overlays — respetar siempre).
