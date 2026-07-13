# 📊 Portfolio — Dashboard Maestro

> Última actualización: **2026-07-13** · Actualizar en cada sesión de trabajo.

## Estado global

| Proyecto | Fase | Avance | ¿Comercializable hoy? | Bloqueador principal | Próximo hito | Deadline |
|---|---|---|---|---|---|---|
| **Kiwiano** | **~85%** — merge GRANDE "olas 1-5" a main (13-jul, 77 archivos/+9729 líneas): modo TV 2.0, marcador en vivo, cuentas individuales por club + login premium, ligas, fotos, video/transmisión — **todo sin Stripe**, F5.2 sigue sin avance | 🟢 Alto — **activo, en otro chat** ⚠️ HANDOFF (`docs/HANDOFF.md`) desactualizado 6 días (dice 07-07 "F5 80%", git llega a 13-jul con producto muchísimo más avanzado) | Casi — checkout escrito, falta probarlo con claves | **Tavo**: crear webhook en Stripe + pegar `sk_test_`/`whsec_` en Vercel (sin cambios) | Prueba de pago con tarjeta test en preview → merge a main con claves live | **2026-08-10** (fecha del chat de dev) |
| **FitMark** (nombre por definir) | Carrera al lanzamiento (**91%**, su propio número) — 13-jul: botón "Continuar con Google" en login + **Gustavo migró Supabase de Mumbai a Sídney y fijó Vercel en syd1** (baja latencia, hecho por vos mismo con Opus) | 🟢 Alto — **activo, en otro chat** ⚠️ HANDOFF desactualizado (dice 07-08, git llega a 13/14-jul) | Casi — freemium listo con **cobro simulado**, falta pasarela real | Pasarela de pago real + nombre definitivo (15-ago) | Pasarela de pago real | 🎯 Lanzamiento gratis **2026-08-31** |
| **Easy Courts** | Etapa 0 completa (**~55%**, estimado por el loop desde git — su HANDOFF sigue en 60%/09-jul) — **chat ACTIVO**: landing premium con parallax de pelotas + selector de idioma (13-jul), i18n ES/EN completo (12-jul), reporta tokens de nuevo | 🟡 Medio — activo | No — todo mock, nada persiste | Necesita que Tavo provea Supabase (`DATABASE_URL`) + claves Stripe; Prisma no genera en sandbox | Etapa 1: conectar DB + auth real + deploy piloto | 2026-12-15 |
| **Navaja Suiza** | **~80% (su propio número, HANDOFF fresco)** — **divisor de gastos colaborativo CODEADO Y LISTO** (12-jul: link de invitación + login magic-link + realtime), inerte hasta activar Supabase — sin cambios esta sesión | 🟡 Medio — activo, apuesta #3 | Casi — todo el código está, falta un solo paso tuyo | **Vos**: crear proyecto Supabase + correr `schema.sql` + pegar claves | Activar Supabase → enciende login + divisor compartido de una sola vez | este mes (baja) |

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
- ⚠️ **HANDOFF desactualizado — patrón que se repite**: Kiwiano, FitMark y ahora también Easy Courts narran una "última sesión" varios días más vieja que sus commits reales (Padel incluso tiene un commit "docs: HANDOFF..." que no tocó el archivo). No es grave — git sigue siendo la fuente de verdad y el loop lo lee — pero ya son 3 de 5 repos con el mismo síntoma.
- 🎉 **Navaja Suiza: divisor de gastos COLABORATIVO shippeado (12-jul)** — link de invitación, login por magic-link, esquema RLS por membresía, vista compartida en tiempo real. Está **codeado y verificado, solo inerte** hasta que Gustavo active Supabase (crear proyecto + correr `schema.sql` + pegar claves). Resuelve de una sola vez las tareas #13 y #14 del tablero (se consolidan).
- 📌 **Segunda coincidencia sin coordinar**: Easy Courts (12-jul) completó i18n ES/EN, el mismo tipo de trabajo que FitMark hizo el 10-jul. Dos proyectos distintos llegando a la misma prioridad de "abrir el mercado angloparlante" por su cuenta.
- ✅ **Easy Courts reporta tokens por primera vez (12-jul)**: con esto el panel de costos ya tiene datos de los 4 proyectos activos. Kiwiano y FitMark siguen con su cifra de hace varios días (07-07/07-08) — no incluyeron el CSV en sus cierres más recientes.
- 🚀 **Kiwiano dio un salto grande sin avisar en el HANDOFF (13-jul)**: merge "olas 1-5" — 77 archivos, +9729 líneas. Cuentas por club + login premium, ligas, marcador en vivo, modo TV 2.0, fotos, video/transmisión. El F8 "Plan Pro" que el HANDOFF describía como planificado ya está en producción en gran parte — el HANDOFF sigue anclado en el mundo de "F5 80%, Stripe en pruebas" de hace 6 días. Además hay una rama activa aparte (`claude/handoff-premium-roadmap-0ojicp`) con cámara en vivo por WebRTC — trabajo de streaming que la pipeline daba por "diferido post-monetización" y ya está en curso.
- ✅ **Gustavo resolvió solo la tarea de latencia de FitMark (13-jul)**: migró la BBDD de Supabase de Mumbai a Sídney y fijó las funciones de Vercel en `syd1` — commit directo suyo con Opus 4.8, sin pasar por el chat de dev. Tarea #`fm-region-check` del tablero, cerrada. Sacada del tablero por el loop.
- 📌 **Tercera coincidencia de trabajo paralelo sin coordinar**: Easy Courts sumó parallax + selector de idioma en su landing (13-jul), el mismo tipo de pulido visual que FitMark y Kiwiano vienen haciendo cada uno en su carril — refuerza el patrón de que los 3 equipos convergen en "landing vendedora" al mismo tiempo sin que la torre lo esté empujando.

## Definición de "comercializable" (checklist por producto)

- [ ] Landing pública con propuesta de valor clara
- [ ] Onboarding self-service (sin intervención manual)
- [ ] Flujo de cobro real (Stripe / Transbank / Mercado Pago)
- [ ] Analytics de uso (eventos clave + funnel)
- [ ] Términos de servicio + privacidad
- [ ] Soporte/contacto y monitoreo de errores
