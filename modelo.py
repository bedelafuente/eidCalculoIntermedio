from math import isfinite

FIN_IDA = 15.0
FIN_COMPRA = 25.0
TIEMPO_TOTAL = 40.0
POSICION_INICIAL = 0.0
POSICION_PANADERIA = 15.0
VELOCIDAD_IDA = 1.0
VELOCIDAD_REGRESO = -1.0


def _validar_tiempo(t: float) -> None:
    if not isfinite(t) or not 0 <= t <= TIEMPO_TOTAL:
        raise ValueError(f"El tiempo debe estar entre 0 y {TIEMPO_TOTAL:g} s.")


def velocidad(t: float) -> float:
    _validar_tiempo(t)
    if t < FIN_IDA:
        return VELOCIDAD_IDA
    if t < FIN_COMPRA or t == TIEMPO_TOTAL:
        return 0.0
    return VELOCIDAD_REGRESO


def posicion(t: float) -> float:
    _validar_tiempo(t)
    if t < FIN_IDA:
        return POSICION_INICIAL + VELOCIDAD_IDA * t
    if t < FIN_COMPRA:
        return POSICION_PANADERIA
    return POSICION_PANADERIA + VELOCIDAD_REGRESO * (t - FIN_COMPRA)


def desplazamiento(t: float) -> float:
    return posicion(t) - POSICION_INICIAL


def distancia(t: float) -> float:
    _validar_tiempo(t)
    if t < FIN_IDA:
        return abs(VELOCIDAD_IDA) * t
    distancia_ida = abs(VELOCIDAD_IDA) * FIN_IDA
    if t < FIN_COMPRA:
        return distancia_ida
    return distancia_ida + abs(VELOCIDAD_REGRESO) * (t - FIN_COMPRA)


def etapa(t: float) -> str:
    _validar_tiempo(t)
    if t < FIN_IDA:
        return "ida"
    if t < FIN_COMPRA:
        return "compra"
    if t < TIEMPO_TOTAL:
        return "regreso"
    return "fin"
