# EID de Cálculo Intermedio

Tema: desplazamiento y distancia recorrida mediante la integral de la velocidad y de la rapidez.

## Primera escena: viaje a la panadería

`ViajePanaderia` muestra un auto que avanza desde la casa (0 m) a la panadería
(15 m), permanece detenido durante la compra y regresa. Un reloj compartido
sincroniza su posición y los contadores de desplazamiento y distancia acumulada.
El resultado final es **0 m de desplazamiento y 30 m de distancia recorrida**.

La escena dura **30 segundos**: 2 s de presentación, 24 s para representar los
40 s del viaje y 4 s de cierre. Todas las etapas usan la misma escala temporal
(0,6 s de video por segundo del modelo). Es un clip sin narración para integrar
al video final de 4 a 6 minutos.

### Entorno e instalación

- Entorno comprobado: **Python 3.11.15**, **Manim Community 0.22.0**, macOS ARM64.
- La dependencia Python está fijada en [requirements.txt](requirements.txt).
- Esta escena usa texto Pango y figuras vectoriales propias; no requiere LaTeX
  ni imágenes externas.

En macOS, con Python 3.11 y Homebrew disponibles:

```bash
brew install cairo pango pkg-config
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Para otros sistemas, seguir la [instalación oficial de Manim](https://docs.manim.community/en/stable/installation.html)
y luego instalar `requirements.txt` en un entorno virtual de Python 3.11.
Los comandos siguientes se ejecutan desde la raíz del repositorio, con ese
entorno activado.

### Generar el video

Vista previa de baja resolución (480p, 15 fps):

```bash
python -m manim -ql escenas/viaje_panaderia.py ViajePanaderia
```

Archivo resultante: `media/videos/viaje_panaderia/480p15/ViajePanaderia.mp4`.
Para abrirlo automáticamente al terminar, usar `-pql` en lugar de `-ql`.

Exportación para edición (1080p, 60 fps):

```bash
python -m manim -qh escenas/viaje_panaderia.py ViajePanaderia
```

Archivo resultante: `media/videos/viaje_panaderia/1080p60/ViajePanaderia.mp4`.
`media/` y `.venv/` se generan localmente y están excluidos de Git.

### Código, parámetros y comprobaciones

- [modelo.py](modelo.py): velocidad, posición, desplazamiento, distancia y etapas;
  las entradas son segundos dentro de `[0, 40]` y las longitudes son metros.
- [escenas/viaje_panaderia.py](escenas/viaje_panaderia.py): escena `ViajePanaderia`;
  `SEGUNDOS_VIDEO_POR_SEGUNDO_MODELO` controla la escala temporal de las tres etapas.
- [Guion del clip y puntos de revisión](docs/08-escena-viaje.md).

Las comprobaciones matemáticas se ejecutan sin Manim ni dependencias externas:

```bash
python -m unittest discover -s tests -v
```

Verifican los hitos de 0, 15, 25 y 40 s, la pausa, la continuidad de la posición,
el crecimiento de la distancia y la coincidencia con las integrales por rectángulos.

## Desarrollo del proyecto

- [Desarrollo matemático: viaje en auto a la panadería](docs/05-desarrollo-matematico.md).
- [Fuentes y declaración inicial de apoyos de IA](docs/06-fuentes.md).
- [Prompt de NotebookLM utilizado como apoyo de estudio](docs/07-prompt-notebooklm.md).
- [Guion de la primera escena](docs/08-escena-viaje.md).
- [Tema y pregunta central](docs/04-tema.md).
- [Pauta del proyecto](docs/01-pauta-proyecto.md).
- [Apunte base](docs/02-introduccion-integral.md).
- [Rúbrica de evaluación](docs/03-rubrica-evaluacion.md).

Pendiente: completar curso, grupo, integrantes y cuentas de GitHub; gráfica
velocidad-tiempo y conexión visual con las integrales; guion completo,
narraciones de los integrantes y revisión final de referencias y declaración de IA.
