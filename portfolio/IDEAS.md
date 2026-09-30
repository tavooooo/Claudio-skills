# 💡 Ideas — Estacionamiento

> Toda idea nueva se anota aquí y NO interrumpe el sprint activo (regla 4 de `PIPELINE.md`).
> Formato: fecha · idea · proyecto afectado · ¿cuándo evaluarla?

| Fecha | Idea | Proyecto | Evaluar en |
|---|---|---|---|
| 2026-07-05 | Comercializar Navaja Suiza para nicho mochileros WHV | La-Suiza | 2027, si hay ingresos en los otros 3 |
| 2026-07-05 | Diseñar "loops" (chequeos autónomos) para que Claude ayude sin supervisión constante | portfolio | En definición — ver pregunta abierta abajo |

## Brainstorm de nombre — FitMark / "Biohack AI" (verificado en web el 2026-07-05)

Disponibilidad chequeada contra apps de fitness existentes:

| Candidato | Estado | Nota |
|---|---|---|
| **Ferro** ⭐ | 🟢 Libre entre apps | Solo choca con un fabricante de máquinas (ferrogym.com). Logo natural: ficha de tabla periódica "Fe" |
| **Wallace** ⭐ | 🟢 Libre en fitness | Capitaliza el coach que ya existe; marca humana estilo "Alfred" |
| Férreo | 🟢 Probablemente libre | Variante de respaldo de Ferro ("voluntad férrea") |
| Tensor | 🔴 Tomado | tensorfit.com |
| Fierro | 🔴 Tomado | fierro.app — ⚠️ además es COMPETENCIA directa: app de gym con IA en español, PRs, rankings |
| Overload | 🔴 Tomado | OverLoad en App Store |
| Gymetric | 🔴 Tomado | GyMetric en Google Play |

**Estado 2026-07-05: APARCADO por decisión de Gustavo** — ni Ferro ni Wallace lo
convencieron. Hay tiempo para pensarlo; la prioridad ahora es lanzar antes que la
competencia. Cuando se retome: verificar dominio, App Store/Play Store, INAPI (Chile)
e IPONZ (NZ) del candidato final. FitMark sigue como nombre provisorio de trabajo.

**⚠️ Inteligencia competitiva — fierro.app** (investigado por Gustavo, 2026-07-05):
ver ficha completa en `proyectos/fitmark.md` § Competencia.

## ~~Pregunta abierta — loops autónomos~~ ✅ Resuelto 2026-07-05

Gustavo decidió: loop **diario** (08:00 NZ), con los 3 niveles de alcance
(revisar+avisar, coordinación, y avance autónomo en proyectos en pausa), push al
teléfono si es urgente + resumen siempre en el chat. Implementado — ver `LOOPS.md`.

## 🎨 Ilustraciones de ejercicios con IA local (anotado 2026-07-07)

Idea de Gustavo: generar las ilustraciones del avatar haciendo cada ejercicio
(152) con modelos de imagen gratis.

- **Piloto**: build.nvidia.com (créditos gratis ~1k-5k) SOLO para validar estilo —
  su licencia es de evaluación, no sirve para assets de producción.
- **Producción**: correr local en el PC de Gustavo (GPU NVIDIA 8GB+ VRAM):
  FLUX.1-schnell (Apache 2.0, comercial OK) o SDXL. FLUX.1-dev NO (no comercial).
- **Receta de consistencia**: LoRA del avatar (20-30 imgs de entrenamiento) +
  ControlNet/OpenPose con esqueletos de poses reales → mismo personaje, técnica correcta.
- **Dimensión**: ~300 finales (2 poses × 152 ejercicios), ~2.000 generaciones con
  descartes, ~4-8 h de GPU local. Pendiente: confirmar GPU del PC de Gustavo.
- **Hardware de Gustavo (2026-07-07)**: notebook 32GB RAM + i7 + **RTX NVIDIA 16GB
  CONFIRMADA** → vía local viable: FLUX.1-schnell fp8
  (~15-25s/img) o SDXL (~8-15s/img); las ~2.000 generaciones = 8-12h de GPU
  (tandas nocturnas, notebook enchufado y ventilado). LoRA del avatar entrenable
  local. Plan: piloto 5 ejercicios en build.nvidia.com → ComfyUI local → LoRA →
  producción de las 152.

### 📦 Datasets de ejercicios evaluados (2026-07-14, pedido de Gustavo)

Gustavo recordó un repo de GitHub con "+1.400 gifs de ejercicios". **Encontrado y
verificado**: es **`hasaneyldrm/exercises-dataset`** — 1.324 ejercicios, cada uno con
gif animado (180×180) + thumbnail + metadata (categoría, músculos, equipo,
instrucciones en 9 idiomas), gifs guardados en el repo (`videos/[id]-[media_id].gif`).

