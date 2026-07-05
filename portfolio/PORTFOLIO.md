# 📊 Portfolio — Dashboard Maestro

> Última actualización: **2026-07-05** · Actualizar en cada sesión de trabajo.

## Estado global

| Proyecto | Fase | Avance | ¿Comercializable hoy? | Bloqueador principal | Próximo hito | Deadline |
|---|---|---|---|---|---|---|
| **Kiwiano** | ✅ F4 completada (Vitrina mergeada 05-jul, 15 días antes) → F5 | 🟢 Alto — **activo, en otro chat** | Casi — landing pública LISTA, falta cobro | Sin monetización aún (F5 recién parte) | F5 Stripe: saldo de pelotas + membresía | **2026-08-10** (fecha del chat de dev) |
| **FitMark** (nombre por definir) | Carrera al lanzamiento (85%) — funcional de punta a punta y auditada | 🟢 Alto — **activo, en otro chat** | Casi — falta definir free vs premium | Nombre definitivo pendiente (deadline dura 15-ago) | Definir free vs premium | 🎯 Lanzamiento gratis **2026-08-31** |
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

- 🔴 **Ningún proyecto genera ingresos aún** — prioridad absoluta: primer flujo de cobro real (Kiwiano F5).
- 🔴 **Carrera con fierro.app**: competidor directo pero incompleto (sin pagos, librería 404, rutinas flojas — verificado por Gustavo 05-jul). Decisión: FitMark sale primero — lanzamiento público adelantado a **fin de agosto**. Vigilar fierro.app semanalmente.
- 🟠 **Contenido en redes parte esta semana** (ver `CONTENIDO.md`) — construir audiencia antes del lanzamiento; sin distribución no hay carrera que ganar.
- 🟡 **`features-review` de FitMark**: rescate selectivo de lo útil y descartar la rama (decidido 05-jul; ejecutar en julio).
- 🟡 **Nombre definitivo aparcado** — deadline dura 15-ago (antes del lanzamiento público).
- ✅ ~~Kiwiano `Vitrina` pendiente de merge~~ — **RESUELTO 05-jul**: mergeada a main con landing completa (3 hooks, precios en pelotas, mocks bilingües). Sprint 1 completado 15 días antes de fecha.
- 🟡 Backups automáticos Supabase de Kiwiano (F1.6) siguen pendientes — era la otra tarea del Sprint 1 (vence 20-jul).
- 🟠 **Cero analytics en todos los productos** — sin datos de usuarios no hay buenas decisiones de negocio.
- 🟡 Backups manuales de Supabase en Kiwiano (F1.6 pendiente).
- 🟡 **Nombre de Biohack AI sin cerrar** — riesgo de seguir construyendo marca/copy sobre un nombre que se va a cambiar.

## Definición de "comercializable" (checklist por producto)

- [ ] Landing pública con propuesta de valor clara
- [ ] Onboarding self-service (sin intervención manual)
- [ ] Flujo de cobro real (Stripe / Transbank / Mercado Pago)
- [ ] Analytics de uso (eventos clave + funnel)
- [ ] Términos de servicio + privacidad
- [ ] Soporte/contacto y monitoreo de errores
