# Navaja Suiza (repo: La-Suiza) — Ficha de proyecto

> Actualizado: 2026-07-12 (HANDOFF propio fresco, mismo día)

**Qué es**: PWA personal con ~15 mini-apps para la vida diaria de mochileros en
working holiday (Canadá, Australia, NZ): finanzas, conversor, inversiones, divisor de
gastos, agenda, supermercado, comidas, recetario, metas, hábitos, diario, documentos
(con OCR), viajes, idiomas (repetición espaciada). Single-user por diseño (Fase 1).

**Stack**: Next.js 15.5 · React 19 · Tailwind 3.4 · **Dexie/IndexedDB local** tras una
abstracción `Repository<T>` · Supabase scaffolded pero inactivo · Tesseract.js (OCR)
· Leaflet · Recharts · GSAP · Vitest (6 módulos de dominio testeados).

## Estado (git al 2026-07-09)

- 🟢 **TIENE CHAT ACTIVO** (descubierto por el loop 08-jul): no está dormido. El 09-jul
  pushearon **deploy en Vercel** (`la-suiza.vercel.app`) + **upgrade visual premium**
  (transiciones de ruta, hero animado, glows, nav activa) + auditoría funcional. HANDOFF
  propio al día con reporte de tokens ya configurado. Se declaran **~80%**.
- ✅ Funcionalmente completa en local (IndexedDB/Dexie); UX pulida (WCAG, GSAP).
- ✅ Schema SQL completo con RLS listo (`supabase/schema.sql`).
- 🟡 **Próximo hito (su HANDOFF)**: conectar Supabase (BBDD) + Login — requiere que Gustavo
  cree el proyecto Supabase y provea URL + anon key. Luego migrar `useLiveQuery` a realtime.
- ⚠️ **Ramas**: la app vive en `claude/github-skills-import-4xhew4` (default/Vercel); el
  tracking de la torre se fusiona a `claude/project-portfolio-tracking-ib0574`. **El loop NO
  debe pushear código directo** — coordina vía el chat activo (como Kiwiano/FitMark), o el
  cambio no se despliega y su merge lo pisa.

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

## 🎉 Capa colaborativa CODEADA (12-jul) — solo falta activar Supabase

El chat de dev construyó TODO lo que faltaba, verificado (local OK, 0 errores JS):
1. ✅ **Login sin contraseña** (magic link, `signInWithOtp`) — `app/login`.
2. ✅ **Link de invitación**: `app/unir/[token]` — el amigo abre el link, se loguea y
   se une al grupo automáticamente.
3. ✅ **Vista compartida en tiempo real** (`CloudDivisor.tsx`): grupo compartido,
   gastos, neteo, realtime — conmuta sola a modo compartido si hay Supabase + sesión;
   el modo local sigue intacto si no.
4. ✅ **Esquema RLS por membresía** en `supabase/schema.sql`: cualquier miembro del
   grupo lee/escribe, nadie ve grupos ajenos (`is_group_member()`, `join_group_by_token()`).
5. 🔑 **Todo queda INERTE hasta activar Supabase** — el único paso que falta es tuyo:
   crear el proyecto en supabase.com, correr `schema.sql`, pegar las claves
   (`NEXT_PUBLIC_SUPABASE_URL`/`ANON_KEY`) y activar el proveedor de email (magic link).
   Un solo paso enciende login + divisor compartido a la vez.
6. ⏳ **Pendiente real, no resuelto por esto**: la UI de "nuevo gasto" TODAVÍA no deja
   elegir quiénes participan (sigue dividiendo entre todos por defecto) — es una mejora
   de UI aparte, chica, que puede ir después de activar Supabase.

**Nicho (eval 08-jul)**: el divisor es el mejor gancho, más que la super-app entera.
Splitwise se volvió tacaño (paywalls) → hay demanda de alternativa. Dolor universal
(roommates, parejas, viajes), con los mochileros WHV como punta de entrada afilada.
Competencia real (Splitwise, Tricount, Splid): se gana por UX + gratis + integración
con la super-app para el segmento WHV. Apuesta #3 del portfolio, no #1.