⚠️ **HALLAZGO CRÍTICO DE LICENCIA (esto cambia el plan)**: los gifs **NO son libres**.
- El **código y el JSON** son MIT (uso comercial OK).
- Pero las **imágenes/gifs son © Gym Visual** (gymvisual.com), redistribuidos en el
  repo a 180×180 "con permiso". El propio repo dice que **no reclama propiedad del
  contenido** y que el **uso comercial requiere tu propia licencia de Gym Visual**.
- Implicancia dura: **no se pueden meter esos gifs en FitMark tal cual** (sería
  infracción), y **tampoco calcarlos/rotoscopiarlos** para hacer "los nuestros" con
  Wallace — una animación trazada de la de ellos sigue siendo obra derivada = infracción.
  Incluso extraer esqueletos OpenPose *automáticamente de sus gifs* para alimentar
  ControlNet es zona gris (el esqueleto deriva de sus decisiones creativas de animación).

✅ **Lo que SÍ sirve, limpio y gratis** — enfoque en 2 capas:
1. **Capa de metadata (catálogo)**: el JSON MIT de este repo (nombres, categorías,
   músculos, equipo, instrucciones 9 idiomas) es usable comercial. Alternativa aún más
   limpia para la data: **`yuhonas/free-exercise-db`** (~800 ejercicios, data en
   **Unlicense = dominio público total**, sin atribución; imágenes son fotos JPG, no gifs).
   → Sirve para poblar/validar el catálogo de FitMark sin nube legal.
2. **Capa de movimiento (los gifs de Wallace)**: las poses tienen que ser **nuestras**.
   Los gifs de Gym Visual pueden mirarse como *referencia visual para uno mismo* (igual
   que ver cualquier video para saber cómo se hace un ejercicio), pero **no como input
   que la pipeline reproduce**. Camino comercial limpio para el movimiento:
   - Definir las poses nosotros: librería de poses de dominio público, mocap propio, o
     posar el esqueleto OpenPose a mano por ejercicio → luego FLUX.1-schnell + ControlNet
     genera a Wallace sobre ESE esqueleto (encaja con la pipeline ya anotada arriba).
   - O, si se quiere velocidad, **licenciar el pack de Gym Visual** (tienen licencia
     comercial a la venta) y usar sus gifs directo — evita generar, pero no es "Wallace".

**Términos reales de Gym Visual (verificados 2026-07-15)**: licencia N-CRFL
(no-exclusiva, royalty-free, pago único, perpetua, mundial). Gifs ~$10 c/u, baja a
**~$6 c/u comprando 5+**; ilustraciones planas $3 → $0.75 (10+). Catálogo: 6.502 gifs.
Costo estimado para las 152 de FitMark ≈ **$900 USD una sola vez** (o menos si se usan
ilustraciones planas en vez de gifs). ⚠️ **DOS restricciones que nos pegan**: (1) prohíbe
usar los assets en "productos destinados a reventa" o "stock content"; (2) **prohíbe
explícitamente subirlos/distribuirlos en cualquier plataforma de IA** → confirma por
partida doble que **NO** se pueden usar como input para generar los de Wallace (lo bloquea
el copyright Y su propia licencia). O sea: licencia Gym Visual y Wallace-generado son
caminos **excluyentes**, no uno escalón del otro.

**Opción 100% gratis que funciona HOY como guía**: las **fotos JPG de free-exercise-db**
(dominio público, Unlicense) — no son animadas, son fotos de personas reales demostrando,
pero legales y $0. Sirven de guía visual en la app desde ya, sin licencia ni riesgo.

### 📊 Mapeo 152 FitMark ↔ 873 free-exercise-db (hecho 2026-07-15)

**Decisión de Gustavo (15-jul)**: lanzar con las fotos gratis y reemplazar de a poco por
GIFs de Wallace. La torre cruzó los 152 ejercicios de FitMark contra los 873 del dataset
(script + reporte + CSV en `portfolio/recursos/fitmark-fotos/`):

- ✅ **122 DIRECTO (80%)** — match confiable, foto usable tal cual.
- 🟡 **20 PROBABLE (13%)** — hay candidato pero ~mitad son la variante equivocada
  (ej. *Band Hip Adductions* por Abducciones = músculo opuesto) → 10 min de revisión manual.
- 🔴 **10 HUÉRFANO (6%)** — no existen en el dataset (bird dog, hollow hold, frog pump,
  hip thrust smith, hidrante, patada de burro, wall sit, sumo-KB) → **primeros en la cola
  de Wallace**, que es justo donde el 3D suma más que una foto de archivo.
- **Piso realista de cobertura limpia: ~80% hoy, ~88-90% con la revisión de los PROBABLE.**

Entregables en `portfolio/recursos/fitmark-fotos/`: `MAPEO.md` (reporte + brief listo para
pegar en el chat de FitMark), `mapeo_fitmark_fedb.csv` (152 filas slug→fedb_id→foto),
`match.py` (script reproducible). El chat de FitMark implementa el wiring — la torre solo
preparó el mapa (no toca su código).

