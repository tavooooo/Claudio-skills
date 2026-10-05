# FitMark — Mapeo de fotos guía (free-exercise-db)

> Generado por la torre de control (loop) el 2026-07-15. Cruza los **152 ejercicios**
> de FitMark (`src/lib/data/exercises.ts`) contra los **873** de
> [`yuhonas/free-exercise-db`](https://github.com/yuhonas/free-exercise-db) (dominio
> público / Unlicense — **$0, uso comercial OK, sin atribución**). Objetivo: cuántos
> ejercicios pueden llevar foto guía GRATIS desde el día 1, y cuáles quedan primeros
> en la cola de los GIFs de Wallace 3D.

## Resultado

| Clase | Ejercicios | % | Qué significa |
|---|---|---|---|
| ✅ **DIRECTO** | 122 | 80% | Match confiable, usar la foto tal cual |
| 🟡 **PROBABLE** | 20 | 13% | Hay candidato pero conviene mirarlo (algunos son la variante equivocada) |
| 🔴 **HUÉRFANO** | 10 | 6% | Sin foto en el dataset → primeros para Wallace |
| | | | |
| **Cobertura potencial** | **142/152** | **93%** | con las gratis, hoy |

**Lectura honesta**: los ~122 DIRECTO son sólidos (auditados a muestra). De los 20
PROBABLE, aproximadamente la mitad son correctos y la otra mitad son la variante
equivocada (ej. *Band Hip Adductions* por Abducciones = músculo opuesto; *Yoke Walk*
≠ Caminata del Pato) — por eso van a revisión manual, no directo. Piso realista de
cobertura limpia sin tocar nada: **~80%**; con 10 min de revisión de los PROBABLE, ~88-90%.

## 🔴 Huérfanos — cola de Wallace (no existen en el dataset)

- **Hollow Hold** · `hollow-hold` — core/BODYWEIGHT
- **Burpees** · `burpees` — cuadriceps/BODYWEIGHT
- **Sentadillas Isométricas en Pared** · `sentadilla-isometrica-pared` — cuadriceps/BODYWEIGHT
- **Abducciones de Cadera en Polea de Pie** · `abduccion-cadera-pie-polea` — gluteos/CABLE
- **Almeja con Banda** · `almeja-banda` — gluteos/RESISTANCE_BAND
- **Bird Dog** · `bird-dog` — gluteos/BODYWEIGHT
- **Frog Pump en Máquina Smith** · `frog-pump-smith` — gluteos/SMITH_MACHINE
- **Hidrante** · `hidrante` — gluteos/BODYWEIGHT
- **Patadas de Burro** · `patada-burro` — gluteos/BODYWEIGHT
- **Peso Muerto Sumo con Kettlebell** · `peso-muerto-sumo-kettlebell` — gluteos/KETTLEBELL

(Son casi todos ejercicios modernos de glúteo/core con nombre propio: bird dog,
hollow hold, frog pump, hip thrust variantes smith, hidrante, patada de burro, wall
sit. Justo el tipo de contenido donde Wallace 3D suma más que una foto de archivo.)

## 🟡 Probables — revisar a ojo (10 min)

| FitMark | Candidato free-exercise-db | score |
|---|---|---|
| Aperturas con Mancuernas | One-Arm Flat Bench Dumbbell Flye | 0.8 |
| Fondos en Paralelas (Pecho) | Parallel Bar Dip | 0.65 |
| Pec Deck (Contractora) | Butterfly | 0.8 |
| Peso Muerto Sumo con Barra | Barbell Deadlift | 0.8 |
| Pájaros con Mancuernas | Bent Over Dumbbell Rear Delt Raise With Head On Bench | 0.8 |
| Patadas de Tríceps con Mancuerna | Decline Dumbbell Triceps Extension | 0.8 |
| Press Francés con Barra EZ | Lying Close-Grip Barbell Triceps Extension Behind The Head | 0.7 |
| Press Francés Sentado con Barra | Lying Close-Grip Barbell Triceps Extension Behind The Head | 0.7 |
| Caminata del Pato | Yoke Walk | 0.8 |
| Saltos con Rodillas al Pecho | Knee Tuck Jump | 0.65 |
| Subidas al Cajón con Mancuernas | Dumbbell Seated Box Jump | 0.63 |
| Nordic Curl (Curl Nórdico) | 90/90 Hamstring | 0.8 |
| Swing con Kettlebell | Double Kettlebell Alternating Hang Clean | 0.8 |
| Abducciones de Cadera en Máquina | Thigh Abductor | 0.8 |
| Abducciones de Cadera Sentado con Banda | Band Hip Adductions | 0.55 |
| Elevaciones de Cadera Tumbado de Lado | Hip Circles (prone) | 0.63 |
| Elevaciones Laterales de Pierna Tumbado | Lateral Bound | 0.63 |
| Frog Pump | Frog Sit-Ups | 0.65 |
| Peso Muerto con Balón Medicinal | Axle Deadlift | 0.65 |
| Zancadas con Mancuernas | Dumbbell Rear Lunge | 0.65 |

## Cómo se arma la URL de cada foto

Cada ejercicio del dataset trae 2 fotos (inicio → fin). Patrón de URL cruda:

```
https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/<fedb_id>/0.jpg   (inicio)
https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/<fedb_id>/1.jpg   (fin del movimiento)
```
Ejemplo: `press-banca-barra` → fedb_id `Barbell_Bench_Press_-_Medium_Grip` →
`https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/Barbell_Bench_Press_-_Medium_Grip/0.jpg`

El CSV `mapeo_fitmark_fedb.csv` (adjunto) tiene las 152 filas con `fm_slug`,
`fedb_id` y `img` (path de la primera foto) listas para consumir.

## 📋 Brief listo para pegar en el chat de FitMark

> **Contexto**: decidimos lanzar con fotos guía gratis de free-exercise-db (dominio
> público) y reemplazarlas de a poco por GIFs de Wallace 3D. La torre ya cruzó los 152
> ejercicios contra el dataset: **142/152 (93%) tienen candidato**, ~122 confiables.

> **Tarea sugerida** (sin bloquear nada existente):
> 1. Agregar un campo opcional `guideImage?: { start: string; end: string }` al tipo
>    `Exercise` (o una tabla/mapa `slug → fedb_id` aparte para no ensuciar el seed).
> 2. Descargar las ~142 fotos del dataset a `public/exercises/<slug>/{0,1}.jpg` (o
>    servirlas por URL cruda de GitHub al principio para no pesar el repo).
> 3. Mostrarlas en la ficha del ejercicio como par inicio→fin (o crossfade suave).
> 4. Para los 10 huérfanos + los PROBABLE errados: dejar el placeholder actual y
>    marcarlos como 'cola Wallace'. El CSV de la torre trae la clasificación por slug.
> 5. Licencia: free-exercise-db es Unlicense (dominio público). Los GIFs de Gym Visual
>    NO se usan (© de ellos). Todo lo de acá es limpio para comercial.
