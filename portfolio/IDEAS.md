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
- **Hardware de Gustavo (2026-07-07)**: notebook 32GB RAM + 16GB video + i7.
  PENDIENTE verificar que sean 16GB de GPU NVIDIA dedicada (nvidia-smi) y no
  memoria compartida de Intel integrada. Si es RTX 16GB: FLUX.1-schnell fp8
  (~15-25s/img) o SDXL (~8-15s/img); las ~2.000 generaciones = 8-12h de GPU
  (tandas nocturnas, notebook enchufado y ventilado). LoRA del avatar entrenable
  local. Plan: piloto 5 ejercicios en build.nvidia.com → ComfyUI local → LoRA →
  producción de las 152.
