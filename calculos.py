import numpy as np


def calcular_recta(x, y):
    """
    Calcula la pendiente y la ordenada al origen
    utilizando dos puntos.
    """

    x1 = x[0]
    x2 = x[1]

    y1 = y[0]
    y2 = y[1]

    pendiente = (y2 - y1) / (x2 - x1)

    intercepto = y1 - pendiente * x1

    return pendiente, intercepto