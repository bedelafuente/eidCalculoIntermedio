# EID de Cálculo Intermedio - Grupo 16

**MAT1188 · 2026 · Distancia recorrida y desplazamiento**

Pregunta central: **¿Por qué integrar velocidad puede dar un resultado distinto de la distancia total recorrida?**

| Integrante | Cuenta de GitHub |
| --- | --- |
| Juan Ignacio Carrera | Pendiente de confirmar |
| Benjamin De La Fuente | Pendiente de confirmar |
| Benjamin Aliaga | Pendiente de confirmar |

Este clon tiene como remoto [bedelafuente/eidCalculoIntermedio](https://github.com/bedelafuente/eidCalculoIntermedio).
La configuración local de autor es `juan-xp`. El avance se desarrolla en
**[dev/grupo-16-video](https://github.com/bedelafuente/eidCalculoIntermedio/tree/dev/grupo-16-video)**,
creada directamente desde `main` en `63340b53e2e9a254c9f776b79662915afaf3ff1b`.

## Avance del video

La [base visual de cinco minutos](avances/grupo16_base_sin_audio.mp4) contiene
presentación, conceptos, ejemplo, animaciones de Manim, cálculos, respuesta y
créditos. **No tiene audio y todavía no es el MP4 final de evaluación.**
Los nombres que aparecen en las escenas identifican la voz prevista en el guion.

El ejemplo es un viaje a la panadería: 15 m de ida, 10 s de compra y 15 m de
regreso. La velocidad toma valores +1, 0 y -1 m/s. El viaje modelado dura 40 s:
**desplazamiento = 0 m; distancia recorrida = 30 m**.

- [Guion completo, cálculos y tiempos para las tres voces](docs/10-guion-video.md).
- [Criterios V1-V8 y pendientes del video](docs/11-revision-video.md).
- [Estado del avance y verificaciones](docs/12-estado-del-avance.md).
- [Ficha técnica del video](docs/13-ficha-tecnica-video.md).
- [Checklist de entregables](docs/14-checklist-entregables.md).
- [Identificación de los tres PDF y alcance exclusivo del grupo 16](docs/09-documentos-y-alcance.md).
- [Fuentes, recursos y declaración de IA](docs/06-fuentes.md).

Se considera únicamente la rúbrica del **video, V1-V8, hasta 40 puntos**.
Los apartados de defensa oral no forman parte de este avance.

## Entorno y dependencias

Entorno verificado para este avance: **Windows, Python 3.14.0, Manim Community
0.22.0**, PyAV 19.0.1. La escena inicial también había sido comprobada con
Python 3.11.15 en macOS. `requirements.txt` fija Manim en 0.22.0.

Instalar las dependencias del sistema indicadas en la
[documentación oficial de Manim](https://docs.manim.community/en/stable/installation.html).
Para el video completo se necesita una de estas fuentes Unicode: **Segoe UI,
DejaVu Sans, Cambria o Noto Sans**. Se usa la primera disponible, en ese orden.
En el render de Windows se utilizó Segoe UI. Las escenas usan Pango y figuras
vectoriales propias; no necesitan LaTeX, música, imágenes ni descargas en ejecución.

Ejemplo de instalación en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

En macOS/Linux, activar con `source .venv/bin/activate`. En macOS pueden ser
necesarios Cairo y Pango mediante Homebrew. Ejecutar los comandos desde la raíz.

## Renderizar las escenas

Base completa a 720p y 15 fps, igual al avance incluido:

```powershell
python -m manim -r 1280,720 --fps 15 escenas/video_grupo16.py VideoGrupo16
```

Resultado: `media/videos/video_grupo16/720p15/VideoGrupo16.mp4`, sin audio.
Los diez bloques están definidos en [video_plan.py](video_plan.py):
20 + 35 + 20 + 30 + 35 + 35 + 35 + 35 + 35 + 20 = **300 segundos**.
El reloj del viaje y el de la gráfica usan 0,6 s de video por segundo del modelo.
La posición y la gráfica simultáneas se sincronizan con el mismo `ValueTracker`.

Exportación de mayor resolución para edición:

```powershell
python -m manim -r 1920,1080 --fps 30 escenas/video_grupo16.py VideoGrupo16
```

Resultado: `media/videos/video_grupo16/1080p30/VideoGrupo16.mp4`, sin audio.
Esta exportación se ofrece como comando reproducible; el avance verificado es
el render 720p15. Conservar los tiempos del guion al incorporar las voces.

Clip inicial independiente, 30 s:

```powershell
python -m manim -ql escenas/viaje_panaderia.py ViajePanaderia
```

Resultado: `media/videos/viaje_panaderia/480p15/ViajePanaderia.mp4`.
[Guion y detalles del clip](docs/08-escena-viaje.md).

## Código y comprobación matemática

- [modelo.py](modelo.py): velocidad, posición, desplazamiento, distancia y etapas.
- [escenas/video_grupo16.py](escenas/video_grupo16.py): montaje completo, gráfica,
  rectángulos y comparación de integrales.
- [escenas/viaje_panaderia.py](escenas/viaje_panaderia.py): auto, edificios y contadores.
- [Desarrollo matemático](docs/05-desarrollo-matematico.md).

```powershell
python -m unittest discover -s tests -v
```

Las ocho pruebas no requieren Manim. Comprueban hitos, pausa, continuidad,
crecimiento de la distancia e integrales por rectángulos. Se ejecutaron
correctamente en el entorno de este avance. El render se revisó con metadatos
y fotogramas: 4500 cuadros, aproximadamente 300 s, 1280 × 720 y cero pistas de audio.

## Ficha y entrega

El generador opcional produce una **ficha PDF de avance marcada como borrador**:

```powershell
python -m pip install -r requirements-documentos.txt
python -m herramientas.ficha_avance
```

Resultado: `output/pdf/MAT1188_EID_G16_2026_borrador.pdf`. Registra el SHA de `HEAD`
al ejecutarse; también acepta `--sha` con un commit de 40 caracteres. Usar un
commit publicado que corresponda al código, sin cambios pendientes.
El PDF generado no se añade a Git y no sustituye la ficha final.

Para completar la entrega, todavía se necesitan las cuentas de GitHub, las voces
reales de los tres integrantes, sincronización y mezcla, revisión del video con
audio y ficha definitiva. Cada voz debe explicar matemáticas, además de
presentarse. Los entregables finales se llaman:

- `MAT1188_EID_G16_2026.mp4`: video narrado de 4-6 minutos.
- `MAT1188_EID_G16_2026.pdf`: ficha con integrantes, cuentas, tema, pregunta,
  duración real, enlace público, SHA del código final, referencias y declaración de IA.

La pauta indica entrega final el **18 de octubre de 2026 a las 23:59**, en
Blackboard, con MP4 y ficha separados. El equipo debe confirmar la entrega y
aceptación del PDF de ética independiente. Este avance no realiza esa entrega.

## Documentos base del repositorio

- [Tema del grupo 16](docs/04-tema.md).
- [Pauta del EID](docs/01-pauta-proyecto.md).
- [Apunte: Introducción a la integral](docs/02-introduccion-integral.md).
- [Transcripción de la rúbrica](docs/03-rubrica-evaluacion.md), que conserva ambos
  componentes del original; aquí se utilizan solo V1-V8.
- [Prompt previo de NotebookLM](docs/07-prompt-notebooklm.md), apoyo de estudio
  con otro ejemplo; no es el guion del video evaluado.

`media/`, `tmp/`, `audio/`, `output/` y `.venv/` se generan localmente y están
excluidos de Git. Solo la base seleccionada en `avances/` se publica como muestra.
