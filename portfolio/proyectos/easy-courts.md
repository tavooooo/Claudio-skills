# Easy Courts (repo: Padel) — Ficha de proyecto

> Actualizado: 2026-07-17 por el loop, desde git

**Qué es**: plataforma web premium para gestionar clubes de pádel/pickleball:
**arriendo de canchas**, clases, torneos/ligas, partidas abiertas (estilo Playtomic),
pagos y panel de administración completo. Bilingüe ES/EN (nuevo 12-jul).

**Stack**: Next.js 16.2 · React 19 · Tailwind 4 · framer-motion · recharts
· Prisma (schema de ~638 líneas, 20 modelos — **desconectado de la app**)
· Stripe integrado (checkout + webhook firmado) en **modo demo, sin llaves reales**.

## Estado — "Etapa 0" completa (~50% estimado), TIENE CHAT ACTIVO

- 🟢 **Ya no está en pausa**: entre el 07 y el 12 de julio subió a "nivel producto"
  (partidas abiertas, notificaciones, búsqueda global, seguridad server-side) y
  completó **i18n ES/EN de toda la app** (12-jul) — mismo tipo de trabajo que FitMark
  hizo días antes, sin coordinación entre chats.
- ✅ **Reporta tokens por primera vez (12-jul)**: hook instalado y funcionando, ya
  visible en el panel de costos de la torre.
- ✅ App jugador completa: inicio, reservar, partidas, clases, eventos, ligas, pagos, perfil, checkout.
- ✅ Admin completo: dashboard, reservas, pistas, clases, eventos, ligas, socios, finanzas, ajustes.
- ✅ Landing de marketing + PWA + headers de seguridad.
- ❌ **TODO sigue siendo mock** (`src/lib/data.ts`): mutaciones en memoria, auth falsa
  (client-only), `/admin` sin protección server-side. La i18n y las mejoras de producto
  no cambiaron esto — es la Etapa 1 completa la que falta.
- 🟢 **Landing rediseñada (13-jul)**: rediseño premium con animaciones + selector de idioma,
  pelotas de pádel con parallax de scroll (y un fix de recorte de costuras el mismo día).
  Repo también creó rama `main` nueva (mismo commit que la rama de tracking) — no es
  contenido nuevo, solo un puntero equivalente.
- 🟡 **Demo más funcional pero SIGUE en Etapa 0 (17-jul)**: agregó **persistencia local**
  (`src/lib/store.tsx`, demo store en el navegador), 8 features nuevas, QR + compartir + enlaces
  externos + guía de niveles, y una **matriz de QA 15/15 verde** (i18n vivo en datos merged, reset
  completo). ⚠️ **Ojo, no confundir**: `src/lib/data.ts` **sigue siendo "Mock Data Layer"** — la
  persistencia es del lado del navegador, NO hay Postgres ni auth reales. La Etapa 1 (la que lo
  vuelve vendible) sigue sin empezar. Estimado ~55→58% por el pulido del demo. Reportó tokens de
  nuevo (17-jul: 495M in / 1,92M out).
- 💼 **Primer paso comercial: deck de ventas + pagos + matchmaking (23-jul)**: **deck de presentación
  para dueños de club** (`/presentacion.html`, página estática interactiva) — el material para salir a
  vender a clubes. Además: **pagar en el club (efectivo)** con restricción por deuda pendiente,
  matchmaking (compartir una reserva la publica como **partida abierta**), invitaciones dirigidas,
  selector de cuenta para impersonar socios (demo), y fix de i18n en los charts de admin (inglés).
  Sigue siendo demo (mock), pero es la primera vez que arma material de venta B2B.
- 🔦 **Acceso físico + luces por pista (18-jul, demo bien arquitecturado)**: código de acceso
  (PIN + ventana horaria con buffer) y control de luces on/off por pista desde la reserva, detrás
  de una capa `src/lib/access/provider.ts` — interfaz `AccessProvider` + `DemoAccessProvider` que
  **se cambia por un adaptador real (UniFi Access / Protege WX / relé Shelly) sin tocar la UI**.
  Investigación de integración real ya documentada en el repo. Es el tipo de valor B2B que
  diferencia a Easy Courts (el club automatiza acceso/luces desde la app). + **rating numérico
  1.0–7.0** (estándar internacional, con equivalencias). Sigue siendo demo (Etapa 0). ~58→60%.
  Tokens 18-jul: 498M in / 1,93M out.

## Brechas para comercializar (Etapas 1–4 del roadmap)

1. **Etapa 1 (la crítica)**: Postgres real + conectar Prisma + auth real (Auth.js/Supabase)
   + proteger `/admin` + Server Actions persistentes. Bloqueada: requiere que Gustavo
   provea `DATABASE_URL` de Supabase + claves Stripe; además Prisma no genera su cliente
   en el sandbox (el proxy bloquea la descarga del engine) — hay que correr
   `npm run db:generate` en local/CI.
2. Stripe live + pasarela chilena (Transbank / Mercado Pago).
3. Emails/push, monitoreo, tests E2E.
4. Multi-tenant (varios clubes).

**Nota estratégica**: es el producto con mayor ticket potencial (B2B, clubes pagan
mensualidad), pero el que más lejos está de producción. No empezar Etapa 1 hasta que
Kiwiano esté cobrando (ver `PIPELINE.md`).

**Docs internas**: `HANDOFF.md`, `ROADMAP.md`, `DATABASE.md`, `SECURITY.md`.
