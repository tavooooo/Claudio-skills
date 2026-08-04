# Claudio-skills

Repositorio de skills globales para todos los proyectos.

## Proceso de trabajo (aplica a TODO proyecto donde esté este repo)

1. **Planificar antes de codear.** Antes de escribir cualquier línea de código: entender el problema, pensar el enfoque y trazar un plan breve. Las manos van a la obra recién cuando el plan existe. Para trabajos multi-paso, usar la skill `writing-plans`.
2. **Cuestionar la respuesta antes de entregarla.** Ninguna respuesta es definitiva por ser la primera. Antes de darla por terminada: revisarla con ojo crítico, buscarle errores, casos borde y supuestos débiles, y verificarla con evidencia real (ejecutar, renderizar, mirar el output). Ver skills `verification-before-completion` y `fableSkill`.
3. **Responder con resultados, no con procesos.** La primera frase de la respuesta dice qué se logró o qué se encontró. El detalle del "cómo" va después, y solo si aporta. No narrar pasos intermedios ni el recorrido interno.
4. **Cuidar el alcance.** Ceñirse a lo pedido: no agregar features, refactors ni cambios fuera del objetivo acordado. Si algo fuera de alcance parece necesario, proponerlo primero — no hacerlo por iniciativa propia.
5. **Aprender de la experiencia trabajando juntos.** Cuando el usuario corrija un comportamiento o quede clara una preferencia, registrarla en la sección "Lecciones aprendidas" de este archivo (commit directo a `main`), para que las próximas sesiones la apliquen sin repetir el error.

## Lecciones aprendidas

- (2026-07-07) Los entregables HTML deben verse completos **sin JavaScript**: las vistas previas móviles (iOS Quick Look, previews de chat) no ejecutan JS. Pre-renderizar el contenido estático; el JS solo mejora. Ver skill `fableSkill`.
- (2026-07-07) Los links de Artifacts de claude.ai piden login. Para compartir con terceros sin registro, entregar además el archivo autocontenido (HTML/ZIP).
- (2026-07-07) El usuario suele trabajar desde el celular: probar los entregables en viewport móvil y en el flujo real de apertura (vista previa, no navegador).
- (2026-08-03) **Antes de medir o probar cualquier cosa, levantar el entorno y ESPERAR a que responda** — y comprobarlo, no suponerlo. Medir contra un entorno a medio arrancar no da error: da números creíbles y falsos, y se tarda horas en descubrirlo. Tres formas reales de que pase: la base de datos no estaba en pie y se midió la pantalla de error; un servidor viejo ocupaba el puerto y servía HTML que pedía hojas de estilo ya reemplazadas (sin CSS **todo mide diminuto**: una pasada dio 374 problemas inventados); y se midió antes de que el servidor contestara. La comprobación va en un guion que **sale con error** si algo falta, no en un recordatorio. Ejemplo: `scripts/audit-server.sh` en easy-court.
- (2026-08-03) **Un guardián o una prueba que no sabe fallar no sirve.** Después de escribir una comprobación, romperla a propósito y confirmar que salta. Se aplica igual a los guiones de verificación: si el "antes" no está en rojo, el "después" en verde no prueba nada.
- (2026-08-04) **`pkill -f "algo"` se mata a sí mismo.** El shell que lo ejecuta
  lleva ese mismo texto en su línea de comando, así que el patrón se encuentra a
  sí mismo: el `pkill` muere y **todo lo que venía detrás en el comando no llega
  a correr**. Hoy eso dejó viva la caché de compilación que creía borrada, y
  media hora dudando del CSS servido en vez de del comando. Matar por PID
  (`ps -eo pid,cmd`, luego `kill <pid>`), o `pkill -f "patrón" || true` en un
  comando aparte y COMPROBAR después que el proceso ya no está.
- (2026-08-03) **Los contenedores de trabajo remotos son efímeros**: se suspenden al quedar inactiva la sesión y vuelven sin nada corriendo (se reconoce con `uptime` = "up 1 min"). No es un fallo que investigar. Corolario: commitear y pushear seguido, porque lo que no está subido se pierde.

## Convenciones de trabajo

- **Las skills se commitean y pushean directamente a `main`** (instrucción del dueño del repo, 2026-07-07). No usar ramas ni PRs para agregar o editar skills, salvo que el cambio toque algo más que `.claude/skills/`.
- Toda skill nueva o editada sigue el proceso TDD de `writing-skills` (baseline RED con subagente → escribir → GREEN → cerrar loopholes) antes de commitear.
- Las skills se escriben en inglés, con frontmatter `name` + `description` ("Use when..."), en `.claude/skills/<nombre>/SKILL.md`.
- No duplicar contenido entre skills: referenciar con `superpowers:<skill-name>`.
