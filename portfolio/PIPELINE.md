# 🗓️ Pipeline y Deadlines

> Plan propuesto el 2026-07-05. Las fechas son compromisos, no deseos —
> si una fecha se mueve, se anota el motivo en el registro de sesiones.

## Principio rector

**Un solo proyecto "activo" por sprint.** Los demás quedan en mantenimiento
(solo bugs críticos). Cada sprint termina con algo demostrable/vendible.

> **Realidad al 2026-07-05**: Gustavo trabaja Kiwiano y Biohack AI en paralelo,
> cada uno en su propio chat. La pipeline sigue marcando el ORDEN DE PRIORIDAD
> (qué se cierra primero, qué espera), no una prohibición de tocar dos cosas a
> la vez. Esta sesión (torre de control) no desarrolla ninguno de los dos —
> coordina fechas, riesgos y costos entre ambos.

## Q3 2026 (jul–sep): Kiwiano a la venta + FitMark medible

### Sprint 1 — Kiwiano vitrina (2026-07-06 → 2026-07-20)
- [x] ✅ Rescatar/mergear rama Vitrina — **HECHO 05-jul, 15 días antes** (landing con 3 hooks, precios en pelotas, mocks bilingües, story real)
- [ ] Backups automáticos Supabase (F1.6) — única tarea restante del sprint
- **Entregable**: kiwiano con landing pública navegable. ✅ CUMPLIDO

### Sprint 2 — Kiwiano monetización F5 (adelantado: ya en curso → 2026-08-10, fecha fijada por el chat de dev)
- [x] ✅ **F5.1 mergeada 06-jul, EN PRODUCCIÓN**: sistema de pelotas + planes + billing UI + panel de cobros + membresía $40 NZD + saldo visible a jugadores + recordatorio de vencimiento
- [ ] **F5.2 Stripe Checkout** — ✍️ codeado (07-jul) y en pruebas en Vitrina · 🔑 **bloqueado por Tavo**: crear webhook en Stripe + pegar `sk_test_`/`whsec_` en Vercel → probar pago test → merge con claves live
- [ ] Onboarding self-service para clubes (hoy es solo superadmin)
- [ ] Analytics básico (eventos: registro club, torneo creado, upgrade)
- **Entregable**: 🎯 **primer producto cobrable del portfolio** (beta comercial 15-ago). Máquina de cobro ✅ construida; falta go-live de Stripe.

### F7 Kiwiano "En Vivo" (planificado 08-jul — roadmap proyectado por Tavo)
Orden de prioridad real tras F5.2: **F5.2 → F7.1 → F7.2 → F7.3 → F6** (F6 Crecimiento es continuo, por eso va al final).
- [ ] **F7.1 Marcador en vivo** — puntaje punto a punto editable desde fuera de la cancha, en vivo en modo TV, alimenta el ranking. Riesgo BAJO. Candidato a ir **justo después de F5.2** (en los torneos ya se juega con puntos/sets, solo falta anotarlos).
- [ ] **F7.2 Streaming del partido** — cámara→WHIP→Cloudflare Stream, plan Pro/créditos. Riesgo MEDIO (costo). **DIFERIDO a post-monetización** ("cuando ya estemos generando").
- [ ] **F7.3** — (ver HANDOFF de Kiwiano). Diferido.

### Sprint 3 — Kiwiano primeros clientes (2026-08-16 → 2026-08-31)
- [ ] Piloto con 2–3 clubes reales (NZ y/o Chile)
- [ ] Términos de servicio + privacidad
- [ ] Plan de publicidad inicial (Instagram pádel, grupos WhatsApp de clubes)

### ⚡ Carrera FitMark (jul–ago, EN PARALELO a los sprints Kiwiano — se trabaja en su propio chat)

> Ajuste 2026-07-05: fierro.app (competencia directa) está incompleta — sin pagos,
> librería 404, rutinas flojas. Decisión de Gustavo: **salir primero**. El lanzamiento
> público de FitMark se adelanta de sept a **agosto**, y el contenido en redes parte YA.

