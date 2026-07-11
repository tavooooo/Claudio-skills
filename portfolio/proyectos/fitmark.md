# FitMark / Biohack AI — Ficha de proyecto

> Actualizado: 2026-07-05
> **Nombre en transición**: Gustavo está evaluando renombrar el producto a
> "Biohack AI", pero no lo convence del todo. FitMark sigue siendo el nombre
> del repo/código. Ver `IDEAS.md` para el brainstorm de nombres.

**Qué es**: tracker de entrenamiento de fuerza mobile-first (iPhone-first). Registro de
sesiones y PRs, rutinas, base de 152 ejercicios, mapa muscular SVG/3D interactivo,
logros, y **Wallace**, coach IA (Claude API). En español. Deploy: Vercel (auto en `main`).

**Stack**: Next.js 16.2 · React 19 · Tailwind 4 · Zustand + Zod · GSAP/three.js/recharts
· Supabase (Postgres + Auth con Google OAuth, RLS verificada) · Prisma · Vitest (32 tests) + Playwright.

## Estado (actualizado 2026-07-11 por el loop, desde git main — 91% su propio número;
   HANDOFF narra hasta 08-jul, desactualizado vs. los commits reales)

- ✅ **11-jul — tarjetas de "Compartir" para RRSS**: exportar la sesión/día como imagen
  (story). Serie larga de fixes específicos de iOS (skipFonts en html-to-image por hang
  de Safari, achicar imágenes musculares embebidas antes de capturar, ajustar layout de la
  tarjeta). Mismo tipo de feature que Kiwiano construyó la misma semana, sin coordinación.
- ✅ **08-jul (tarde) — Wallace fundamentado en la KB**: las rutinas ahora explican el
  porqué citando la fuente del artículo + **auto-crecimiento de la KB**: registra en
  `kb_gaps` los temas que la gente pregunta y no están (detector servidor + detector
  Wallace), con panel admin para resolver. Wallace: 1 intento por proveedor, cae a Groq.
  Medallas derivadas de récords (antes NUNCA se escribían). KB de `features-review`
  **confirmado idéntico en main** al rescatarlo — no se perdió nada al borrar la rama.
- ✅ **10-jul — app BILINGÜE ES/EN completa**: i18n en toda la app (núcleo, ejercicios,
  rutinas, tracker, coach, landing, auth) + selector de idioma + **catálogo 152/152
  ejercicios traducido**. Amplía el mercado direccionable (no solo hispanohablantes).
  Hecho con **orquestación multi-agente** (los commits marcan "agentes en curso").

- ✅ **08-jul**: **íconos musculares en toda la app** (MuscleIcon/RoutineMuscleIcon desde
  los trazados reales del mapa, fuente única `lib/data/musclePaths.ts`; precisión por porción
  con el código de color del mapa) · **calendario con vista semanal nueva** + íconos en las
  celdas · modal de rutina rehecho (una página, pantalla completa en móvil) · renombrar
  sesiones (sobre todo las libres) · **medallas retroactivas** (antes nunca aparecían;
  "Logros"→"Medallas") · Wallace con **fallback de proveedor** (Gemini→Groq) · varios fixes
  responsive (progreso y chat ya no se ensanchan en el teléfono).
- ✅ **07-jul**: Wallace conversacional (burbujas separadas, typeo ~26cps), tarjetas de
  ejercicio colapsables + **reordenar unificado** (handle ⋮⋮ móvil, drag nativo PC), y
  **auditoría de rendimiento**: queries en paralelo, auth cacheada, skeletons.

- ✅ Núcleo maduro: tracker, rutinas, ejercicios, mapa muscular, coach IA, landing con scroll-video, onboarding progresivo.
- ✅ **05-jul**: PRs con celebración de récords, plantillas de rutina y peso corporal,
  guía de primeros pasos, admin de usuarios, y **QA profundo con 5 auditores paralelos
  (48 hallazgos, ~25 arreglados: bucle de redirects, falsos récords, TZ Chile, seguridad admin)**.
