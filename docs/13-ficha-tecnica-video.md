# Ficha técnica del video EID

## Identificación

| Campo | Información |
| --- | --- |
| Asignatura | MAT1188 — Cálculo Intermedio |
| Año | 2026 |
| Grupo | G16 |
| Tema | Distancia recorrida y desplazamiento |
| Pregunta central | ¿Por qué integrar velocidad puede dar un resultado distinto de la distancia total recorrida? |
| Integrantes | Juan Ignacio Carrera; Benjamin De La Fuente; Benjamin Aliaga |
| Cuentas de GitHub | bedelafuente, BenjaminAliagaMardones y juan-xp |
| Repositorio | https://github.com/bedelafuente/eidCalculoIntermedio |
| Rama del código entregado | `main` |
| SHA del código entregado | `857881bb64990a14ce3da663b2d4a193fcb05c72` |

## Descripción del contenido

El video explica la diferencia entre desplazamiento y distancia mediante un
viaje unidimensional a una panadería. El auto recorre 15 m hacia la derecha,
permanece detenido 10 s y regresa 15 m hacia la izquierda. La velocidad por
tramos es $+1$, $0$ y $-1$ m/s durante un tiempo modelado de 40 s.

La integral de la velocidad acumula los aportes con signo:

$$
\Delta x=15+0-15=0\ \text{m}.
$$

La integral de la rapidez acumula magnitudes no negativas:

$$
D=15+0+15=30\ \text{m}.
$$

La respuesta es que el desplazamiento puede anularse cuando el móvil regresa a
su posición inicial, mientras la distancia suma todos los trayectos recorridos.

## Estructura y duración prevista

| Bloque | Contenido | Duración prevista |
| --- | --- | ---: |
| 1 | Presentación, integrantes y pregunta central | 0:20 |
| 2 | Posición, velocidad, rapidez, desplazamiento y distancia | 0:35 |
| 3 | Datos y supuestos del ejemplo | 0:20 |
| 4 | Viaje a la panadería y contadores | 0:30 |
| 5 | Gráfica velocidad-tiempo | 0:35 |
| 6 | Sumas de Riemann y refinamiento | 0:35 |
| 7 | Integral de la velocidad | 0:35 |
| 8 | Integral de la rapidez | 0:35 |
| 9 | Respuesta y comprobación | 0:35 |
| 10 | Créditos y fuentes | 0:20 |
| **Total previsto** |  | **5:00** |

La duración real del archivo exportado es de **5:58**, dentro del rango exigido
de 4 a 6 minutos.

## Especificaciones audiovisuales

| Elemento | Base técnica | Confirmación final |
| --- | --- | --- |
| Formato | MP4 | Listo |
| Resolución del MP4 final | 1920 × 1080 | Listo |
| Render de referencia | 1280 × 720, 15 fps, aproximadamente 300 s, sin audio | Lista |
| Duración exigida | Entre 4 y 6 minutos, incluidos presentación, cierre y créditos | Listo |
| Audio | Tres voces propias, identificadas por nombre, con explicación matemática sustantiva | Listo |
| Animación | Manim Community 0.22.0; Python del entorno documentado en README | Lista |
| Escenas | `escenas/video_grupo16.py`, escena `VideoGrupo16` | `857881bb64990a14ce3da663b2d4a193fcb05c72` |
| Recursos externos | No se usan imágenes, música ni audio externo en la base | Listo |

## Evidencias incluidas en el repositorio

- [Guion completo y distribución temporal](10-guion-video.md).
- [Desarrollo matemático](05-desarrollo-matematico.md).
- [Fuentes y declaración de IA](06-fuentes.md).
- [Revisión de criterios V1–V8](11-revision-video.md).
- [Estado técnico y pendientes](12-estado-del-avance.md).
- [Código de la escena completa](../escenas/video_grupo16.py).
- [Modelo matemático y pruebas](../modelo.py).

## Fuentes y declaración de IA

Las fuentes matemáticas complementarias son OpenStax, *Calculus Volume 1*, y
Grant Sanderson/3Blue1Brown, *Integration and the fundamental theorem of
calculus*. También se utiliza el apunte base del curso y la documentación oficial
de Manim Community. Las referencias completas y los enlaces están en
[06-fuentes.md](06-fuentes.md).

Se declara el apoyo de un asistente de programación de OpenAI y NotebookLM para
comprensión, planificación, redacción, código y revisión. Las voces del video
son propias de los integrantes. Las ideas matemáticas se contrastaron con las
fuentes registradas, el desarrollo del proyecto y las pruebas del modelo.

## Archivos de entrega

- **Video:** `MAT1188_EID_G16_2026.mp4`.
- **Ficha técnica:** `MAT1188_EID_G16_2026.pdf`.
- **Código de ética:** `MAT1188_ETICA_G16_2026.pdf`, entregado por separado en
  la actividad correspondiente de Blackboard.

El video y la ficha técnica se entregan como archivos separados. El repositorio
público contiene el código correspondiente al SHA indicado en esta ficha.
