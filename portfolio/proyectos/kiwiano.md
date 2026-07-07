# Kiwiano — Ficha de proyecto

> Actualizado: 2026-07-06

**Qué es**: plataforma SaaS multi-club de torneos y ranking de pádel. Cada club vive en
`/club/[slug]` con su marca. Admins pegan nombres desde WhatsApp — sin cuentas
individuales por diseño. Bilingüe ES/EN. Deploy: `kiwiano.vercel.app`.

**Stack**: Next.js 16.2 · React 19 · Tailwind 4 · Zustand · Supabase (Postgres + Realtime)
· Auth propia (3 contraseñas por club: espectador/jugador/admin + superadmin, bcrypt + cookie HMAC).

## Estado (actualizado 2026-07-06 por el loop, desde git main)

- ✅ **F1–F3 completas**: motores Americano + Liga, ranking, historial, perfiles de jugador,
  likes atómicos, guardado con optimistic locking, realtime, imágenes para stories 9:16, PWA, OG images.
- ✅ **F4 "UI vendible" COMPLETA (05-jul)**: Vitrina mergeada a main — landing pública con
  3 hooks + precios en pelotas + caja de 24 gratis, mocks bilingües fieles, modo TV,
  PWAs instaladas abren en su club, realtime de espectador arreglado.
- 🟢 **F5.1 monetización MERGEADA a main (06-jul)**: sistema de pelotas (ledger + débito al
  crear torneo + reembolso al cancelar + caja de 24 de bienvenida) + planes + **billing UI
  club y superadmin** + panel de cobros en /superadmin + membresía **$40 NZD** con precios
  desde constantes + torneos de prueba restringidos a superadmin + billing hardening.
- 🟢 **F5.2 Stripe Checkout CODEADO (07-jul), en pruebas en Vitrina**: acción de checkout +
  webhook `/api/stripe/webhook` + botón "Pagar con tarjeta", todo opt-in por env vars
  (sin claves = la app sigue igual). También: saldo de pelotas visible para jugadores,
  recordatorio de vencimiento de membresía, pase de UX premium (a11y, touch targets).
- 🔑 **Bloqueador EN MANOS DE TAVO**: crear el webhook endpoint en Stripe (Sandbox) y pegar
  `STRIPE_SECRET_KEY` + `STRIPE_WEBHOOK_SECRET` en Vercel → probar pago con tarjeta test
  en preview → merge a main con claves live. Fecha objetivo: **2026-08-10**.
- ❌ **F6 growth sin empezar**: categorías, inscripción online, notificaciones, multi-deporte.

## Brechas para comercializar

1. ~~Landing pública~~ ✅ lista (05-jul).
2. ~~Máquina de cobro (pelotas + planes + billing UI)~~ ✅ mergeada (06-jul) — falta **Stripe real** (F5.2) + correr migración 012.
3. Onboarding self-service (hoy solo el superadmin crea clubes).
4. Analytics: cero.
5. Backups Supabase automáticos (F1.6, hoy manual — vence 20-jul).

**Docs internas**: `docs/HANDOFF.md`, `docs/PLATFORM_PLAN.md`, `docs/ROADMAP_PREMIUM.md`.
