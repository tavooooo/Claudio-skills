# Kiwiano — Ficha de proyecto

> Actualizado: 2026-07-15 (git; su HANDOFF al día, 15-jul)

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
    `AccountsAdmin.tsx` y `LinkPlayerBanner.tsx` nuevos) — ✅ **aclarado (14-jul, HANDOFF)**: no
    reemplaza el login compartido de 3 contraseñas, **convive** con él (login personal + código
    de registro + enlazar jugador). No es un pivote de diseño.
  - Ligas inter-clubes (backend + `/liga/[slug]` pública + gestión), fotos de jugadores,
    multi-deporte, grupos con ranking propio, dashboard Pro (`ProInsights.tsx`), stories con sponsor.
  - ✅ **Migraciones 015→019 CORRIDAS en Supabase (14-jul)** — todo el bloque ya está activo
    en producción, no solo en el código.
- 🎥 **Cámara en vivo WebRTC — mergeada a main y VALIDADA EN PERSONA por Tavo, sin lag (14-jul)**:
  celular → modo TV por WiFi (~0.3s), señalización por Supabase Realtime (sin servidor de video
  ni migración nueva), selector de lentes 0,5×/1×/3×, video 16:9 1080p pantalla completa. v1 es
  1 cámara→1 TV (multi-espectador necesitaría un SFU). Esto es lo que la pipeline daba por
  "diferido post-monetización" — llegó de todos modos, en paralelo a F5.2 Stripe.
  - ⚠️ **Pendiente conocido (discutido con Tavo, sin codear)**: la cámara solo garantiza conexión
    dentro de la MISMA WiFi (P2P sin TURN falla entre redes por NAT/CGNAT). Dos mejoras: (a) TURN
    de respaldo (sigue 1:1), (b) SFU si se quiere que cualquier visitante del sitio vea la
    transmisión en vivo (feature más grande, evaluar costo/infra).
- ✅ **Backups F1.6 Capa 2 (offsite) HECHOS y verificados (15-jul, en main)**: GitHub Action diario
  (`.github/workflows/backup.yml`, Node 22) exporta las 12 tablas a JSON → artifact (90d) + rama
  huérfana `backups` (`AAAA/MM/DD/`). Verificado corriendo solo. **Capa 1** (PITR gestionado de
  Supabase) pospuesta a propósito por Tavo hasta tener clientes de pago. Cierra el riesgo que
  estaba en el tablero (vencía 20-jul). Pendiente menor: respaldar buckets de Storage offsite.
- 🎨 **Rediseño UX del flujo Pro + pase visual premium (15-jul, mergeado a main desde `vitrina`)**:
  menú admin reorganizado por tarea, **Interclubes** con puerta propia `/interclubes`, config del
  club movida a `/ajustes`, nuevo **Centro de control** `/centro` (mosaico de tareas del admin),
  CTAs de marca con gradiente+glow en todas las pantallas, landing con sección "En directo" (mock
  fiel al modo TV real: video + score bug + standings) y barra de auspicios (marquee) en el TV.
  Blueprint en `docs/REDISENO_PRO.html`. Todo con confirmación en acciones destructivas.

## Brechas para comercializar

1. ~~Landing pública~~ ✅ lista (05-jul).
2. ~~Máquina de cobro (pelotas + planes + billing UI)~~ ✅ mergeada (06-jul) — falta **Stripe real** (F5.2) + correr migración 012.
3. Onboarding self-service (hoy solo el superadmin crea clubes).
4. Analytics: cero.
5. Backups Supabase automáticos (F1.6, hoy manual — vence 20-jul).

**Docs internas**: `docs/HANDOFF.md`, `docs/PLATFORM_PLAN.md`, `docs/ROADMAP_PREMIUM.md`.
