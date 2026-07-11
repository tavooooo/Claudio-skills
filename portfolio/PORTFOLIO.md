# 📊 Portfolio — Dashboard Maestro

> Última actualización: **2026-07-11** · Actualizar en cada sesión de trabajo.

## Estado global

| Proyecto | Fase | Avance | ¿Comercializable hoy? | Bloqueador principal | Próximo hito | Deadline |
|---|---|---|---|---|---|---|
| **Kiwiano** | F5 monetización **~80%** — F5.4 Plan Gratis ✅ shipped 09-jul, precios de landing actualizados (Membresía $79/Pro $159, 30% off lanz.), F8 Plan Pro roadmap planificado; **F5.2 Stripe sigue EN PRUEBAS, sin avance** | 🟢 Alto — **activo, en otro chat** ⚠️ HANDOFF desactualizado (dice 07-07, git llega a 11-jul) | Casi — checkout escrito, falta probarlo con claves | **Tavo**: crear webhook en Stripe + pegar `sk_test_`/`whsec_` en Vercel (sin cambios) | Prueba de pago con tarjeta test en preview → merge a main con claves live | **2026-08-10** (fecha del chat de dev) |
| **FitMark** (nombre por definir) | Carrera al lanzamiento (**91%**, su propio número) — tarjetas de "compartir" para RRSS (11-jul, varios fixes de iOS), Wallace fundamenta rutinas en la KB + auto-crece la base | 🟢 Alto — **activo, en otro chat** ⚠️ HANDOFF desactualizado (dice 07-08, git llega a 11-jul) | Casi — freemium listo con **cobro simulado**, falta pasarela real | Pasarela de pago real + nombre definitivo (15-ago) | Pasarela de pago real | 🎯 Lanzamiento gratis **2026-08-31** |
| **Easy Courts** | Etapa 0 completa (~45%) — **chat ACTIVO** (subió a nivel producto: partidas abiertas, notificaciones, búsqueda, seguridad); HANDOFF + reporte configurado 09-jul | 🟡 Medio — activo | No — todo mock, nada persiste | Necesita que Tavo provea Supabase (`DATABASE_URL`) + claves Stripe; Prisma no genera en sandbox | Etapa 1: conectar DB + auth real + deploy piloto | 2026-12-15 |
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
- ✅ **`features-review` — RESUELTA (09-jul): BORRADA por el chat de FitMark.** La rama ya no existe. Se reconstruirá desde cero en main cuando toque (ranking, red social/feed, planes, cuentas gym/coach, chat — checklist en `IDEAS.md`). Riesgo cerrado.
- ⚠️ **Ambos "pausados" tienen chat activo** (descubierto 08–09 jul): Navaja Suiza (deploy Vercel, ~80%) y Easy Courts (nivel producto, HANDOFF+reporte). El loop **coordina vía sus chats, NO pushea código directo** — como Kiwiano/FitMark. Ya no hay proyecto realmente "en pausa" para avance autónomo.
- 🟡 **Nombre definitivo aparcado** — deadline dura 15-ago (antes del lanzamiento público).
- ✅ ~~Kiwiano `Vitrina` pendiente de merge~~ — **RESUELTO 05-jul**: mergeada a main con landing completa. Sprint 1 completado 15 días antes de fecha.
- ✅ ~~Máquina de cobro de Kiwiano~~ — **F5.1 en producción** (pelotas, planes, billing UI, membresía $40 NZD, saldo visible a jugadores, recordatorio de vencimiento). **F5.2 Stripe Checkout codeado y en pruebas** — 🔑 bloqueado por Tavo: crear webhook en Stripe Sandbox + `STRIPE_SECRET_KEY`/`STRIPE_WEBHOOK_SECRET` en Vercel.
- 🟡 Backups automáticos Supabase de Kiwiano (F1.6) siguen pendientes (vence **20-jul**, 9 días).
- 🟠 **Cero analytics en todos los productos** — sin datos de usuarios no hay buenas decisiones de negocio.
- 🟡 **Nombre de FitMark sin cerrar** — riesgo de seguir construyendo marca/copy sobre un nombre que se va a cambiar (deadline 15-ago).
- ✅ **Wallace KB confirmado a salvo (11-jul)**: el HANDOFF de FitMark reporta que al rescatar el KB antes de borrar `features-review`, resultó estar **YA idéntico en main** — no se perdió nada. Cierra el cabo suelto de la decisión del 08-jul.
- 📌 **Coincidencia sin coordinar (11-jul)**: Kiwiano y FitMark construyeron **la misma semana** una función de "compartir para RRSS" (tarjetas/imágenes de resultados) en sus chats independientes — sin que la torre lo sugiriera. Señal de que ambos equipos convergen en la misma prioridad de distribución/growth por su cuenta.
- ⚠️ **HANDOFF desactualizado en Kiwiano y FitMark**: ambos narran una "última sesión" varios días más vieja que sus commits reales en `main`. No es grave (git sigue siendo la fuente de verdad y el loop lo lee), pero el bloque "Torre de control" de esos HANDOFF no refleja el trabajo más reciente — si a alguno de los dos chats de dev le sirve, conviene que lo actualicen al cerrar.

## Definición de "comercializable" (checklist por producto)

- [ ] Landing pública con propuesta de valor clara
- [ ] Onboarding self-service (sin intervención manual)
- [ ] Flujo de cobro real (Stripe / Transbank / Mercado Pago)
- [ ] Analytics de uso (eventos clave + funnel)
- [ ] Términos de servicio + privacidad
- [ ] Soporte/contacto y monitoreo de errores
