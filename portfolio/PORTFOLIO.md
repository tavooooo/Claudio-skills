# 📊 Portfolio — Dashboard Maestro

> Última actualización: **2026-07-08** · Actualizar en cada sesión de trabajo.

## Estado global

| Proyecto | Fase | Avance | ¿Comercializable hoy? | Bloqueador principal | Próximo hito | Deadline |
|---|---|---|---|---|---|---|
| **Kiwiano** | F5 monetización **80%** — F5.1 en producción; **F5.2 Stripe Checkout codeado (Vitrina), EN PRUEBAS** | 🟢 Alto — **activo, en otro chat** | Casi — checkout escrito, falta probarlo con claves | **Tavo**: crear webhook en Stripe + pegar `sk_test_`/`whsec_` en Vercel | Prueba de pago con tarjeta test en preview → merge a main con claves live | **2026-08-10** (fecha del chat de dev) |
| **FitMark** (nombre por definir) | Carrera al lanzamiento (**91%**) — íconos musculares en toda la app, calendario semanal, medallas retroactivas, Wallace con fallback | 🟢 Alto — **activo, en otro chat** | Casi — freemium listo con **cobro simulado**, falta pasarela real | Pasarela de pago real + nombre definitivo (15-ago) | Pasarela de pago real | 🎯 Lanzamiento gratis **2026-08-31** |
| **Easy Courts** | Etapa 0 (demo mock completa) | 🟡 Medio — en pausa | No — nada persiste | Todo es mock: sin DB real, sin auth real, admin sin protección | Etapa 1: Postgres + Prisma + auth real | 2026-12-15 |
| **Navaja Suiza** | **~80%, chat ACTIVO** — desplegada (Vercel) + upgrade premium (09-jul); pista comercial | 🟡 Medio — activo, apuesta #3 | Casi — desplegada; falta nube + login (+ compartir para el divisor) | Necesita que Tavo cree el proyecto Supabase + claves; luego login | Conectar Supabase + Login (su próximo hito); después divisor colaborativo | este mes (baja) |

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
- ✅ **`features-review` — DECIDIDO (08-jul): se DESCARTA y se reconstruye desde cero.** A 129 commits de divergencia, rehacer limpio salía más barato que el cherry-pick. Lo que había (a reconstruir en main): ranking, red social/feed, planes, cuentas gym/coach, chat. ⚠️ **Excepción a salvar ANTES de borrar**: `wallace-kb/` = 262 artículos = **contenido escrito** (1 archivo `.wkml` de ~550KB + índice HTML), NO código — exportarlo es gratis y evita reescribir 262 artículos a mano. La rama la borra el chat de dev de FitMark (no la torre).
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
