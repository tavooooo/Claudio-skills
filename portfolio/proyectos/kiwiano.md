# Kiwiano — Ficha de proyecto

> Actualizado: 2026-07-05

**Qué es**: plataforma SaaS multi-club de torneos y ranking de pádel. Cada club vive en
`/club/[slug]` con su marca. Admins pegan nombres desde WhatsApp — sin cuentas
individuales por diseño. Bilingüe ES/EN. Deploy: `kiwiano.vercel.app`.

**Stack**: Next.js 16.2 · React 19 · Tailwind 4 · Zustand · Supabase (Postgres + Realtime)
· Auth propia (3 contraseñas por club: espectador/jugador/admin + superadmin, bcrypt + cookie HMAC).

## Estado (actualizado 2026-07-05 por el loop, desde HANDOFF main)

- ✅ **F1–F3 completas**: motores Americano + Liga, ranking, historial, perfiles de jugador,
  likes atómicos, guardado con optimistic locking, realtime, imágenes para stories 9:16, PWA, OG images.
- ✅ **F4 "UI vendible" COMPLETA (05-jul)**: Vitrina mergeada a main — landing pública con
  3 hooks + precios en pelotas + caja de 24 gratis, mocks bilingües fieles, modo TV,
  PWAs instaladas abren en su club, realtime de espectador arreglado.
- 🟡 **F5 monetización EN CURSO**: Stripe con saldo de pelotas + membresía. Fecha objetivo
  del chat de dev: **2026-08-10**.
- ❌ **F6 growth sin empezar**: categorías, inscripción online, notificaciones, multi-deporte.

## Brechas para comercializar

1. ~~Landing pública~~ ✅ lista (05-jul).
2. Cobro: Stripe saldo de pelotas + membresía (F5, en curso, 10-ago).
3. Onboarding self-service (hoy solo el superadmin crea clubes).
4. Analytics: cero.
5. Backups Supabase automáticos (F1.6, hoy manual — vence 20-jul).

**Docs internas**: `docs/HANDOFF.md`, `docs/PLATFORM_PLAN.md`, `docs/ROADMAP_PREMIUM.md`.