- [x] ✅ **`features-review` DECIDIDO (08-jul): descartar y reconstruir desde cero** — a 129 commits de divergencia, rehacer limpio < cherry-pick. Reconstruir en main: ranking, red social/feed, planes, cuentas gym/coach, chat. Salvar `wallace-kb/` (contenido, no código) antes de borrar. Lo ejecuta el chat de dev de FitMark.
- [ ] Analytics (PostHog o Vercel Analytics) + rate-limit `/api/chat` (Upstash) — jul
- [x] ✅ **Definir feature-set + freemium (06-jul)**: FREE 5/5/10 vs PREMIUM $5,99/mes cableado con cobro simulado; falta pasarela real
- [ ] Pasarela de pago real para el freemium (hoy simulado) — antes del lanzamiento
- [ ] 🎨 **Ilustraciones de ejercicios con IA local** (notebook RTX 16GB de Gustavo, confirmada): Fase 1 = ComfyUI + FLUX.1-schnell + piloto de 5 ejercicios (instrucción ya entregada, ver `IDEAS.md`) → Fase 2 = LoRA del avatar + ControlNet → producción de las 152 (~2 poses c/u). Licencia comercial limpia (Apache 2.0) — jul-ago, no bloquea el lanzamiento
- [ ] Contenido en redes desde la semana del 06-jul (ver `CONTENIDO.md`) — continuo
- [ ] 🎯 **Lanzamiento público (gratis) — fin de agosto**, antes de que fierro complete su app
- [ ] Nombre definitivo: aparcado, decidir antes del lanzamiento (deadline dura: 15-ago)

### Sprint 4 — FitMark monetización temprana (2026-09-01 → 2026-09-30)
- [ ] Modelo de precios freemium (Wallace + features premium) — la competencia es
      gratis: monetizar por VALOR (coach IA, librería, mapa muscular), no por básicos
- [ ] Stripe subscripciones

## Q4 2026 (oct–dic): FitMark cobra + Easy Courts se vuelve real

### Sprint 5 — FitMark monetización (2026-10-01 → 2026-10-31)
- [ ] Stripe subscripciones + paywall de features premium
- [ ] Conectar Wallace KB RAG (262 artículos) como feature premium

### Sprint 6–7 — Easy Courts Etapa 1 (2026-11-01 → 2026-12-15)
- [ ] Postgres real + conectar Prisma (schema ya existe, 20 modelos)
- [ ] Auth real (Auth.js/Supabase) + protección server-side de `/admin`
- [ ] Mutaciones persistentes (reservas, partidas)
- **Entregable**: demo vendible a un club piloto (dic 2026 / ene 2027).

### 🧭 Navaja Suiza → pista comercial (nuevo 08-jul, PRIORIDAD BAJA · este mes, sin robar foco)
> Gustavo descongela Navaja Suiza y adelanta la evaluación comercial. Apuesta #3.
- [x] ✅ Nicho evaluado (08-jul): el **divisor de gastos** es el mejor gancho (Splitwise se volvió tacaño; dolor universal; WHV como punta de entrada). Motor de división YA completo y testeado.
- [x] ✅ **Divisor colaborativo CODEADO (12-jul)**: login magic-link + link de invitación + vista compartida realtime + RLS por membresía. Verificado localmente. **Inerte hasta activar Supabase** (🔑 único paso pendiente, es de Gustavo).
- [ ] 🔑 **Gustavo: activar Supabase** — crear proyecto, correr `schema.sql`, pegar claves, activar proveedor de email. Enciende login + divisor compartido de una vez.
- [ ] (menor) UI: elegir participantes por gasto (hoy divide entre todos por defecto).
- **Regla**: avances pequeños y testeados; NO desplaza a Kiwiano ni FitMark. El loop puede ir chipeando piezas verificadas en la rama de La-Suiza.

## Reglas de la pipeline

1. No se empieza un sprint nuevo sin cerrar (o cancelar explícitamente) el anterior.
2. Toda sesión de Claude se registra en `metricas/sesiones.csv` (proyecto, avance, tokens/costo).
3. Revisión semanal del dashboard (`PORTFOLIO.md`): actualizar avance, riesgos y fechas.
4. Ideas nuevas van a `IDEAS.md` — no interrumpen el sprint activo.
