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

## Estado (actualizado 2026-08-10 por el loop, desde git main — ~98%, EN BETA CERRADA)

- 💪 **10-ago — gran tanda en el mapa muscular + catálogo**: el trapecio se parte en **3 zonas**
  (y se nombra por zonas en los 23 ejercicios que lo tocan), romboides y redondo menor estrenan trazo
  propio, y el **serrato se reasigna a hombros** (en 20/23 ejercicios cargaba él solo la cifra de espalda
  alta). El heatmap ahora cuenta **MÚSCULOS** (el grupo solo agrupa) y sube de 10 a **15 grupos**; el
  core deja de encenderse en día de pierna. Herramienta de trazado de músculos en el repo (con guardián
  que vigila la trampa de cortar dos veces el original). Migración 031 (los 21 ejercicios que la app
  conocía y la base no). Los **1103 logros** ahora en inglés. Fix volumen de unilaterales (valía la mitad).
- 🌐 **09-ago — logros en inglés + Catálogo completo + rango a 4 peldaños**: la tubería de logros y
  las **674 placas del Catálogo** ahora hablan inglés (antes el Catálogo solo mostraba 132: faltaban
  los ejercicios sin tocar). El cardio llega hasta el rango "Amo" (250 sesiones) y la escalera de un
  ejercicio sube a **cuatro peldaños** (Maestro, Amo). Carrusel de rangos que viste la página entera al
  hojear, muestra semanal grupo por grupo, y la "estela" de la placa del ejercicio en curso gira al
  doble para avisar de logros nuevos. Fix: hojear el carrusel ya no abre descanso en la última serie.
- 💠 **08-ago — pulido fino del sistema de logros**: el "latido" de la raya del catálogo (pasa por
  blanco antes de apagarse, ya no se pintaba doble), rarezas/sombras/arlequines ahora conseguibles,
  el hexágono avisa "hay algo nuevo" y la raya dice cuál. **Los logros se conceden AL ESCRIBIR + hay
  barrido nocturno** (con aviso que lleva hasta ellos); botón de admin para revivir el aviso de logros
  ya conseguidos. Cardio "Dominado" pide sesiones, no series. Progreso: "0,15 de 1" reemplazado por
  dos condiciones con dos barras y cifras reales. Nota técnica: anotaron en AGENTS.md las trampas de
  `pg_net` en el barrido.
- 🔞 **07-ago — dos piezas de lanzamiento + más logros**: **fecha de nacimiento pedida al registrarse
  con verificación de edad** (compliance — la app declara `minAge` en los legales) e **invitaciones
  abiertas** (cualquiera puede invitar, no solo el admin → mecanismo de crecimiento viral de la beta).
  Bug real corregido: el gráfico de progreso decía 73 kg sobre un punto dibujado en 102. Logros:
  Colecciones y Catálogo encendidos (+375 placas), +100 de volumen, Constancia se concede sola, y una
  **auditoría de logros** (qué se puede verificar de verdad; dos etiquetas que mentían, corregidas). El
  buscador entiende los dos idiomas y palabras sueltas.
- 🛡️ **06-ago — perfil de rango pulido (continuación)**: el **marco** con **escudo por rango** y
  **anillo de nivel** entra en Progreso (con la foto del muro), un juego de escudos por rango con su
  neón (38→56 px, la Bestia deja de verse chica), "si eres Oro **todo** es de oro" (tarjeta, barra,
  halo), nombre grande sobre el marco. Terminología: **las medallas son RANGOS**, "nivel" queda para
  la experiencia. Cartel de 3 pasos para quien entra a Progreso y aún no ve nada. Todo pulido visual
  del sistema de rangos de los días previos.
- 🏅 **05-ago — capa de enganche ENORME: 968 logros + rangos narrados**: **catálogo de 968 logros**
  (893 de base + 75 reconocimientos), servido en una **página pública** `/catalogo-logros.html` (sin
  login, útil también para marketing). Las **placas de rango** ganan **36 títulos fijos por usuario**,
  un **"papiro"** que te llama por nombre y cuenta tu historia (cada placa cuenta SU historia, no tu
  índice de hoy), tiers ligados a técnicas avanzadas (**Oro** = Bi-Serie Suprema, **Esmeralda** =
  Súper Serie al Fallo, Bronce ya visible). Regla: **sin peso corporal no hay rango**. El "cuerpo
  encendido" estrena **leyenda en /progress** (qué se consigue en cada color/zona). **Escalera de
  volumen recalibrada** para que la base dure años, no meses (progresión sostenible a largo plazo).
- 🏆 **04-ago — sistema de RANGOS gamificado "La Bestia" + cardio en rutinas**: el rango estrena
  **placas** en un **carrusel de 6** (la del usuario presidiendo la tarjeta, con cartel "BLOQUEADO"
  cruzado en diagonal), placas que se igualan por área y crecen por peldaño, con nombres de nivel,
  neón que respira y destello — el enganche del carrusel es propio (no el snap del navegador) y afinado
  para iPhone/WebKit. Refuerza el gimnasio navegable con **progresión visual de nivel**. Además,
  **cardio dentro de las rutinas**: objetivo de distancia/km por ejercicio, la bici deja de pedir
  repeticiones (el catálogo manda sobre lo guardado), el cardio se pauta como una tanda entera.
