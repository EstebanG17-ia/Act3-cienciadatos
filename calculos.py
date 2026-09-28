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

    # Calcular la pendiente
    pendiente = (y2 - y1) / (x2 - x1)

    # Calcular la ordenada al origen
    intercepto = y1 - pendiente * x1

    return pendiente, intercepto


def generar_valores(x):
    """
    Genera valores enteros desde el menor valor de X
    hasta cinco valores después del mayor valor de X.
    """

    # Obtener el menor y mayor valor de X
    x_min = int(np.min(x))
    x_max = int(np.max(x))

    # Crear valores enteros para interpolación
    # y predicción
    valores_x = np.arange(
        x_min,
        x_max + 6
    )

    return valores_x