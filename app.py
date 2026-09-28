"""
Actividad: Ajuste de Recta y Predicción Interactiva con Streamlit

Alumno: Esteban Gomez Estrada
Matrícula: 2403032186
Asignatura: Ciencia de Datos
Fecha: 27/09/2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from calculos import calcular_recta


def mostrar_grafica(x, y, pendiente, intercepto):
    """
    Genera y muestra la gráfica de los puntos
    originales y la recta calculada.
    """

    # Crear valores de X para dibujar la recta
    x_recta = np.linspace(
        x.min(),
        x.max() + 5,
        100
    )

    # Calcular los valores de Y de la recta
    y_recta = pendiente * x_recta + intercepto

    # Crear la figura
    fig, ax = plt.subplots()

    # Mostrar los dos puntos originales
    ax.scatter(
        x,
        y,
        marker="o",
        s=100,
        label="Puntos originales"
    )

    # Mostrar la recta
    ax.plot(
        x_recta,
        y_recta,
        linewidth=2,
        label="Recta ajustada"
    )

    # Configurar la gráfica
    ax.set_title("Ajuste de la recta")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Agregar rejilla
    ax.grid(True)

    # Agregar leyenda
    ax.legend()

    # Mostrar gráfica en Streamlit
    st.pyplot(fig)


st.set_page_config(
    page_title="Ajuste de Recta",
    page_icon="📈"
)

st.title("📈 Ajuste de Recta y Predicción")

st.write(
    "Aplicación para calcular una recta a partir de dos puntos "
    "y realizar predicciones."
)

st.subheader("1. Cargar archivo CSV")

archivo = st.file_uploader(
    "Selecciona un archivo CSV",
    type=["csv"]
)

if archivo is not None:

    # Leer archivo CSV con Pandas
    datos = pd.read_csv(archivo)

    st.write("### Datos cargados")
    st.dataframe(datos)

    # Validar columnas
    if "x" not in datos.columns or "y" not in datos.columns:

        st.error(
            "El CSV debe contener las columnas x e y."
        )

    # Validar cantidad de puntos
    elif len(datos) != 2:

        st.error(
            "El CSV debe contener exactamente dos puntos."
        )

    else:

        # Convertir datos a NumPy
        x = datos["x"].to_numpy(dtype=float)
        y = datos["y"].to_numpy(dtype=float)

        # Validar que X1 y X2 sean diferentes
        if x[0] == x[1]:

            st.error(
                "Los valores de X no pueden ser iguales."
            )

        else:

            # Calcular pendiente y ordenada
            pendiente, intercepto = calcular_recta(x, y)

            st.subheader("2. Cálculo de la recta")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Pendiente (m)",
                    f"{pendiente:.4f}"
                )

            with col2:
                st.metric(
                    "Ordenada al origen (b)",
                    f"{intercepto:.4f}"
                )

            st.write("### Ecuación de la recta")

            st.latex(
                f"y = {pendiente:.4f}x + {intercepto:.4f}"
            )

            # Punto 3
            st.subheader("3. Gráfica de la recta")

            mostrar_grafica(
                x,
                y,
                pendiente,
                intercepto
            )