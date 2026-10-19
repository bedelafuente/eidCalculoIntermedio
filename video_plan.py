from dataclasses import dataclass

INTEGRANTES = (
    "Juan Ignacio Carrera",
    "Benjamin De La Fuente",
    "Benjamin Aliaga",
)
CURSO = "MAT1188"
GRUPO = 16
PREGUNTA = (
    "¿Por qué integrar velocidad puede dar un resultado distinto "
    "de la distancia total recorrida?"
)


@dataclass(frozen=True)
class Bloque:
    clave: str
    titulo: str
    duracion: int
    voz: str


BLOQUES = (
    Bloque("presentacion", "Tema y pregunta central", 20, INTEGRANTES[0]),
    Bloque("conceptos", "Posición, velocidad, rapidez y desplazamiento", 35, INTEGRANTES[0]),
    Bloque("datos", "Nuestro modelo de viaje", 20, INTEGRANTES[0]),
    Bloque("viaje", "Un viaje, dos contadores", 30, INTEGRANTES[0]),
    Bloque("grafica", "La velocidad indica el sentido", 35, INTEGRANTES[1]),
    Bloque("riemann", "De pequeños aportes a una integral", 35, INTEGRANTES[1]),
    Bloque("desplazamiento", "Acumular con signo", 35, INTEGRANTES[1]),
    Bloque("distancia", "Acumular magnitudes", 35, INTEGRANTES[2]),
    Bloque("cierre", "Respuesta a la pregunta central", 35, INTEGRANTES[2]),
    Bloque("creditos", "Fuentes, recursos e IA", 20, "Créditos"),
)
DURACION_TOTAL = sum(b.duracion for b in BLOQUES)


def cronograma():
    inicio = 0
    for bloque in BLOQUES:
        fin = inicio + bloque.duracion
        yield inicio, fin, bloque
        inicio = fin
