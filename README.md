# EID de Cálculo Intermedio — Grupo 16

**MAT1188 · 2026 · Distancia recorrida y desplazamiento**

Pregunta central: **¿Por qué integrar velocidad puede dar un resultado distinto
de la distancia total recorrida?**

| Integrante | Cuenta de GitHub |
| --- | --- |
| Juan Ignacio Carrera | `juan-xp` |
| Benjamin De La Fuente | `bedelafuente` |
| Benjamin Aliaga | `BenjaminAliagaMardones` |

Repositorio público: <https://github.com/bedelafuente/eidCalculoIntermedio>

## Resumen del proyecto

El video explica la diferencia entre desplazamiento y distancia con un viaje en
una dimensión: el auto avanza 15 m hacia la panadería, permanece detenido 10 s
y regresa 15 m. La velocidad toma los valores $+1$, $0$ y $-1$ m/s durante 40 s
de tiempo modelado. Por tanto:

$$
\Delta x=15+0-15=0\ \text{m},
\qquad
D=15+0+15=30\ \text{m}.
$$

La rama entregada es `main`. El SHA del código que corresponde al video está
registrado en la [ficha técnica](docs/13-ficha-tecnica-video.md).

## Requisitos

- Python 3.12 o superior.
- Manim Community 0.22.0, fijado en `requirements.txt`.
- Dependencias del sistema requeridas por Manim: Cairo, Pango y FFmpeg. En
  Windows se necesita además una fuente Unicode disponible, como Segoe UI; en
  Linux y macOS pueden usarse DejaVu Sans, Cambria o Noto Sans.
- Ejecutar los comandos desde la raíz del repositorio, la carpeta que contiene
  este `README.md`.

Consulta la [instalación oficial de Manim](https://docs.manim.community/en/stable/installation.html)
si tu sistema no tiene alguna dependencia gráfica.

## Instalación en Windows (PowerShell)

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Si PowerShell bloquea la activación del entorno, revisa la política de ejecución
de scripts de tu usuario y la documentación de Python. También puedes usar
`.venv\Scripts\python.exe` directamente sin activar el entorno.

## Instalación en Linux

Instala Python, FFmpeg, Cairo, Pango y sus paquetes de desarrollo mediante el
gestor de paquetes de tu distribución. Después:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Instalación en macOS

Con Homebrew, instala las dependencias gráficas habituales:

```bash
brew install cairo pango ffmpeg pkg-config
```

Luego crea el entorno e instala Manim:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Ejecutar las pruebas

Las pruebas matemáticas no necesitan Manim y comprueban posiciones, velocidad,
pausa, continuidad, distancia e integrales por tramos:

```bash
python -m unittest discover -s tests -v
```

La salida esperada termina con `OK` y ocho pruebas aprobadas.

## Renderizar las escenas

La escena principal se llama `VideoGrupo16` y está en
`escenas/video_grupo16.py`. El siguiente comando funciona en Windows, Linux y
macOS después de activar el entorno virtual:

```bash
python -m manim -r 1920,1080 --fps 30 escenas/video_grupo16.py VideoGrupo16
```

El archivo se genera en:

```text
media/videos/video_grupo16/1080p30/VideoGrupo16.mp4
```

El render de referencia, a 720p y 15 fps, se obtiene con:

```bash
python -m manim -r 1280,720 --fps 15 escenas/video_grupo16.py VideoGrupo16
```

La escena breve del viaje se ejecuta con:

```bash
python -m manim -ql escenas/viaje_panaderia.py ViajePanaderia
```

Las animaciones no incluyen voces. El audio del video evaluable se graba y se
sincroniza durante la edición final.

## Estructura principal

- `modelo.py`: velocidad, posición, desplazamiento, distancia y etapas del viaje.
- `video_plan.py`: bloques, voces y duración del montaje.
- `escenas/video_grupo16.py`: escena completa, gráfica, rectángulos y contadores.
- `escenas/viaje_panaderia.py`: auto, edificios y recorrido sobre la recta.
- `tests/test_modelo.py`: ocho pruebas del modelo matemático.
- `docs/05-desarrollo-matematico.md`: desarrollo y verificación del ejemplo.
- `docs/10-guion-video.md`: guion y tiempos de narración.
- `docs/13-ficha-tecnica-video.md`: ficha técnica para la entrega.
- `docs/14-checklist-entregables.md`: lista de comprobación final.
- `docs/06-fuentes.md`: referencias y declaración de IA.

## Reproducibilidad y ficha

El código entregado está identificado por el SHA indicado en la ficha técnica.
El generador `herramientas/ficha_avance.py` produce una ficha de avance marcada
como borrador; no sustituye la ficha PDF final:

```bash
python -m pip install -r requirements-documentos.txt
python -m herramientas.ficha_avance
```

La ficha final debe llamarse `MAT1188_EID_G16_2026.pdf` y registrar duración,
enlace público, SHA, referencias y declaración de IA.

## Entrega

Los archivos académicos son:

- `MAT1188_EID_G16_2026.mp4`: video narrado de 4 a 6 minutos.
- `MAT1188_EID_G16_2026.pdf`: ficha técnica.
- `MAT1188_ETICA_G16_2026.pdf`: código de ética, entregado por separado en
  Blackboard.

El MP4 y la ficha se cargan como archivos separados. El repositorio debe ser
público y contener el código correspondiente al SHA anotado en la ficha.

## Documentación y fuentes

- [Tema del grupo 16](docs/04-tema.md).
- [Pauta del EID](docs/01-pauta-proyecto.md).
- [Apunte base: Introducción a la integral](docs/02-introduccion-integral.md).
- [Rúbrica](docs/03-rubrica-evaluacion.md).
- [Fuentes y declaración de IA](docs/06-fuentes.md).
- [Guion completo](docs/10-guion-video.md).
- [Revisión V1–V8](docs/11-revision-video.md).
- [Checklist de entregables](docs/14-checklist-entregables.md).

Los directorios `.venv/`, `media/`, `tmp/`, `audio/` y `output/` son locales o
generados y están excluidos de Git. El archivo en `avances/` es solo un render de
referencia sin audio; no reemplaza al video final.
