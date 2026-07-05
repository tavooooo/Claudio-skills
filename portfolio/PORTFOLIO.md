# 📊 Portfolio — Dashboard Maestro

> Última actualización: **2026-07-05** · Actualizar en cada sesión de trabajo.

## Estado global

| Proyecto | Fase | Avance | ¿Comercializable hoy? | Bloqueador principal | Próximo hito | Deadline |
|---|---|---|---|---|---|---|
| **Kiwiano** | F4 "UI vendible" (~70%) | 🟢 Alto | Casi — falta landing + cobro | Sin monetización (F5 Stripe sin empezar); landing/home/TV en rama Vitrina sin mergear | Mergear Vitrina + landing pública | 2026-07-20 |
| **FitMark** | Producto maduro, pre-monetización | 🟢 Alto | No — sin pagos ni analytics | Sin Stripe, sin analytics, rama `features-review` pausada | Analytics + rate-limit chat + plan de precios | 2026-08-31 |
| **Easy Courts** | Etapa 0 (demo mock completa) | 🟡 Medio | No — nada persiste | Todo es mock: sin DB real, sin auth real, admin sin protección | Etapa 1: Postgres + Prisma + auth real | 2026-10-15 |
| **Navaja Suiza** | Fase 1 completa (local-only) | 🟢 Alto | N/A (personal) | Sin nube (Supabase scaffolded, inactivo) | Mantener; evaluar comercializar en 2027 | — |

## Orden de la pipeline (foco secuencial, no picotear)

1. **Kiwiano** → es el más cerca de venderse: F1–F3 listas, solo falta vitrina + Stripe.
2. **FitMark** → producto sólido con deploy en Vercel; necesita monetización y datos de uso.
3. **Easy Courts** → mayor potencial de ticket (B2B clubes) pero le falta una fase entera de integración.
4. **Navaja Suiza** → congelado como proyecto personal; no invertir tokens salvo mantenimiento.

## Semáforo de riesgos

- 🔴 **Ningún proyecto genera ingresos aún** — prioridad absoluta: primer flujo de cobro real (Kiwiano F5).
- 🟠 **Ramas huérfanas con trabajo valioso**: Kiwiano `Vitrina` (landing/TV), FitMark `features-review` (ranking, social, planes) — rescatar antes de que se pudran.
- 🟠 **Cero analytics en todos los productos** — sin datos de usuarios no hay buenas decisiones de negocio.
- 🟡 Backups manuales de Supabase en Kiwiano (F1.6 pendiente).

## Definición de "comercializable" (checklist por producto)

- [ ] Landing pública con propuesta de valor clara
- [ ] Onboarding self-service (sin intervención manual)
- [ ] Flujo de cobro real (Stripe / Transbank / Mercado Pago)
- [ ] Analytics de uso (eventos clave + funnel)
- [ ] Términos de servicio + privacidad
- [ ] Soporte/contacto y monitoreo de errores