✅ **EJECUTADO por el chat de FitMark (15-jul)**: construyeron `exerciseGuideImages.ts` +
`ExerciseGuideImage.tsx`, y **auditaron a ojo cada foto** — corrigieron los 27 mapeos "PROBABLE"
con variante equivocada que la torre había marcado como dudosos, agregaron 2 y quitaron 10 sin
foto válida → **127/152 verificadas**, 25 a la cola de Wallace. El mapeo de la torre sirvió de
base y su auditoría lo mejoró. Está en rama `test/fotos-guia-fedb`, falta mergear a main.
   El diferencial de marca (Wallace haciendo cada ejercicio) sale de la vía generada, no
   de reusar los de Gym Visual.
   El diferencial de marca (Wallace haciendo cada ejercicio) sale de la vía generada, no
   de reusar los de Gym Visual.

**Veredicto**: el repo es un gran hallazgo **para la metadata** (o mejor free-exercise-db
por licencia), pero **no como fuente de gifs** para un producto comercial. Los gifs de
Wallace hay que generarlos con poses propias. Esto NO cambia la pipeline FLUX/ControlNet
ya planeada — solo confirma que el esqueleto de pose debe originarse limpio, no calcado
de Gym Visual.

## 🔁 Reconstrucción de features-review (FitMark) — desde cero (decidido 2026-07-08)

La rama `claude/features-review` se DESCARTA (129 commits divergentes; rehacer
limpio < cherry-pick). Inventario de lo que tenía, para reconstruir en `main`
cuando toque (Sprint 4, monetización/social, sep):

- **Ranking** entre usuarios/amigos.
- **Red social / feed** (seguir, publicar, ver actividad).
- **Planes** (tiers premium más allá del freemium actual 5/5).
- **Cuentas de gym / coach** (roles distintos al usuario normal).
- **Chat**.

⚠️ **Salvar ANTES de borrar la rama** (esto NO se reconstruye, es contenido):
`wallace-kb/` → `wallace-wiki.wkml` (~550KB, 262 artículos) + `indice-wallace.html`
+ `resumen-wallace-kb.html` + `README.md`. Exportarlos a un lugar seguro (o a
main bajo `wallace-kb/`) evita reescribir 262 artículos a mano. Lo hace el chat
de dev de FitMark en el mismo movimiento en que borra la rama.
- **Mantenerlo en la MISMA ruta** (`wallace-kb/` en la raíz) es lo más seguro:
  así cualquier referencia existente de Wallace al KB sigue resolviendo. Si se
  decide moverlo (a `src/`, `public/`, etc.), el chat de dev DEBE actualizar la
  ruta que usa Wallace (RAG/coach) para no dejar al coach sin base de conocimiento
  (pedido explícito de Gustavo 08-jul).

## 🕹️ Landing "gym navegable" con Wallace 2.5D (idea 2026-07-12)

> ✅ **EN CONSTRUCCIÓN (03-ago-2026)**: el chat de FitBook empezó a construirlo. Wallace camina
> hacia la cámara (ciclo de andar de 4 fotogramas, atlas de 5 vistas → 8 direcciones), 5 estaciones
> medidas sobre el render, y el MuscleMap pasó a ser el avatar "cuerpo iluminado". Hay demo
> autocontenida del gimnasio. La idea de abajo se está haciendo realidad — dejar esta sección como
> registro del origen (el video de Emergent) y del razonamiento técnico que se recomendó.


Gustavo compartió un video-ad de "Emergent" (app.emergent.sh): un sitio tipo
videojuego top-down donde un personaje camina por una escena isométrica y, al
pisar carteles en el piso (PRODUCTS, MEN, ABOUT...), se abren paneles con
contenido real. Quiere algo así para FitMark: estaciones dentro de un gym
(mesón de entrada, base de ejercicios, etc.) con **Wallace en 3D/2.5D**
caminando entre ellas.

**Veredicto técnico**: factible y FitMark YA tiene `three.js` en el stack (no
hace falta adoptar Emergent ni ninguna herramienta externa).

**Dos caminos evaluados**:
- A) Movimiento libre 3D (como el video) — alto impacto, alto costo; choca con
  la regla mobile-first de FitMark (WASD no existe en iPhone, hay que diseñar
  control táctil desde cero).
- B) **Recomendado**: "gym tour" con **GSAP ScrollTrigger** (skill ya instalada
  en FitMark) — el scroll mueve la cámara por el gym ilustrado, estación por
  estación, con Wallace caminando en 2-3 poses. Mobile-friendly nativo (el
  scroll ES el control), sin física de colisiones.

**Wallace 2.5D en vez de 3D completo**: evita rigging/animación 3D real
(semanas de trabajo). Se puede generar con la misma pipeline de ilustraciones
IA local ya anotada en el tablero (ComfyUI + FLUX, RTX de Gustavo).

**Prioridad**: landing nueva, NO bloquea el lanzamiento (Stripe/nombre van
primero). Diferenciador fuerte vs. fierro.app — ningún competidor tiene algo
así. Cuando se retome: preparar spec/brief detallado para el chat de dev de
FitMark (la torre no toca su código).
