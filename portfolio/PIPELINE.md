# 🗓️ Pipeline y Deadlines

> Plan propuesto el 2026-07-05. Las fechas son compromisos, no deseos —
> si una fecha se mueve, se anota el motivo en el registro de sesiones.

## Principio rector

**Un solo proyecto "activo" por sprint.** Los demás quedan en mantenimiento
(solo bugs críticos). Cada sprint termina con algo demostrable/vendible.

## Q3 2026 (jul–sep): Kiwiano a la venta + FitMark medible

### Sprint 1 — Kiwiano vitrina (2026-07-06 → 2026-07-20)
- [ ] Rescatar/mergear rama Vitrina: F4.1 landing pública, F4.2 home rediseñado, F4.3 modo TV
- [ ] Backups automáticos Supabase (F1.6)
- **Entregable**: kiwiano con landing pública navegable.

### Sprint 2 — Kiwiano monetización F5 (2026-07-21 → 2026-08-15)
- [ ] Stripe + planes Free / Club / Pro
- [ ] Onboarding self-service para clubes (hoy es solo superadmin)
- [ ] Analytics básico (eventos: registro club, torneo creado, upgrade)
- **Entregable**: 🎯 **primer producto cobrable del portfolio** (beta comercial 15-ago).

### Sprint 3 — Kiwiano primeros clientes (2026-08-16 → 2026-08-31)
- [ ] Piloto con 2–3 clubes reales (NZ y/o Chile)
- [ ] Términos de servicio + privacidad
- [ ] Plan de publicidad inicial (Instagram pádel, grupos WhatsApp de clubes)

### Sprint 4 — FitMark pre-monetización (2026-09-01 → 2026-09-30)
- [ ] Analytics (PostHog o Vercel Analytics) + funnel de onboarding
- [ ] Rate-limit `/api/chat` (Upstash) — controla el costo de Wallace
- [ ] Rescatar rama `features-review` (resolver colisión de migración 003)
- [ ] Definir modelo de precios (freemium: Wallace + logros premium)

## Q4 2026 (oct–dic): FitMark cobra + Easy Courts se vuelve real

### Sprint 5 — FitMark monetización (2026-10-01 → 2026-10-31)
- [ ] Stripe subscripciones + paywall de features premium
- [ ] Conectar Wallace KB RAG (262 artículos) como feature premium

### Sprint 6–7 — Easy Courts Etapa 1 (2026-11-01 → 2026-12-15)
- [ ] Postgres real + conectar Prisma (schema ya existe, 20 modelos)
- [ ] Auth real (Auth.js/Supabase) + protección server-side de `/admin`
- [ ] Mutaciones persistentes (reservas, partidas)
- **Entregable**: demo vendible a un club piloto (dic 2026 / ene 2027).

## Reglas de la pipeline

1. No se empieza un sprint nuevo sin cerrar (o cancelar explícitamente) el anterior.
2. Toda sesión de Claude se registra en `metricas/sesiones.csv` (proyecto, avance, tokens/costo).
3. Revisión semanal del dashboard (`PORTFOLIO.md`): actualizar avance, riesgos y fechas.
4. Ideas nuevas van a `IDEAS.md` — no interrumpen el sprint activo.
