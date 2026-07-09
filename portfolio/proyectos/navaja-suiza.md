# Navaja Suiza (repo: La-Suiza) — Ficha de proyecto

> Actualizado: 2026-07-08

**Qué es**: PWA personal con ~15 mini-apps para la vida diaria de mochileros en
working holiday (Canadá, Australia, NZ): finanzas, conversor, inversiones, divisor de
gastos, agenda, supermercado, comidas, recetario, metas, hábitos, diario, documentos
(con OCR), viajes, idiomas (repetición espaciada). Single-user por diseño (Fase 1).

**Stack**: Next.js 15.5 · React 19 · Tailwind 3.4 · **Dexie/IndexedDB local** tras una
abstracción `Repository<T>` · Supabase scaffolded pero inactivo · Tesseract.js (OCR)
· Leaflet · Recharts · GSAP · Vitest (6 módulos de dominio testeados).

## Estado

- ✅ Funcionalmente completa en almacenamiento local; sin TODOs bloqueantes; UX pulida (WCAG, GSAP).
- ✅ Schema SQL completo con RLS listo (`supabase/schema.sql`, 26 tablas).
- 🟡 Pendiente de nube (4 pasos del README): crear proyecto Supabase + schema, login UI + protección de rutas, migrar `useLiveQuery` a realtime, mover imágenes a Storage.

## Rol en el portfolio — CAMBIO 2026-07-08

**Gustavo decide adelantar la evaluación comercial.** Deja de ser "congelado, cero
tokens" → pasa a **preparación para venta, PRIORIDAD BAJA este mes** (sin robar foco a
Kiwiano ni FitMark, que son la #1 y #2). La regla de cero tokens se relaja: se permite
invertir en la pista comercial, con moderación.

- **Cambios a hacer para venta**: inicio de sesión (auth) + subir a la nube (Supabase,
  ya scaffoldeado) + el divisor de gastos colaborativo (ver abajo).

## Gancho comercial: el DIVISOR DE GASTOS (hallazgo 2026-07-08)

Revisado el código: el **motor de división ya está completo y testeado** (`lib/domain/settle.ts`):
- Cada gasto tiene `payerId` (quién pagó) + `participants` (quiénes participan — subconjunto
  seleccionable, no siempre todos) → cubre "una cosa la paga uno, otra otro".
- 3 modos: partes iguales · por peso/porcentaje · montos exactos.
- `computeBalances` (balance neto por persona) + `settle` (transferencias mínimas para
  saldar) — estilo Splitwise. Con tests.

**Lo que FALTA (el trabajo nuevo = capa colaborativa):**
1. Auth / cuentas (inicio de sesión).
2. **Link de invitación** para agregar participantes a un viaje.
3. Viaje/gasto **compartido multi-usuario** (cada uno se loguea y ve/agrega gastos).
4. Sync en la nube (Supabase pasa de scaffolded a activo; realtime).
5. (UI) exponer la selección de participantes por gasto si hoy solo muestra "partes iguales".

**Nicho (eval 08-jul)**: el divisor es el mejor gancho, más que la super-app entera.
Splitwise se volvió tacaño (paywalls) → hay demanda de alternativa. Dolor universal
(roommates, parejas, viajes), con los mochileros WHV como punta de entrada afilada.
Competencia real (Splitwise, Tricount, Splid): se gana por UX + gratis + integración
con la super-app para el segmento WHV. Apuesta #3 del portfolio, no #1.
