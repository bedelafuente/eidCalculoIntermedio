"""Primera escena: un mismo recorrido, dos formas de acumular metros.

Ejecutar desde la raíz: python -m manim -ql escenas/viaje_panaderia.py ViajePanaderia
"""

from manim import (
    DOWN, LEFT, RIGHT, UP, Arrow, Circle, DecimalNumber,
    NumberLine, Polygon, Rectangle, RoundedRectangle, Scene, Text,
    ValueTracker, VGroup, linear,
)

from modelo import (
    FIN_COMPRA, FIN_IDA, POSICION_PANADERIA, TIEMPO_TOTAL,
    desplazamiento, distancia, etapa, posicion,
)


BLANCO = "#F4F7FC"
SUAVE = "#B3C2D6"
AZUL = "#73C9FF"
AMARILLO = "#FFD479"
PANEL = "#192A40"
BORDE = "#344C68"

# Un segundo del modelo ocupa 0,6 s de video en todas las etapas.
# El viaje dura 24 s de video, más presentación y cierre (30 s en total).
SEGUNDOS_VIDEO_POR_SEGUNDO_MODELO = 0.6


def texto(contenido, tamano=24, color=BLANCO, **kwargs):
    """Texto Pango: esta escena puede renderizarse sin una instalación LaTeX."""
    return Text(contenido, font_size=tamano, color=color, **kwargs)


def crear_auto():
    """Auto vectorial propio. El centro horizontal indica su posición."""
    carroceria = RoundedRectangle(
        width=1.05, height=0.31, corner_radius=0.08,
        fill_color=AZUL, fill_opacity=1, stroke_width=0,
    )
    cabina = Polygon(
        [-0.30, 0.10, 0], [-0.18, 0.36, 0],
        [0.16, 0.36, 0], [0.34, 0.10, 0],
        fill_color=AZUL, fill_opacity=1, stroke_width=0,
    )
    ventana = Polygon(
        [-0.21, 0.14, 0], [-0.13, 0.29, 0],
        [0.11, 0.29, 0], [0.23, 0.14, 0],
        fill_color=PANEL, fill_opacity=1, stroke_width=0,
    )
    ruedas = VGroup(*[
        Circle(radius=0.10, fill_color=BLANCO, fill_opacity=1,
               stroke_color=PANEL, stroke_width=3).move_to([x, -0.17, 0])
        for x in (-0.31, 0.31)
    ])
    return VGroup(carroceria, cabina, ventana, ruedas)


def crear_edificio(nombre, punto, color, casa=False):
    cuerpo = Rectangle(
        width=0.85, height=0.55, fill_color=PANEL,
        fill_opacity=1, stroke_color=color, stroke_width=2,
    )
    puerta = Rectangle(
        width=0.18, height=0.30, fill_color=color,
        fill_opacity=0.6, stroke_width=0,
    ).align_to(cuerpo, DOWN)
    if casa:
        techo = Polygon(
            [-0.53, 0.28, 0], [0, 0.64, 0], [0.53, 0.28, 0],
            fill_color=color, fill_opacity=0.5, stroke_color=color,
        )
    else:
        techo = Rectangle(
            width=1.0, height=0.18, fill_color=color,
            fill_opacity=0.6, stroke_width=0,
        ).next_to(cuerpo, UP, buff=0)
    edificio = VGroup(cuerpo, puerta, techo)
    edificio.move_to(punto + UP * 1.12)
    etiqueta = texto(nombre, 22, color).next_to(edificio, UP, buff=0.16)
    return VGroup(edificio, etiqueta)


def crear_contador(titulo, descripcion, funcion, reloj, centro, color):
    tarjeta = RoundedRectangle(
        width=5.35, height=1.55, corner_radius=0.15,
        fill_color=PANEL, fill_opacity=1, stroke_color=BORDE, stroke_width=1,
    ).move_to(centro)
    encabezado = texto(titulo, 23, color).move_to(centro + UP * 0.43)
    aclaracion = texto(descripcion, 16, SUAVE).move_to(centro + DOWN * 0.51)
    numero = DecimalNumber(
        funcion(0), num_decimal_places=1, mob_class=Text,
        font_size=40, color=color,
    )
    unidad = texto("m", 25, color).move_to(centro + RIGHT * 0.87)

    def actualizar(mob):
        mob.set_value(funcion(reloj.get_value()))
        # Anclar el borde derecho evita desplazar la unidad al cambiar de dígitos.
        mob.move_to(centro + LEFT * 0.15)
        mob.align_to(centro + RIGHT * 0.50, RIGHT)

    numero.add_updater(actualizar)
    numero.update()
    return VGroup(tarjeta, encabezado, aclaracion, numero, unidad)