- 🕹️ **03-ago — NACE el "gimnasio navegable" con Wallace 3D** (la idea del video, ver `IDEAS.md`):
  **Wallace camina de verdad hacia la cámara** (ciclo de andar de 4 fotogramas, sin patinar), con
  un **atlas de 5 vistas generadas → 8 direcciones en pantalla**, recorriendo **5 estaciones**
  medidas sobre el render. El **MuscleMap dejó de ser un widget y pasó a ser tu AVATAR** ("cuerpo
  iluminado": escala de 4 tonos, rellenos translúcidos que tiñen sin tapar, luz simétrica). Hay una
  **demo autocontenida del gimnasio** para mirarlo sin desplegar. Renders optimizados (1,8 MB → 32 KB).
  Es exactamente el concepto que la torre registró el 12-jul tras analizar el video de Emergent —
  ahora en construcción real.
- 📈 **03-ago — "escalera" de peso corporal en /progress**: 6 peldaños derivados del historial
  (puros, con tests), migración `022` (historial de peso corporal). F0: índices que faltaban + limpieza
  (16 MB de peso muerto fuera).
- 💬 **02-ago — comentarios con HILOS en el feed**: respuestas anidadas a comentarios (hilos de un
  nivel), barra de comentar sobre el teclado con textarea que crece, animación de la primera
  respuesta, manejo de respuestas que fallan. + CTA "Empezar gratis" fijado al borde inferior de la
  landing. Iteración de beta sobre la capa social.
- 🧠 **30-jul — Wallace más inteligente + feed social pulido**: **Wallace con contexto completo**
  (comentarios + 14 días de comida + días sin registro) y **dietas como tarjetas agregables al
  calendario** — el coach IA ahora razona con la nutrición además del entreno. **Reacciones estilo
  Facebook** en el feed (💪 con long-press para elegir emoji + apilado que abre la lista, con los
  fixes de selección de texto de iOS durante el gesto). Renombre: el espacio de UNA persona pasa de
  "Muro" a **"Perfil"** (con @nickname editable). Sesiones: el orden de ejercicios se guarda y se
  respeta, foco automático en el ejercicio en curso; cardio/isométricos ya no piden peso en la revisión.
- 🧪 **28-jul — iterando la beta + más pulido de lanzamiento**: **pre-aprobar invitaciones por
  correo** (antes de que exista la cuenta), **medidor de cupo del plan gratis en las 4 pantallas**
  con tope, "Premium **próximamente**" en la landing + tarjeta que explica lo "prestado" durante la
  beta, **cupo de IA atómico en Postgres** (migración 017). **i18n 100%**: barrido total, todo lo
  visible al usuario es bilingüe es/en. Nuevo **sistema de calentamiento** (fila de warm-up arriba,
  editable/borrable desde el día, incluida en el volumen y en la imagen compartida) + **reordenar
  series arrastrando** (long-press) + comprimir tarjeta de ejercicio a una línea. **Más renders 3D
  propios**: Peso Muerto Rumano e Hip Thrust (fondo negro puro) → ya ~4 ejercicios con render propio.
- 🚀 **27-jul — BETA CERRADA (hito)**: FitBook pasó a **acceso por invitación** (un único control
  para las dos vías, fix del bucle de redirección, nav apagada sin invitación), con **formulario de
  feedback** (tarjeta de agradecimiento en Hoy + contexto) y **topes del plan gratis subidos** para
  la beta. Ya no es solo desarrollo: hay **usuarios reales probando**. Además, listo para instalarse:
  - **PWA instalable**: manifest + iconos + meta de iOS para abrir a pantalla completa; icono con el
    logo completo (mancuerna + FIT book).
  - **Notificaciones en tiempo real** (con sondeo como red de seguridad), cada aviso lleva a su pantalla.
  - **Endurecimiento de seguridad**: cabeceras HTTP, cobro simulado detrás de un flag, errores sin
    detalle interno.
  - **Biblioteca de alimentos server-side** (deja de vivir en el navegador → persistencia real por usuario).
  - Fix de kcal con basura de coma flotante, fix del holograma de la landing (las cabeceras bloqueaban el iframe).
- 🛠️ **26-jul — sistema de admin del CATÁLOGO + Wallace multiidioma**: máquina de back-office para
  gestionar el catálogo a medida que los usuarios crean ejercicios propios — triaje de personalizados
  (agrupados y con duplicados), **la IA los agrupa**, migración de un grupo al catálogo oficial
  avisando al usuario, reparar filas que quedaron en el ejercicio equivocado (por usuario y rango de
  peso), revertir renombrados usando las notificaciones como registro, previsualización de impacto.
  Panel de notificaciones manual + avisos automáticos al promover. Matching más fino: **unilateral
  vs bilateral e instrumento como diferenciadores duros**, buscador de destinatarios por nombre/@alias.
  **Wallace responde en el idioma en que le escriben**. 3 ejercicios nuevos (Curl Martillo Cruzado,
  Sentadillas Búlgaras con Mancuernas, Aducciones de Cadera en Máquina). Lint del repo a cero.
- 📄 **25-jul — legales al día + cardio afinado + limpieza**: **documentos legales (T&C +
  Privacidad, ES+EN) actualizados** para cubrir las features nuevas (nutrición, muro, coach) —
  disciplina pre-lanzamiento. Cardio afinado (tiempo en minutos que se guarda en segundos, métrica
  secundaria por ejercicio km/m/saltos/pisos, caminata inclinada con ajuste de columnas), dropsets
  como cadena agrupada con color por tipo, fix de guardado (una columna sin migrar ya no perdía el
  entreno), repasada completa de i18n. **Limpieza**: se eliminó el mapa muscular 3D experimental
  (`/muscle-map`).
- 🏃 **24-jul — grupo CARDIO + dropsets + "Muro"**: nuevo grupo **CARDIO** con 9 ejercicios
  registrables por tiempo ("cardio lite") — el catálogo se amplía más allá de la fuerza. Tipos de
  serie **W/D/F + dropsets** (menú al tocar el número de serie), "copiar a todas" con fill-down por
  columna (peso y reps por separado). La red social se **renombró de "Vitrina" a "Muro"** en toda la
  UI visible. + acceso "Mis alumnos" para coaches en móvil, notificación de bienvenida al hacerse
  Premium, fixes de compartir (PNG en la primera captura) y pulido del bottom nav (haz tipo cometa).
- 🎉 **23-jul — RED SOCIAL MERGEADA A MAIN**: la "vitrina" pasó a producción — `src/app/vitrina/_components/`
  (PostCard, PostComposer, RepostModal, SocialSidebar, WallSocialRow) con posts, muros por @nickname,
  reposts, menciones, moderación y tests (`social-actions.test.ts`). Con esto la reconstrucción de
  `features-review` queda **esencialmente completa** (coach + chat/Wallace + red social, los 3 en main).
  La rama `vitrina` volvió a estar a la par de `main`.
- ✨ **23-jul — gran pase de UI/UX**: dashboard "Hoy" rediseñado (racha/stats en una tarjeta, gráficos
  de fuerza en carrusel), **constructor de rutinas v2** (filtros desplegables, acordeón, chips
  indicadores), botón central "Entrenar", campanita de notificaciones estilo "T", y **nuevo eslogan:
  "Registra. Progresa. Rompe récords."**
- 📣 **22-jul — arranca el motor de contenido pre-lanzamiento**: (a) rama nueva
  `claude/fitbook-content-calendar-jfxiw1` con un **calendario de contenido orgánico de 4 semanas**;
  (b) en main, **compartir "Mi semana/mes" del calendario como imagen** para redes (theme-aware,
  figuras musculares con color fiable en iOS Safari vía color literal + precarga/decode, zona
  horaria dinámica del dispositivo). Es la munición de contenido que el usuario puede postear.
  (En paralelo, el repo de la torre sumó skills de social/video/canvas/grabar-demos.)
- ☀️ **21-jul — TEMA CLARO completo (en main)**: "versión día" estilo Apple seleccionable desde
  el menú del usuario. Trabajo grande (~20 commits): un solo verde de marca por variable CSS
  (`var(--acc)`, #76b900) en toda la app, cero negros residuales, fixes de serialización CSSOM
  (nav, bandas sticky, toggles), landing siempre oscura, arte anatómico sobre lienzo adaptado.
  La app deja de ser solo dark.
- 👨‍🏫 **21-jul — panel coach más profundo (en main)**: tabla comparativa de alumnos, cambio
  rápido entre alumnos, **nutrición real + meta semanal por alumno**, ficha del alumno con roster
  lateral y calendario clickeable. El tier Coach pasa de "cimientos" a herramienta usable.
- 📱 **20-jul — RED SOCIAL v3 casi lista (rama `vitrina`, aún no en main; ya 67 commits sobre main)**: "Vitrina v3" en fases
  A–E — datos/lib/actions (notifs, reposts, likes, edición, denuncias), **PostCard pro** (menú,
  edición, denuncia, repost, likes, menciones), **campanita de notificaciones + listas de follows +
  muros por @nickname**, **semana de entreno compartible + panel de moderación**. Es la pieza "red
  social/feed" de features-review, ya bastante completa. `vitrina` es staging (30 commits adelante
  de main, se mergea con main regularmente). Falta el merge a main.
- ✨ **20-jul — pulido en main**: visualización del exceso de macros (escala ámbar→naranja→rojo
  según cuánto te pasaste de la meta, respetando el color base de cada macro), vista semana de
  comidas con kcal dentro del anillo, mapa muscular (antebrazo siempre en ambas láminas), panel
  coach con días de asignación.
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
