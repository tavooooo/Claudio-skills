# Kiwiano — Ficha de proyecto

> Actualizado: 2026-07-05

**Qué es**: plataforma SaaS multi-club de torneos y ranking de pádel. Cada club vive en
`/club/[slug]` con su marca. Admins pegan nombres desde WhatsApp — sin cuentas
individuales por diseño. Bilingüe ES/EN. Deploy: `kiwiano.vercel.app`.

**Stack**: Next.js 16.2 · React 19 · Tailwind 4 · Zustand · Supabase (Postgres + Realtime)
· Auth propia (3 contraseñas por club: espectador/jugador/admin + superadmin, bcrypt + cookie HMAC).

## Estado

- ✅ **F1–F3 completas**: motores Americano + Liga, ranking, historial, perfiles de jugador,
  likes atómicos, guardado con optimistic locking, realtime, imágenes para stories 9:16, PWA, OG images.
- 🟡 **F4 "UI vendible" ~70%**: F4.5 (transiciones) lista; **F4.1 landing, F4.2 home, F4.3 modo TV
  están en la rama `Vitrina` sin mergear y desactualizada** ← rescatar primero.
- ❌ **F5 monetización sin empezar**: Stripe, planes Free/Club/Pro, onboarding self-service.
- ❌ **F6 growth sin empezar**: categorías, inscripción online, notificaciones, multi-deporte.

## Brechas para comercializar

1. Landing pública (rama Vitrina) — sin esto no hay puerta de entrada.
2. Cobro: Stripe + planes (F5).
3. Onboarding self-service (hoy solo el superadmin crea clubes).
4. Analytics: cero.
5. Backups Supabase automáticos (F1.6, hoy manual).

**Docs internas**: `docs/HANDOFF.md`, `docs/PLATFORM_PLAN.md`, `docs/ROADMAP_PREMIUM.md`.