class ViajePanaderia(Scene):
    """Ida, compra y regreso con desplazamiento y distancia sincronizados."""

    def construct(self):
        reloj = ValueTracker(0)
        titulo = texto("¿Volver al inicio significa recorrer cero metros?", 31)
        titulo.to_edge(UP, buff=0.42)
        subtitulo = texto("Un viaje a la panadería · Movimiento en una dimensión", 21, SUAVE)
        subtitulo.next_to(titulo, DOWN, buff=0.18)

        recta = NumberLine(
            x_range=[0, POSICION_PANADERIA, 5], length=10,
            include_numbers=False, include_tip=True,
            color=SUAVE, tick_size=0.09, stroke_width=2,
        ).move_to(DOWN * 0.10)
        marcas = VGroup(*[
            texto(f"{x} m", 20, SUAVE).next_to(recta.n2p(x), DOWN, buff=0.20)
            for x in (0, 5, 10, 15)
        ])
        eje = texto("Posición x (m)", 18, SUAVE).move_to([0, -0.95, 0])
        casa = crear_edificio("Casa", recta.n2p(0), AZUL, casa=True)
        panaderia = crear_edificio("Panadería", recta.n2p(POSICION_PANADERIA), AMARILLO)
        sentido = VGroup(
            texto("Sentido positivo", 17, SUAVE),
            Arrow(LEFT * 0.5, RIGHT * 0.5, buff=0, color=SUAVE, stroke_width=2),
        ).arrange(RIGHT, buff=0.2).move_to([0, 0.95, 0])

        auto = crear_auto()
        auto.add_updater(lambda mob: mob.move_to(
            recta.n2p(posicion(reloj.get_value())) + UP * 0.34
        ))
        auto.update()

        contador_desplazamiento = crear_contador(
            "Desplazamiento acumulado", "Cambio de posición desde la casa",
            desplazamiento, reloj, [-2.85, -2.05, 0], AZUL,
        )
        contador_distancia = crear_contador(
            "Distancia acumulada", "Todo lo recorrido, sin cancelar tramos",
            distancia, reloj, [2.85, -2.05, 0], AMARILLO,
        )

        etiqueta_tiempo = texto("Tiempo del viaje:", 18, SUAVE).move_to([-0.80, 1.88, 0])
        numero_tiempo = DecimalNumber(
            0, num_decimal_places=1, mob_class=Text, font_size=25, color=BLANCO,
        )

        def actualizar_tiempo(mob):
            mob.set_value(reloj.get_value()).move_to([1.03, 1.88, 0])

        numero_tiempo.add_updater(actualizar_tiempo)
        numero_tiempo.update()
        unidad_tiempo = texto("s", 20, SUAVE).move_to([1.7, 1.88, 0])

        mensajes = {
            "ida": "IDA · v = +1 m/s · Ambos contadores aumentan",
            "compra": "COMPRA · v = 0 m/s · El auto y los contadores se detienen",
            "regreso": "REGRESO · v = −1 m/s · Baja el desplazamiento; aumenta la distancia",
            "fin": "LLEGADA · v = 0 m/s · Desplazamiento: 0 m | Distancia: 30 m",
        }
        estados = VGroup()
        for nombre, mensaje in mensajes.items():
            rotulo = texto(mensaje, 22).move_to([0, -3.25, 0])
            rotulo.add_updater(
                lambda mob, nombre=nombre: mob.set_opacity(
                    1 if etapa(reloj.get_value()) == nombre else 0
                )
            )
            rotulo.update()
            estados.add(rotulo)

        self.add(
            titulo, subtitulo, recta, marcas, eje, casa, panaderia, sentido,
            auto, contador_desplazamiento, contador_distancia,
            etiqueta_tiempo, numero_tiempo, unidad_tiempo, estados,
        )
        self.wait(2)
        # Linear evita aceleraciones visuales que contradigan la velocidad constante.
        # El mismo reloj controla todas las representaciones, también durante la compra.
        for inicio, fin in ((0, FIN_IDA), (FIN_IDA, FIN_COMPRA), (FIN_COMPRA, TIEMPO_TOTAL)):
            self.play(
                reloj.animate.set_value(fin),
                run_time=(fin - inicio) * SEGUNDOS_VIDEO_POR_SEGUNDO_MODELO,
                rate_func=linear,
            )
        # Fijar exactamente el final también actualiza el estado de llegada.
        reloj.set_value(TIEMPO_TOTAL)
        self.wait(4)
