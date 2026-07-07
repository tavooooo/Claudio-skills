# 📊 Portfolio — Dashboard Maestro

> Última actualización: **2026-07-07** · Actualizar en cada sesión de trabajo.

## Estado global

| Proyecto | Fase | Avance | ¿Comercializable hoy? | Bloqueador principal | Próximo hito | Deadline |
|---|---|---|---|---|---|---|
| **Kiwiano** | F5 monetización **80%** — F5.1 en producción; **F5.2 Stripe Checkout codeado (Vitrina), EN PRUEBAS** | 🟢 Alto — **activo, en otro chat** | Casi — checkout escrito, falta probarlo con claves | **Tavo**: crear webhook en Stripe + pegar `sk_test_`/`whsec_` en Vercel | Prueba de pago con tarjeta test en preview → merge a main con claves live | **2026-08-10** (fecha del chat de dev) |
| **FitMark** (nombre por definir) | Carrera al lanzamiento (**91%**) — Wallace conversacional + rendimiento + drag unificado | 🟢 Alto — **activo, en otro chat** | Casi — freemium listo con **cobro simulado**, falta pasarela real | Pasarela de pago real + nombre definitivo (15-ago) | Pasarela de pago real | 🎯 Lanzamiento gratis **2026-08-31** |
| **Easy Courts** | Etapa 0 (demo mock completa) | 🟡 Medio — en pausa | No — nada persiste | Todo es mock: sin DB real, sin auth real, admin sin protección | Etapa 1: Postgres + Prisma + auth real | 2026-12-15 |
| **Navaja Suiza** | Fase 1 completa (local-only) | 🟢 Alto — congelado | N/A (personal) | Sin nube (Supabase scaffolded, inactivo) | Mantener; evaluar comercializar en 2027 | — |

> **Nota de esta sesión**: Kiwiano y Biohack AI se desarrollan activamente en
> otros chats en paralelo. Esta sesión (Claudio-skills) es la torre de control:
> no compite con ese trabajo, lo coordina — lee el estado real del repo (git log)
> y mantiene este dashboard al día.

## Orden de la pipeline (foco secuencial, no picotear)

1. **Kiwiano** → es el más cerca de venderse: F1–F3 listas, solo falta vitrina + Stripe.
2. **FitMark** → producto sólido con deploy en Vercel; necesita monetización y datos de uso.
3. **Easy Courts** → mayor potencial de ticket (B2B clubes) pero le falta una fase entera de integración.
4. **Navaja Suiza** → congelado como proyecto personal; no invertir tokens salvo mantenimiento.

## Semáforo de riesgos

- 🔴 **Ningún proyecto genera ingresos reales aún** — pero la máquina de cobro ya existe en ambos:
  Kiwiano F5.1 (pelotas + planes + billing UI, cobro manual) mergeado 06-jul; FitMark freemium 5/5
  cableado 06-jul con **cobro simulado**. Falta cerrar con pasarela real (Kiwiano Stripe F5.2, FitMark pasarela).
- 🔴 **Carrera con fierro.app**: competidor directo pero incompleto (sin pagos, librería 404, rutinas flojas — verificado por Gustavo 05-jul). Decisión: FitMark sale primero — lanzamiento público adelantado a **fin de agosto**. Vigilar fierro.app semanalmente.
- 🟠 **Contenido en redes parte esta semana** (ver `CONTENIDO.md`) — construir audiencia antes del lanzamiento; sin distribución no hay carrera que ganar.
- 🟠 **`features-review` de FitMark — la divergencia CRECE** (07-jul: main pasó de 67 a **90 commits adelante**; la rama sigue con 415): rescate selectivo y descartar (decidido 05-jul; ejecutar en julio). Cada día de dev activo en main encarece el cherry-pick (incluye Wallace KB de 262 artículos).
- 🟡 **Nombre definitivo aparcado** — deadline dura 15-ago (antes del lanzamiento público).
- ✅ ~~Kiwiano `Vitrina` pendiente de merge~~ — **RESUELTO 05-jul**: mergeada a main con landing completa. Sprint 1 completado 15 días antes de fecha.
- ✅ ~~Máquina de cobro de Kiwiano~~ — **F5.1 en producción** (pelotas, planes, billing UI, membresía $40 NZD, saldo visible a jugadores, recordatorio de vencimiento). **F5.2 Stripe Checkout codeado y en pruebas** — 🔑 bloqueado por Tavo: crear webhook en Stripe Sandbox + `STRIPE_SECRET_KEY`/`STRIPE_WEBHOOK_SECRET` en Vercel.
- 🟡 Backups automáticos Supabase de Kiwiano (F1.6) siguen pendientes (vence **20-jul**).
- 🟠 **Cero analytics en todos los productos** — sin datos de usuarios no hay buenas decisiones de negocio.
- 🟡 **Nombre de FitMark sin cerrar** — riesgo de seguir construyendo marca/copy sobre un nombre que se va a cambiar (deadline 15-ago).

## Definición de "comercializable" (checklist por producto)

- [ ] Landing pública con propuesta de valor clara
- [ ] Onboarding self-service (sin intervención manual)
- [ ] Flujo de cobro real (Stripe / Transbank / Mercado Pago)
- [ ] Analytics de uso (eventos clave + funnel)
- [ ] Términos de servicio + privacidad
- [ ] Soporte/contacto y monitoreo de errores
