"""Comprobaciones físicas y matemáticas del ejemplo, sin necesitar Manim."""

import unittest

from modelo import desplazamiento, distancia, etapa, posicion, velocidad


class ModeloViajeTest(unittest.TestCase):
    def test_hitos_del_documento(self):
        for t, x, d in ((0, 0, 0), (15, 15, 15), (25, 15, 15), (40, 0, 30)):
            with self.subTest(t=t):
                self.assertEqual(posicion(t), x)
                self.assertEqual(desplazamiento(t), x)
                self.assertEqual(distancia(t), d)

    def test_velocidad_y_etapa_en_los_cambios(self):
        casos = (
            (0, 1, "ida"), (14.999, 1, "ida"), (15, 0, "compra"),
            (24.999, 0, "compra"), (25, -1, "regreso"),
            (39.999, -1, "regreso"), (40, 0, "fin"),
        )
        for t, v, nombre in casos:
            with self.subTest(t=t):
                self.assertEqual(velocidad(t), v)
                self.assertEqual(etapa(t), nombre)

    def test_durante_la_compra_no_hay_movimiento_ni_distancia_extra(self):
        for t in (15, 17.5, 20, 24.99, 25):
            self.assertEqual(posicion(t), 15)
            self.assertEqual(distancia(t), 15)

    def test_regreso_acumula_distancia_mientras_disminuye_desplazamiento(self):
        self.assertEqual(desplazamiento(32.5), 7.5)
        self.assertEqual(distancia(32.5), 22.5)

    def test_continuidad_en_los_cambios(self):
        for funcion in (posicion, desplazamiento, distancia):
            for t in (15, 25):
                self.assertAlmostEqual(funcion(t - 1e-7), funcion(t), places=6)
                self.assertAlmostEqual(funcion(t + 1e-7), funcion(t), places=6)

    def test_distancia_no_disminuye_y_acota_magnitud_del_desplazamiento(self):
        anterior = 0
        for i in range(401):
            t = i / 10
            actual = distancia(t)
            self.assertGreaterEqual(actual, anterior)
            self.assertGreaterEqual(actual, abs(desplazamiento(t)))
            anterior = actual

    def test_integrales_por_rectangulos_coinciden_con_los_contadores(self):
        # Intervalos de 0,5 s; los puntos medios evitan los saltos de velocidad.
        suma_con_signo = suma_magnitudes = 0
        for i in range(80):
            aporte = velocidad((i + 0.5) * 0.5) * 0.5
            suma_con_signo += aporte
            suma_magnitudes += abs(aporte)
            self.assertAlmostEqual(suma_con_signo, desplazamiento((i + 1) * 0.5))
            self.assertAlmostEqual(suma_magnitudes, distancia((i + 1) * 0.5))

    def test_rechaza_tiempos_fuera_del_modelo(self):
        for funcion in (velocidad, posicion, desplazamiento, distancia, etapa):
            for t in (-1, 40.01, float("nan"), float("inf"), -float("inf")):
                with self.subTest(funcion=funcion.__name__, t=t):
                    with self.assertRaises(ValueError):
                        funcion(t)


if __name__ == "__main__":
    unittest.main()
