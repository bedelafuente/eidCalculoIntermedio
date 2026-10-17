# Primera escena: viaje y dos contadores

## Propósito

Mostrar que regresar a la posición inicial puede dar desplazamiento cero con
distancia recorrida positiva. Esta escena implementa el movimiento de las
secciones 2 y 7 del [desarrollo matemático](05-desarrollo-matematico.md).
La gráfica velocidad-tiempo y la visualización de las integrales se incorporan
ahora en `escenas/video_grupo16.py`; véase [el guion completo](10-guion-video.md).

## Reloj y representación

El reloj de Manim (`ValueTracker`) representa tiempo del modelo, en segundos.
La posición del auto, los contadores y el texto de etapa leen ese mismo reloj.
El movimiento es lineal en tiempo dentro de cada tramo: aplicar aceleraciones
visuales cambiaría el significado de las velocidades constantes del ejemplo.

El centro horizontal del auto marca su posición en la recta. La flecha señala
el sentido positivo. La posición disminuye en el regreso: la velocidad negativa
significa movimiento hacia la casa. El dibujo del auto se conserva como símbolo
del móvil, también en el regreso.

La escena usa una escala de **0,6 s de video por cada segundo del modelo**,
incluida la compra. Los 40 s de viaje se representan en 24 s. La presentación
y el cierre mantienen detenido el reloj en 0 s y 40 s, respectivamente.

## Guion sugerido para grabar con voz del equipo

Los tiempos corresponden al clip predeterminado de 30 s. Las frases son una
propuesta que el equipo debe revisar y adaptar al guion completo.

| Tiempo del clip | Imagen | Narración sugerida |
| --- | --- | --- |
| 0–2 s | Casa, panadería y contadores en cero. | «¿Volver al inicio significa recorrer cero metros?» |
| 2–11 s | El auto avanza; ambos contadores aumentan. | «En la ida avanzamos quince metros. El desplazamiento y la distancia aumentan juntos.» |
| 11–17 s | Compra: reloj de 15 a 25 s; auto y contadores quietos. | «Durante la compra pasa el tiempo, pero no sumamos recorrido.» |
| 17–26 s | El auto regresa; un contador baja y el otro sube. | «Al regresar disminuye el desplazamiento. La distancia sigue aumentando porque seguimos recorriendo metros.» |
| 26–30 s | Reloj en 40 s; desplazamiento 0 m y distancia 30 m. | «Volvimos al origen: desplazamiento cero y distancia total de treinta metros.» |

## Comprobación matemática y visual

| Reloj del modelo | Posición | Desplazamiento | Distancia |
| --- | --- | --- | --- |
| 0 s | 0 m | 0 m | 0 m |
| 15 s | 15 m | 15 m | 15 m |
| 25 s | 15 m | 15 m | 15 m |
| 32,5 s | 7,5 m | 7,5 m | 22,5 m |
| 40 s | 0 m | 0 m | 30 m |

La posición y el desplazamiento coinciden numéricamente en este ejemplo porque
`x(0) = 0`; el desplazamiento siempre se calcula como `x(t) - x(0)`.
Las pruebas en `tests/test_modelo.py` contrastan los contadores con sumas de
rectángulos de velocidad y rapidez. Los saltos de velocidad en los límites
de las etapas no son saltos de posición.

Para revisar un render, comprobar que el auto permanece en la panadería
mientras el reloj pasa de 15 a 25 s, que no salta en los cambios de etapa y que
al regresar la distancia sigue creciendo. El clip no incluye audio: las voces
de los integrantes se graban y sincronizan durante la edición del video final.

## Verificación de la implementación

- Ocho pruebas matemáticas ejecutadas correctamente con Python 3.11.15.
- Render completo con Manim Community 0.22.0: 854 × 480, 15 fps, 450 fotogramas,
  duración de 30 s.
- Revisión de fotogramas de compra (20 s del modelo), regreso y llegada:
  etiquetas legibles, pausa en 15 m, acumulaciones opuestas durante el regreso
  y cierre con 0 m de desplazamiento y 30 m de distancia.
- La exportación 1080p y la narración quedan para la edición del video final.
