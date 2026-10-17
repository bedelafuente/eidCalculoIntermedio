# Estado del avance del grupo 16

**Fecha:** 17 de octubre de 2026. **Rama:** `dev/grupo-16-video`.

## Preparado

- Tres PDF identificados; tema extraído exclusivamente del grupo 16.
- Rama creada desde `main` en `63340b53e2e9a254c9f776b79662915afaf3ff1b`.
- Visibilidad pública del repositorio confirmada mediante la API de GitHub.
- Integrantes: Juan Ignacio Carrera, Benjamin De La Fuente y Benjamin Aliaga.
- Guion de cinco minutos con explicación matemática sustantiva prevista para cada
  integrante y tiempos de sincronización.
- Diez bloques reproducibles en Manim Community: presentación, conceptos, datos,
  viaje, gráfica sincronizada, sumas de Riemann, integral de velocidad, integral
  de rapidez, respuesta y créditos.
- Fuentes e IA documentadas, matriz V1-V8 y generador de ficha PDF de avance.

## Verificación técnica

Entorno de este avance: **Windows, Python 3.14.0, Manim Community 0.22.0**, PyAV
19.0.1. La escena completa selecciona una fuente Unicode disponible; en este
equipo se usa Segoe UI. No requiere LaTeX ni recursos audiovisuales externos.

- Ocho pruebas de `tests/test_modelo.py` correctas.
- Módulos Python compilados sin errores.
- Render completo de la base: **1280 × 720, 15 fps nominales, 4500 fotogramas,
  aproximadamente 300 s**. El contenedor puede informar unos milisegundos menos
  por la base temporal del codificador.
- La base tiene **cero pistas de audio**: es un material de edición y no el MP4
  final evaluable.
- Ficha PDF de avance generada en dos páginas y revisada visualmente. Lleva la
  indicación de borrador y debe regenerarse después de fijar el commit del avance.
- Revisión de fotogramas de conceptos, datos, compra/regreso, gráfica, rectángulos,
  integrales, cierre y créditos. La revisión inicial detectó glifos ausentes en
  subíndices; se seleccionó explícitamente una fuente Unicode y se regeneró la
  escena. Debe conservarse esa fuente o una equivalente al renderizar de nuevo.

La base se publica como `avances/grupo16_base_sin_audio.mp4`, junto con su código.
Los renders intermedios en `media/`, el audio local y las fichas generadas en
`output/` quedan excluidos de Git. La versión definitiva de la ficha deberá
usar el SHA que corresponda al código del video narrado.

## Pendiente para la entrega evaluable

1. Confirmar las tres cuentas de GitHub y completar el README y la ficha.
2. Cada integrante revisa y graba su explicación con su voz real. La asignación
   del guion puede cambiar por acuerdo del equipo, conservando participación
   matemática sustantiva de los tres e identificación por nombre.
3. Mezclar y sincronizar las grabaciones; comprobar volumen, pronunciación y
   ausencia de cortes. Revisar el video entero con audio.
4. Exportar `MAT1188_EID_G16_2026.mp4`, verificar que abre y que dura 4-6 minutos.
5. Generar la ficha final `MAT1188_EID_G16_2026.pdf` con duración real, repositorio
   público, SHA, fuentes y declaración efectiva de IA; no entregar el borrador.
6. Confirmar entrega y aceptación del PDF de ética independiente. Subir MP4 y
   ficha por separado a Blackboard dentro del plazo de la pauta.

No se ha realizado una entrega a Blackboard ni se acredita participación por
el mero hecho de figurar un nombre en las escenas o en los commits.