- ✅ **06-jul — Freemium 5/5 cableado**: FREE (5 rutinas · 5 ejercicios propios · 10 msgs
  Wallace/mes) vs **PREMIUM $5,99/mes · $39,99/año** con gates en servidor + candados en UI
  + página `/premium`. **El cobro está SIMULADO** (modo prueba para admin) — falta pasarela real.
- ✅ **06-jul — Tanda UX**: coma decimal en inputs de peso, reordenar ejercicios/rutinas con flechas, calendario pulido.
- ✅ **06-jul — Wallace 2.0**: datos reales del usuario, avatar-cara, chat premium y presencia en sesión.
- 🎯 Próximo hito: **pasarela de pago REAL** (hoy simulada) + cerrar nombre definitivo (15-ago).
- 🟡 `/logros` "en construcción"; `/store` es solo vitrina visual (sin checkout).
- ✅ **Rama `claude/features-review` — DECISIÓN FINAL (08-jul): se DESCARTA y se reconstruye
  desde cero en main.** A 129 commits de divergencia el rescate salía más caro que rehacer limpio.
  **A reconstruir** (lo que había en la rama): ranking · red social/feed · planes · cuentas
  gym/coach · chat. ⚠️ **Salvar antes de borrar**: `wallace-kb/` (262 artículos = contenido,
  no código; `wallace-wiki.wkml` ~550KB + `indice-wallace.html`) — exportarlo evita reescribir
  los artículos. Ejecuta el chat de dev de FitMark (borrar rama + salvar KB).
- 🟡 Wallace KB RAG (`wallace-kb/`, 262 artículos) sin conectar (vive en features-review).
- ❌ **Analytics: nada.**

## Brechas para comercializar

1. Analytics + funnel (¿la gente termina el onboarding? ¿usa Wallace?).
2. Rate-limit `/api/chat` (Upstash) — sin esto el coach IA es un costo sin techo.
3. ~~Modelo de precios freemium~~ ✅ cableado (06-jul) — falta **pasarela de pago real** (hoy simulada).
4. `ADMIN_EMAILS` en Vercel y quitar fallback hardcodeado en `src/lib/admin.ts`.
5. ~~Reconciliar `features-review`~~ ✅ decidido 08-jul: **descartar y reconstruir desde cero** (ranking, red social, planes, cuentas gym/coach, chat). Salvar el `wallace-kb/` (contenido) antes de borrar la rama.
6. Cerrar nombre definitivo del producto (ver brainstorm en `IDEAS.md`).
7. 🎨 **Ilustraciones de ejercicios con IA local** (tarea anotada 07-jul): avatar consistente
   demostrando los 152 ejercicios, generado en el notebook RTX 16GB de Gustavo con
   FLUX.1-schnell (licencia comercial). Fase 1 = piloto de 5 (instrucción entregada);
   Fase 2 = LoRA del avatar + ControlNet OpenPose → producción. Detalles en `IDEAS.md`.

## Competencia — fierro.app (vigilancia activa)

Investigación de Gustavo (2026-07-05, probando la app directamente):

- **También está en construcción**: sin planes de pago, todo gratis por ahora.
- **Rutinas precargadas flojas**: mal manejo de descansos, explicaciones de
  ejercicios pobres.
- **Librería de ejercicios rota**: da error 404 — no existe todavía.

**Nuestras ventajas hoy**: librería de 152 ejercicios funcionando, mapa muscular
SVG/3D, coach IA (Wallace) operativo, deploy estable en Vercel.

**Implicancia estratégica**: hay una VENTANA — salir públicamente antes de que
fierro complete su producto. La carrera es por la librería + experiencia de
entrenamiento, no por el precio (ellos son gratis). Revisar fierro.app en cada
loop semanal para detectar sus avances.

**Docs internas**: `HANDOFF.md` (actualizado 2026-07-04), `docs/STACK.md`, `AGENTS.md` (reglas UI de contraste y overlays — respetar siempre).
