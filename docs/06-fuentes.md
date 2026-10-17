# Fuentes y apoyos del proyecto

## Fuentes matemáticas complementarias

### Fuentes consultadas para el video completo (17 de octubre de 2026)

1. **Gilbert Strang y Edwin "Jed" Herman.** *Calculus Volume 1*. OpenStax,
   30 de marzo de 2016. Secciones [5.2, The Definite Integral](https://openstax.org/books/calculus-volume-1/pages/5-2-the-definite-integral)
   y [5.4, Integration Formulas and the Net Change Theorem](https://openstax.org/books/calculus-volume-1/pages/5-4-integration-formulas-and-the-net-change-theorem).
   La primera respalda las sumas de Riemann, el área con signo y la integrabilidad
   de funciones con un número finito de saltos. La segunda respalda integrar
   velocidad para desplazamiento y rapidez para distancia. Se verificaron autoría,
   fecha y relaciones en las páginas de la editorial; no se copian sus ejemplos,
   imágenes ni párrafos.
2. **Grant Sanderson, 3Blue1Brown.** *Integration and the fundamental theorem of
   calculus*, lección del 5 de mayo de 2017, adaptación textual de Kurt Bruns.
   [Página del autor](https://www.3blue1brown.com/lessons/integration/).
   Se consultaron las explicaciones de velocidad por intervalo, rectángulos,
   refinamiento y contribuciones negativas. Se usa la idea conceptual, con
   funciones, cifras, dibujos y animaciones propios de este proyecto.

Estas son las dos fuentes complementarias identificadas en los créditos del
montaje completo. Las siguientes entradas conservan el registro de fuentes
seleccionadas durante el trabajo anterior. Selección o consulta por el asistente
no acredita lectura personal de cada integrante.

### 1. Khan Academy

- **Autor institucional:** Khan Academy.
- **Título:** *Problemas de movimiento con integrales: desplazamiento vs. distancia*.
- **Formato:** video en español, disponible en la página oficial de la institución.
- **Fecha:** s. f. (fecha de publicación no verificada).
- **Enlace:** https://es.khanacademy.org/math/eb-6-semestre-bachillerato-nme/x4cf03381641be9b4%3Aaplicaciones-de-la-integral/x4cf03381641be9b4%3Aproblemas-movimiento/v/motion-problems-with-integrals
- **Aporte al proyecto:** interpretación de la integral de velocidad como desplazamiento y de la integral de rapidez como distancia; compensación de aportes positivos y negativos.
- **Aplicación a nuestro ejemplo:** justificar por qué la ida y el regreso producen desplazamiento cero, aunque la distancia total sea 30 m.

### 2. Grant Sanderson — 3Blue1Brown

- **Autor:** Grant Sanderson (3Blue1Brown).
- **Título:** *Integration and the fundamental theorem of calculus | Chapter 8, Essence of calculus*.
- **Formato:** video de YouTube; original en inglés.
- **Año:** 2017.
- **Video:** https://www.youtube.com/watch?v=rfG8ce4nNh0
- **Lección del autor:** https://www.3blue1brown.com/lessons/integration/
- **Aporte al proyecto:** interpretación visual de la integral como acumulación y relación entre velocidad, cambio de posición y área en una gráfica.
- **Aplicación a nuestro ejemplo:** explicar el significado de los rectángulos velocidad-tiempo y la relación entre la función de posición y la velocidad.

Estas fuentes fueron seleccionadas para el proyecto. El registro no acredita por sí solo que todos los integrantes hayan visto los videos; cada integrante debe revisar y comprender las ideas utilizadas.

## Apunte base del curso

- **Autoría:** no identificada en la transcripción disponible; completar desde el original si aparece.
- **Título:** *Introducción a la integral. Apunte base común para el proyecto de investigación y visualización*.
- **Fecha:** s. f. (no indicada en la transcripción).
- **Registro local:** [02-introduccion-integral.md](02-introduccion-integral.md).
- **Aporte:** particiones, sumas de Riemann, integral definida, acumulación y relación con las derivadas.

## Documentación técnica

- **Autor institucional:** Manim Community.
- **Título:** *Manim Community Documentation — Tutorials*.
- **Fecha:** documentación en actualización continua.
- **Enlace:** https://docs.manim.community/en/stable/tutorials/
- **Uso previsto:** construcción y ejecución de las escenas. Registrar la versión instalada y las páginas concretas utilizadas al implementar el código.

### Documentación utilizada en la primera escena

- **Versión implementada:** Manim Community 0.22.0, con Python 3.11.15.
- [Instalación local](https://docs.manim.community/en/stable/installation/uv.html):
  entorno aislado y dependencias del sistema para macOS.
- [ValueTracker](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html):
  reloj común para sincronizar el movimiento y los contadores.
- [Text](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html):
  texto con Pango para ejecutar esta escena sin LaTeX.
- Los enlaces `stable` pueden cambiar de versión; `requirements.txt` fija la
  versión utilizada en el proyecto. El auto y los edificios se construyen con
  figuras vectoriales en el código, sin recursos gráficos externos.

## Apoyo de IA y verificación

- **Asistente de IA de esta conversación:** apoyo para comprender el tema, proponer y revisar ejemplos, redactar el desarrollo matemático y elaborar el prompt para NotebookLM.
- **NotebookLM:** video explicativo utilizado como apoyo de estudio. El usuario indicó haberlo visto; no se ha inspeccionado aquí el video generado.
- **Asistente de programación de OpenAI:** implementación de `modelo.py`, la escena `ViajePanaderia`, sus pruebas
  y la documentación de ejecución y guion del clip, a partir del desarrollo
  matemático del repositorio. La verificación automática contrasta hitos,
  continuidad, pausa, acumulación de distancia e integrales por rectángulos;
  se ejecutaron las ocho pruebas y se generó el MP4 de 30 s a 480p y 15 fps.
  Se revisaron fotogramas de compra, regreso y llegada para comprobar etiquetas,
  posición y contadores sincronizados.
  El equipo debe revisar y comprender el código antes de incorporarlo a la entrega.
- **Prompt registrado:** [07-prompt-notebooklm.md](07-prompt-notebooklm.md). Corresponde al ejemplo inicial $v(t)=t-2$, no al ejemplo final del auto y la panadería.
- **Comprobaciones realizadas en el desarrollo:** áreas de rectángulos, integrales por tramos y diferencia entre posiciones inicial y final. Para el ejemplo actual se obtiene desplazamiento de 0 m y distancia de 30 m; véase [el desarrollo matemático](05-desarrollo-matematico.md).
- **Pendiente del equipo:** contrastar las afirmaciones utilizadas con las fuentes, revisar el texto y documentar las verificaciones efectivamente realizadas por sus integrantes. Ampliar esta declaración si se usa IA para código, imágenes, narración o edición.

El prompt y el video de NotebookLM son apoyos de IA, no sustituyen las fuentes matemáticas complementarias. La entrega final requiere las voces de los integrantes y las escenas de Manim indicadas en la pauta.

### Ampliación: video completo del grupo 16

- **Herramienta:** asistente de programación de OpenAI, sesión del 17 de octubre
  de 2026. **Finalidad:** contrastar los tres PDF, completar el guion y el plan
  temporal, implementar `escenas/video_grupo16.py`, preparar documentación y
  comprobar el render. No se generan ni suplantan las voces de los estudiantes.
- **Partes apoyadas:** `video_plan.py`, la escena completa, guion, matriz V1-V8,
  registro de documentos, instrucciones y ficha de avance.
- **Verificación matemática:** resultados contrastados con áreas de rectángulos,
  posiciones de `modelo.py` y las ocho pruebas existentes. En n=8,16,32 las sumas
  de puntos medios coinciden exactamente con los tramos: 0 m y 30 m.
- **Verificación técnica:** compilación de los módulos, render completo con
  Manim Community 0.22.0, inspección de metadatos y fotogramas. El registro concreto
  del avance se conserva en `12-estado-del-avance.md`.
- **Responsabilidad del equipo:** revisar las afirmaciones, grabar sus propias
  explicaciones, comprobar el montaje con audio y confirmar el uso real de
  NotebookLM y cualquier otro apoyo antes de presentar la declaración final.
- **Recursos:** se reutiliza la escena de panadería del propio repositorio,
  partiendo de `63340b5`; auto, edificios, ejes y áreas son geometría generada por
  código. No se incorpora material audiovisual externo ni música.
- **Documentación técnica adicional consultada:** [Axes](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html),
  [ValueTracker](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html)
  y [documentación oficial 0.22.0](https://docs.manim.community/en/stable/),
  consultadas el 17 de octubre de 2026.
