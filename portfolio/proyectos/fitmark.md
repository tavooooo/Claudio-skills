# FitBook (ex-FitMark) — Ficha de proyecto

> Actualizado: 2026-07-17
> **Nombre DEFINITIVO decidido (17-jul): FitBook.** Rebrand a fondo (52 archivos:
> toda la i18n, logo `FitBookLogo`, Wallace = "coach de FitBook"). Cierra el debate
> de nombres (antes se barajó "Biohack AI"). ⚠️ El **repo sigue llamándose `fitmark`**
> y la var interna de la torre es `--fitmark`; el PRODUCTO es FitBook.

**Qué es**: app mobile-first (iPhone-first) de **fitness + nutrición**. Entreno: registro de
sesiones y PRs, rutinas, base de 152 ejercicios (con fotos guía + renders 3D propios en
marcha), mapa muscular SVG/3D, logros. Nutrición: comidas con **foto→calorías**, macros,
calendario. Y **Wallace**, coach IA (Claude API). En español + inglés. Deploy: Vercel (auto en `main`).

**Stack**: Next.js 16.2 · React 19 · Tailwind 4 · Zustand + Zod · GSAP/three.js/recharts
· Supabase (Postgres + Auth con Google OAuth, RLS verificada) · Prisma · Vitest (32 tests) + Playwright.

## Estado (actualizado 2026-07-19 por el loop, desde git main — 95% su propio número)

- 🧠 **19-jul — Wallace con MEMORIA + acceso total a datos (en main)**: el coach IA persiste el
  historial de chat (con retención + borrar conversación) y accede a TODOS los datos del usuario
  con **carga perezosa por pregunta** — encuentra sesiones pasadas y ve los pesos reales por serie.
  Pasa de "chat sin contexto" a coach que conoce al usuario. Mejora directa del valor premium.
- 🎮 **19-jul — 2° render 3D propio**: el peso muerto convencional ya usa render propio (después
  del press de banca), formato JPEG unificado. El reemplazo de fotos de archivo por renders propios
  avanza ejercicio a ejercicio.
- 📱 **19-jul — RED SOCIAL en reconstrucción (rama `vitrina`, aún no en main)**: "Vitrina v2: red
  social fit" — follows, @nicknames, buscador, visibilidad y récords. Es una de las 5 piezas de
  `features-review` que se rehacen desde cero. La rama `vitrina` es de staging (se mergea con main
  regularmente, hoy 15 commits adelante). También: búsqueda tolerante de ejercicios (typos,
  conectores intercambiables, sugerencias).
- 👨‍🏫 **18-jul — CUENTA COACH completa (F1–F6, en main)**: nueva dimensión de producto y de
  ingresos. Un entrenador puede: invitar alumnos (`/join/[code]`, registro vinculado, "Mi coach"),
  ver un dashboard de alumnos con detalle (Resumen/Entreno solo lectura), **asignar rutinas por
  snapshot** (planificación semanal; las asignadas NO ocupan cupo FREE del alumno y quedan
  bloqueadas solo-uso), fijar **metas de nutrición** desde el servidor, hacer **check-ins
  semanales + notas privadas + alertas**, con **frontera de privacidad server-side** (migración
  `006_coach.sql`, `coach_links`) y **plan Coach en `/premium`** (`getCoachTier`). Incluye
  mini-calendario del alumno (tema rojo, solo lectura) reutilizando `CalendarClient`.
- 🏷️ **17-jul — REBRAND FitMark → FitBook (nombre definitivo)**: 52 archivos, toda la i18n +
  logo `FitBookLogo` + Wallace "coach de FitBook". Decidido ~1 mes antes del deadline (15-ago).
  Pendiente derivado: dominio propio de FitBook.
- 🎮 **17-jul — arrancaron los RENDERS 3D PROPIOS**: el press de banca ya sirve renders 3D
  propios (`/images/ejercicios/press-banca-barra/{1,2}.png`, inicio→final) en vez de la foto de
  free-exercise-db. **Inicio real del camino Wallace-3D** — el plan de "fotos gratis de placeholder
  → reemplazo gradual por lo propio" está en marcha, primer ejercicio migrado.
- ✅ **17-jul — freemium en el escáner + Wallace estable**: escáner foto→calorías con límite
  (1/día gratis, Premium ilimitado), macros con meta personalizada por sliders (tolerancia ±5%),
  Wallace sin cuelgues (fallback POR MODELO Gemini→Groq, 3 intentos), timeout que ya no corta el stream.
- ✅ **16-jul — FOTOS GUÍA + COMIDAS MERGEADAS A MAIN** (venían de rama):
  - **Fotos guía (tarea preparada por la torre)**: `src/lib/data/exerciseGuideImages.ts` (mapa
    `slug → fedb_id`, fotos por URL cruda de GitHub) + componente `ExerciseGuideImage.tsx` en ficha
    y tarjetas, con badge de "guía visual" en el listado. Auditoría visual en 2 fases (incluyó
    revisar los 20 "PROBABLE" que marcó la torre y corregir fotos que compartían imagen con otro
    movimiento) → **127/152 ejercicios con foto verificada** en main, 25 a la cola de Wallace 3D.
    Licencia limpia (free-exercise-db = Unlicense). Landing con card de foto guía real (press de banca).
  - **COMIDAS foto→calorías (MVP)**: escaneo de foto → estimación de calorías/macros con **visión
    Gemini nativa → Groq (Llama 4 Scout / Qwen) de respaldo**, biblioteca de alimentos, macros con
    anillos, **calendario unificado Entreno/Nutrición en `/tracker`** (toggle, donas, compartir
    tarjeta), persistido en Supabase (migración `005_meals.sql`). El producto ya es **fitness +
    nutrición**, no solo fuerza.
- ✅ **13-jul — Gustavo migró Supabase de Mumbai a Sídney** (`ap-south-1` → `ap-southeast-2`)
  y fijó las funciones de Vercel en `syd1` para minimizar la latencia app↔DB. Commit propio
  (no del chat de dev), hecho con Opus 4.8. Resuelve la tarea "verificar misma región
  Vercel/Supabase" del tablero de la torre — sacada de la lista.
- ✅ **13-jul — botón "Continuar con Google" visible en `/login`**.
- ✅ **12-jul — LANDING REHECHA de punta a punta**: reescribieron la landing pública
  entera (`ScrollVideoLanding`) para reflejar lo que la app hace HOY (antes tenía
  copy/promesas viejas) — mantiene la estética sci-fi neon (video hero, **holograma de
  Wallace**, glitch titles) pero cada claim ahora es real: hero con la promesa de
  entrenar/loguear/romper récords, franja de datos duros con contadores (152+ ejercicios,
  30 músculos mapeados, 5 plantillas, 100% gratis para empezar), 6 tarjetas bento
  construidas con los componentes REALES de la app (calendario, mapa muscular, PR con
  sparkline, mini share-card). Aclaración propia: **el holograma es Wallace, no una
  mascota genérica** (fix explícito 12-jul) — coherente con la idea de la torre de un
  Wallace visual en la landing.
- ✅ **12-jul — calendario y rutinas**: crear rutina respeta las reglas del día, guardado
  a prueba de cortes de red, selector de ejercicios a 2 columnas en desktop, figuras de
  rutina más grandes con mancuerna cian para sesiones libres, "+ Nueva rutina" crea y
  loguea en un solo paso.
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
