# Navaja Suiza (repo: La-Suiza) — Ficha de proyecto

> Actualizado: 2026-07-05

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

## Rol en el portfolio

**Proyecto personal / vitrina. NO comercial por ahora.** Es la herramienta propia de
Gustavo y demo de habilidades. Regla: no invertir tokens salvo mantenimiento o uso
personal real. Reevaluar como producto (nicho WHV backpackers) en 2027 si los otros
tres ya generan ingresos.
