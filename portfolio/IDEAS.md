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
