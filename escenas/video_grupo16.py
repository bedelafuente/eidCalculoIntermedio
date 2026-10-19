import manimpango

from manim import (
    UP, DOWN, LEFT, Axes, Circle, Dot, FadeIn, Line, NumberLine,
    Polygon, Text, Transform, ValueTracker, VGroup, linear,
)

from escenas.viaje_panaderia import (
    ViajePanaderia, crear_auto, BLANCO, SUAVE, AZUL, AMARILLO,
)
from modelo import posicion, velocidad
from video_plan import BLOQUES, INTEGRANTES


NEGATIVO = "#FF9B9B"
VERDE = "#9BE4BE"
FUENTE = next((nombre for nombre in ("Segoe UI", "DejaVu Sans", "Cambria", "Noto Sans")
               if nombre in manimpango.list_fonts()), None)
if FUENTE is None:
    raise RuntimeError("Instala una fuente Unicode: Segoe UI, DejaVu Sans, Cambria o Noto Sans.")


def texto(contenido, tamano=24, color=BLANCO):
    """La fuente explícita conserva subíndices y límites de las integrales."""
    return Text(contenido, font=FUENTE, font_size=tamano, color=color)


def linea(contenido, y, tamano=27, color=BLANCO):
    obj = texto(contenido, tamano, color).move_to([0, y, 0])
    if obj.width > 12.2:
        obj.scale_to_fit_width(12.2)
    return obj


def ejes_velocidad():
    ejes = Axes(
        x_range=[0, 40, 5], y_range=[-1.5, 1.5, 0.5],
        x_length=10, y_length=3.1, tips=False,
        axis_config={"color": SUAVE, "stroke_width": 2,
                     "include_ticks": False},
    ).move_to([0, 0.1, 0])
    etiquetas = VGroup()
    for t in (0, 15, 25, 40):
        punto = ejes.c2p(t, 0)
        etiquetas.add(Line(punto + DOWN * 0.05, punto + UP * 0.05, color=SUAVE))
        etiquetas.add(texto(str(t), 17, SUAVE).move_to(punto + DOWN * 0.23))
    for v in (-1, 1):
        etiquetas.add(texto(f"{v:+d}", 18, SUAVE).next_to(ejes.c2p(0, v), LEFT, buff=0.15))
    etiquetas.add(texto("v (m/s)", 20, SUAVE).move_to([-5.2, 2.02, 0]))
    etiquetas.add(texto("t (s)", 20, SUAVE).move_to([5.48, -0.22, 0]))
    return ejes, etiquetas


def grafica(ejes, rapidez=False):
    segmentos = VGroup()
    for a, b, v, color in ((0, 15, 1, AZUL), (15, 25, 0, SUAVE),
                           (25, 40, 1 if rapidez else -1, AMARILLO if rapidez else NEGATIVO)):
        segmentos.add(Line(ejes.c2p(a, v), ejes.c2p(b, v), color=color, stroke_width=5))
        segmentos.add(Dot(ejes.c2p(a, v), radius=0.045, color=color))
        segmentos.add(Circle(radius=0.045, color=color, fill_color="#101B2B",
                            fill_opacity=1, stroke_width=2).move_to(ejes.c2p(b, v)))
    # v(40)=0, como en modelo.py; los valores aislados no cambian la integral.
    segmentos.add(Dot(ejes.c2p(40, 0), radius=0.045, color=SUAVE))
    return segmentos


def region(ejes, a, b, altura, color):
    return Polygon(
        ejes.c2p(a, 0), ejes.c2p(b, 0),
        ejes.c2p(b, altura), ejes.c2p(a, altura),
        fill_color=color, fill_opacity=0.3, stroke_color=color, stroke_width=1,
    )


