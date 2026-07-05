# Easy Courts (repo: Padel) — Ficha de proyecto

> Actualizado: 2026-07-05

**Qué es**: plataforma web premium para gestionar clubes de pádel/pickleball:
**arriendo de canchas**, clases, torneos/ligas, partidas abiertas (estilo Playtomic),
pagos y panel de administración completo. En español, con localización Chile.

**Stack**: Next.js 16.2 · React 19 · Tailwind 4 · framer-motion · recharts
· Prisma 7.8 (schema de ~638 líneas, 20 modelos — **desconectado de la app**)
· Stripe integrado (checkout + webhook firmado) en **modo demo, sin llaves reales**.

## Estado — "Etapa 0" completa: demo navegable de punta a punta, nada persiste

- ✅ App jugador completa: inicio, reservar, partidas, clases, eventos, ligas, pagos, perfil, checkout.
- ✅ Admin completo: dashboard, reservas, pistas, clases, eventos, ligas, socios, finanzas, ajustes.
- ✅ Landing de marketing + PWA + headers de seguridad.
- ❌ **TODO es mock** (`src/lib/data.ts`): mutaciones en memoria, auth falsa (client-only), `/admin` sin protección server-side.
- ❌ Falta `.env.example` (las docs lo referencian).

## Brechas para comercializar (Etapas 1–4 del roadmap)

1. **Etapa 1 (la crítica)**: Postgres real + conectar Prisma + auth real (Auth.js/Supabase) + proteger `/admin` + Server Actions persistentes.
2. Stripe live + pasarela chilena (Transbank / Mercado Pago).
3. Emails/push, monitoreo, tests E2E.
4. Multi-tenant (varios clubes).

**Nota estratégica**: es el producto con mayor ticket potencial (B2B, clubes pagan
mensualidad), pero el que más lejos está de producción. No empezar Etapa 1 hasta que
Kiwiano esté cobrando (ver `PIPELINE.md`).

**Docs internas**: `README.md`, `ROADMAP.md`, `DATABASE.md`, `SECURITY.md`.
