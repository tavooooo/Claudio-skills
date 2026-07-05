---
name: portfolio-tracker
description: Sistema de trazabilidad del portfolio de proyectos de Gustavo (Kiwiano, FitMark, Easy Courts, Navaja Suiza). Usar al inicio de CUALQUIER sesión de trabajo en un proyecto del portfolio (cargar contexto y sprint activo), al terminar una sesión (registrar avance y gasto en tokens), cuando se pida "estado del portfolio", "cómo van los proyectos", "actualiza el dashboard", o cuando aparezca una idea nueva que amenace con desviar el sprint activo.
---

# Portfolio Tracker

Fuente de verdad: carpeta `portfolio/` en el repo **Claudio-skills**.

| Archivo | Qué es |
|---|---|
| `portfolio/PERFIL.md` | Quién es Gustavo, objetivo, forma de trabajo |
| `portfolio/PORTFOLIO.md` | Dashboard maestro: estado, riesgos, checklist comercial |
| `portfolio/PIPELINE.md` | Sprints con deadlines y reglas de foco |
| `portfolio/proyectos/*.md` | Ficha por proyecto (estado, brechas, docs internas) |
| `portfolio/metricas/sesiones.csv` | Registro de sesiones: avance + tokens/costo |
| `portfolio/IDEAS.md` | Estacionamiento de ideas (no interrumpen el sprint) |

## Al INICIAR una sesión de trabajo

1. Lee `PERFIL.md`, `PORTFOLIO.md` y `PIPELINE.md`.
2. Identifica el **sprint activo** y verifica que el trabajo pedido pertenece a él.
   - Si el pedido es de OTRO proyecto: adviértelo ("esto rompe el foco del sprint X")
     y ofrece anotarlo en `IDEAS.md` en vez de ejecutarlo. Gustavo decide.
3. Lee la ficha del proyecto en `proyectos/` antes de tocar código.

## Al TERMINAR una sesión de trabajo

1. Añade una fila a `metricas/sesiones.csv`:
   `fecha,proyecto,resumen,tokens_entrada,tokens_salida,costo_usd,fuente_costo,notas`
   - Si la sesión corre en API/CLI local, usa `/cost` para obtener el gasto.
   - Si corre en claude.ai (suscripción), deja `costo_usd` vacío y `fuente_costo=suscripcion`;
     el costo real se revisa en Configuración → Uso.
2. Actualiza la ficha del proyecto (`proyectos/<nombre>.md`): fecha, estado, brechas.
3. Si cambió el avance global, un riesgo o una fecha, actualiza `PORTFOLIO.md`
   (y `PIPELINE.md` si una deadline se movió — anotar el motivo).
4. Marca los checkboxes del sprint en `PIPELINE.md` que se hayan completado.
5. Commit + push de `portfolio/` con mensaje `portfolio: <resumen de la sesión>`.

## Al cerrar un sprint

1. Verifica el entregable del sprint contra lo prometido en `PIPELINE.md`.
2. Escribe 3 líneas de retro en la ficha del proyecto: qué salió bien, qué se atrasó, qué cambiar.
3. Activa el sprint siguiente en `PIPELINE.md`.

## Reglas duras

- **Nunca** declarar un proyecto "comercializable" sin cumplir el checklist de `PORTFOLIO.md`.
- **Nunca** iniciar trabajo grande fuera del sprint activo sin decisión explícita de Gustavo.
- Fechas movidas se registran con motivo — el historial de deadlines es un dato, no una vergüenza.