class VideoGrupo16(ViajePanaderia):
    """Los diez bloques comparten el cronograma reproducible de video_plan.py."""

    def cabecera(self, bloque):
        self.clear()
        self.add(linea(bloque.titulo, 3.25, 32))
        self.add(linea(bloque.voz, 2.7, 19, SUAVE))

    def rematar(self, inicio, duracion):
        restante = duracion - (self.time - inicio)
        if restante < -0.1:
            raise ValueError(f"Bloque excedido por {-restante:.2f} segundos")
        if restante > 0:
            self.wait(restante)

    def construct(self):
        for bloque in BLOQUES:
            inicio = self.time
            if bloque.clave == "viaje":
                self.clear()
                self.add_foreground_mobject(linea(bloque.voz, 3.8, 16, SUAVE))
                ViajePanaderia.construct(self)
            else:
                self.cabecera(bloque)
                getattr(self, bloque.clave)()
            self.rematar(inicio, bloque.duracion)

    def presentacion(self):
        self.add(linea("Distancia recorrida y desplazamiento", 1.45, 38, AZUL))
        self.add(linea("MAT1188 · Cálculo Intermedio · Grupo 16 · 2026", 0.7, 24, SUAVE))
        self.add(linea("¿Por qué integrar velocidad puede dar un resultado", -0.2, 28))
        self.add(linea("distinto de la distancia total recorrida?", -0.75, 28))
        for y, nombre in zip((-1.65, -2.15, -2.65), INTEGRANTES):
            self.add(linea(nombre, y, 24, AMARILLO))

    def conceptos(self):
        frases = (
            ("x(t): posición sobre una recta, en metros", 1.7, BLANCO),
            ("v(t): velocidad con signo, en metros por segundo", 0.95, AZUL),
            ("|v(t)|: rapidez, siempre no negativa", 0.2, AMARILLO),
            ("Δx = x(b) − x(a): cambio de posición", -0.55, AZUL),
            ("D: longitud total del recorrido, en metros", -1.3, AMARILLO),
            ("a y b: instantes inicial y final; t: tiempo en segundos", -2.15, SUAVE),
            ("Suponemos movimiento en una dimensión y velocidad integrable", -2.95, SUAVE),
        )
        for frase, y, color in frases:
            self.play(FadeIn(linea(frase, y, 25, color)), run_time=0.5)
            self.wait(2.5)

    def datos(self):
        for contenido, y, color in (
            ("Casa: x(0) = 0 m     Panadería: x = 15 m", 1.6, BLANCO),
            ("IDA       0 ≤ t < 15 s       v = +1 m/s", 0.7, AZUL),
            ("COMPRA   15 ≤ t < 25 s      v = 0 m/s", -0.1, SUAVE),
            ("REGRESO  25 ≤ t < 40 s      v = −1 m/s", -0.9, NEGATIVO),
            ("En t = 40 s el auto se detiene: v(40) = 0", -1.8, SUAVE),
            ("Modelo ideal: cambios instantáneos de velocidad", -2.65, SUAVE),
        ):
            self.add(linea(contenido, y, 26, color))

    def grafica(self):
        ejes, etiquetas = ejes_velocidad()
        self.add(ejes, etiquetas, grafica(ejes))
        reloj = ValueTracker(0)
        punto = Dot(color=VERDE, radius=0.08)
        punto.add_updater(lambda m: m.move_to(ejes.c2p(reloj.get_value(), velocidad(reloj.get_value()))))
        cursor = Line(ejes.c2p(0, -1.4), ejes.c2p(0, 1.4), color=VERDE, stroke_width=1)
        cursor.add_updater(lambda m: m.put_start_and_end_on(
            ejes.c2p(reloj.get_value(), -1.4), ejes.c2p(reloj.get_value(), 1.4)))
        recta = NumberLine(x_range=[0, 15, 5], length=9, include_numbers=False,
                           include_tip=True, color=SUAVE).move_to([0, -2.6, 0])
        auto = crear_auto().scale(0.75)
        auto.add_updater(lambda m: m.move_to(recta.n2p(posicion(reloj.get_value())) + UP * 0.27))
        self.add(linea("Posición del auto x (m) · el mismo reloj controla ambas vistas", -1.9, 20, SUAVE))
        self.add(recta, auto, cursor, punto)
        for x in (0, 5, 10, 15):
            self.add(texto(f"{x} m", 19, SUAVE).next_to(recta.n2p(x), DOWN, buff=0.17))
        self.wait(3)
        for a, b in ((0, 15), (15, 25), (25, 40)):
            self.play(reloj.animate.set_value(b), run_time=(b-a)*0.6, rate_func=linear)
        reloj.set_value(40)

    def riemann(self):
        ejes, etiquetas = ejes_velocidad()
        self.add(ejes, etiquetas, grafica(ejes))
        self.add(linea("Aporte pequeño: v(tᵢ*) Δt     ·     (m/s) × s = m", -1.9, 25, AZUL))
        self.add(linea("Σ v(tᵢ*) Δt  →  ∫₀⁴⁰ v(t) dt   cuando Δt → 0", -2.65, 29))
        self.add(linea("tᵢ*: punto medio · n: cantidad de intervalos · Δt = 40/n", -3.25, 20, SUAVE))
        for n in (8, 16, 32):
            dt = 40 / n
            rectangulos = VGroup()
            for i in range(n):
                a, b = i * dt, (i+1) * dt
                v = velocidad((a+b)/2)
                if v:
                    rectangulos.add(region(ejes, a, b, v, AZUL if v > 0 else NEGATIVO))
            etiqueta = linea(f"n = {n}   ·   Δt = {dt:g} s", 2.15, 23, AMARILLO)
            self.play(FadeIn(rectangulos), FadeIn(etiqueta), run_time=1)
            self.wait(7)
            self.remove(etiqueta)
            if n != 32:
                self.remove(rectangulos)
        self.add(linea("Aquí los cortes coinciden con los tramos: las sumas ya son exactas", 2.15, 20, VERDE))

    def desplazamiento(self):
        ejes, etiquetas = ejes_velocidad()
        self.add(ejes, etiquetas, grafica(ejes))
        positivo = region(ejes, 0, 15, 1, AZUL)
        negativo = region(ejes, 25, 40, -1, NEGATIVO)
        cuenta = linea("Ida: (+1 m/s) × 15 s = +15 m", -2.05, 28, AZUL)
        self.play(FadeIn(positivo), FadeIn(cuenta), run_time=1)
        self.wait(7)
        self.play(Transform(cuenta, linea("Compra: (0 m/s) × 10 s = 0 m", -2.05, 28, SUAVE)), run_time=1)
        self.wait(6)
        self.play(FadeIn(negativo), Transform(cuenta, linea("Regreso: (−1 m/s) × 15 s = −15 m", -2.05, 28, NEGATIVO)), run_time=1)
        self.wait(7)
        self.add(linea("Δx = ∫₀⁴⁰ v(t) dt = 15 + 0 − 15 = 0 m", -2.85, 29, AZUL))
        self.add(linea("Área geométrica: 15 m por región; el aporte inferior lleva signo negativo", 2.15, 20, SUAVE))

    def distancia(self):
        ejes, etiquetas = ejes_velocidad()
        self.add(ejes, etiquetas)
        curva = grafica(ejes)
        positivo = region(ejes, 0, 15, 1, AZUL)
        regreso = region(ejes, 25, 40, -1, NEGATIVO)
        self.add(curva, positivo, regreso)
        self.add(linea("El valor absoluto refleja el tramo negativo sobre el eje", -1.9, 25, AMARILLO))
        self.wait(6)
        self.play(Transform(regreso, region(ejes, 25, 40, 1, AMARILLO)),
                  Transform(curva, grafica(ejes, rapidez=True)),
                  Transform(etiquetas[-2], texto("|v| (m/s)", 20, SUAVE).move_to([-5.2, 2.02, 0])),
                  run_time=3)
        self.wait(4)
        self.add(linea("D = ∫₀⁴⁰ |v(t)| dt = 15 + 0 + 15 = 30 m", -2.65, 29, AMARILLO))
        self.add(linea("|∫₀⁴⁰ v(t) dt| = 0 m    ≠    ∫₀⁴⁰ |v(t)| dt = 30 m", -3.25, 23))

    def cierre(self):
        self.add(linea("La integral de velocidad acumula cambios con signo", 1.65, 28, AZUL))
        self.add(linea("La integral de rapidez suma todo el recorrido", 0.9, 28, AMARILLO))
        self.add(linea("Volvimos a casa: Δx = 0 m     ·     Recorrimos D = 30 m", -0.05, 31))
        self.add(linea("Desplazamiento cero no significa que estuvimos quietos", -0.9, 24, SUAVE))
        self.wait(16)
        self.add(linea("Si solo viajamos en sentido negativo: Δx < 0 y D = |Δx|", -1.85, 25, VERDE))
        self.add(linea("Para obtener la posición final: x(b) = x(a) + ∫ₐᵇ v(t) dt", -2.75, 25))

    def creditos(self):
        for contenido, y, color in (
            ("Strang y Herman · OpenStax · Calculus Volume 1 (2016), §5.2 y §5.4", 1.8, BLANCO),
            ("Grant Sanderson · 3Blue1Brown · Integration and the FTC (2017)", 1.05, BLANCO),
            ("Curso · Introducción a la integral · apunte base, s. f.", 0.3, BLANCO),
            ("Manim Community 0.22.0 · documentación oficial", -0.45, AZUL),
            ("IA de OpenAI: apoyo en guion, código y comprobaciones; NotebookLM: estudio previo", -1.2, SUAVE),
            ("Verificación: áreas por tramos, posición, pruebas y revisión de fotogramas", -1.95, SUAVE),
            ("Referencias, recursos y declaración de IA: docs/06-fuentes.md", -2.7, AMARILLO),
            ("github.com/bedelafuente/eidCalculoIntermedio · rama dev/grupo-16-video", -3.25, SUAVE),
        ):
            self.add(linea(contenido, y, 22, color))
