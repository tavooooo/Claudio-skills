# Kiwiano — Ficha de proyecto

> Actualizado: 2026-07-13 (git; su HANDOFF narra hasta 07-07, ahora 6 días desactualizado)

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
- 🟢 **F5.4 Plan Gratis ✅ shipped (09-jul)**: tier de demo completo — cap de 2 torneos
  (soft-delete rotativo, reversible al subir de plan), 12 jugadores máx, sin branding,
  badge "Plan Gratis" en modo TV, stats premium con teaser, Panel del club, selector
  express de plan en superadmin. Requiere migración `014_free_plan.sql`.
- 🟢 **Precios de landing actualizados (10-jul)**: Membresía $79 / Pro $159, con 30% off
  de lanzamiento (ojo: HANDOFF viejo hablaba de $40 NZD — la estructura de precios cambió,
  confirmar con Tavo si $40 quedó obsoleto o es un tier "Prepago" distinto).
- 🟢 **Compartir para RRSS (11-jul)**: tarjeta cuadrada de perfil de jugador + imágenes de
  podio (story 9:16 + cuadrado 1:1) — sin depender de Stripe. Mismo tipo de feature que
  FitMark construyó la misma semana, sin coordinación entre chats.
- 🗺️ **F8 "Plan Pro completo" planificado (09-jul)**: roadmap en `docs/PLAN_PRO.md`, ~5-7
  sesiones en olas (gestión de jugadores, stories, multi-deporte, grupos con ranking propio,
  dashboard de negocio, marcador en vivo Pro-only que absorbe F7.1, liga inter-clubes).
  Patrón declarado: "fundación por el asistente + agentes en paralelo" — usa orquestación
  multi-agente. Es planificación, aún sin código shippeado.
- 🔑 **Bloqueador de F5.2 SIN CAMBIOS**: sigue esperando que Tavo cree el webhook en Stripe
  y pegue las claves en Vercel. Fecha objetivo: **2026-08-10**.
- ❌ **F6 crecimiento (continuo, va al final)**: categorías, inscripción online, notificaciones, multi-deporte.
- 🚀 **Merge GRANDE "olas 1-5" a main (13-jul)**: merge selectivo desde Vitrina, 77 archivos,
  +9729/-409 líneas, **excluyendo Stripe a propósito** (queda solo en la rama de desarrollo).
  Incluye:
  - **Modo TV 2.0**: cancha dibujada, score bug estilo transmisión, hasta 2 videos por cancha
    con marcador anclado e intercambio, tabla de posiciones con auto-scroll, punto de oro.
  - **Marcador en vivo punto a punto** (tenis/corrido) con anotador rediseñado — esto es F8.2
    (absorbía a F7.1), llegó antes de lo que la pipeline proyectaba.
  - **Cuentas individuales por club + login premium** (`AuthModal.tsx` casi triplicó tamaño,
    `AccountsAdmin.tsx` y `LinkPlayerBanner.tsx` nuevos) — ⚠️ contrasta con el diseño original
    documentado ("sin cuentas individuales por diseño", admins pegan nombres desde WhatsApp).
    Vale confirmar con el chat de dev si esto es un pivote de producto deliberado o un feature
    opcional/paralelo al modelo de 3 contraseñas por club.
  - Ligas inter-clubes (backend + `/liga/[slug]` pública + gestión), fotos de jugadores,
    multi-deporte, grupos con ranking propio, dashboard Pro (`ProInsights.tsx`), stories con sponsor.
  - 🔑 **5 migraciones SQL nuevas sin correr** (`015_pro_foundation` a `019_player_photos`) —
    sin ellas, todo este bloque queda inerte en producción aunque el código ya está en main.
    Es el mismo patrón que Suiza (código listo, bloqueado por un paso de infra de Tavo/Gustavo).
  - Rama activa aparte (`claude/handoff-premium-roadmap-0ojicp`, no mergeada) siguiendo con
    streaming por cámara vía WebRTC — la pipeline marcaba esto como "diferido post-monetización"
    y ya está en desarrollo.

## Brechas para comercializar

1. ~~Landing pública~~ ✅ lista (05-jul).
2. ~~Máquina de cobro (pelotas + planes + billing UI)~~ ✅ mergeada (06-jul) — falta **Stripe real** (F5.2) + correr migración 012.
3. Onboarding self-service (hoy solo el superadmin crea clubes).
4. Analytics: cero.
5. Backups Supabase automáticos (F1.6, hoy manual — vence 20-jul).

**Docs internas**: `docs/HANDOFF.md`, `docs/PLATFORM_PLAN.md`, `docs/ROADMAP_PREMIUM.md`.
