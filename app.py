"""
Actividad: Ecuación de la recta como alternativa de predicción
Alumno: Esteban Gomez Estrada
Matrícula: 2403032186
Asignatura: Ciencia de Datos
Fecha: 27/09/2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from calculos import calcular_recta, generar_valores


def mostrar_grafica(x, y, pendiente, intercepto):
    """
    Genera y muestra la gráfica de los puntos
    originales y la recta calculada.
    """

    x_recta = np.linspace(
        x.min(),
        x.max() + 5,
        100
    )

    y_recta = pendiente * x_recta + intercepto

    fig, ax = plt.subplots()

    ax.scatter(
        x,
        y,
        marker="o",
        s=100,
        label="Puntos originales"
    )

    ax.plot(
        x_recta,
        y_recta,
        linewidth=2,
        label="Recta ajustada"
    )

    ax.set_title("Ajuste de la recta")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    ax.grid(True)
    ax.legend()

    st.pyplot(fig)


st.set_page_config(
    page_title="Ajuste de Recta",
)

st.title("Ajuste de Recta y Predicción")

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

    # Leer archivo CSV
    datos = pd.read_csv(archivo)

    st.write("### Datos cargados")
    st.dataframe(datos)

    # Validar columnas
    if "x" not in datos.columns or "y" not in datos.columns:

        st.error(
            "El CSV debe contener las columnas x e y."
        )

    # Validar que solamente existan dos puntos
    elif len(datos) != 2:

        st.error(
            "El CSV debe contener exactamente dos puntos."
        )

    else:

        # Convertir columnas a NumPy
        x = datos["x"].to_numpy(dtype=float)
        y = datos["y"].to_numpy(dtype=float)

        # Validar que los valores de X sean diferentes
        if x[0] == x[1]:

            st.error(
                "Los valores de X no pueden ser iguales."
            )

        else:

            # =====================================
            # CÁLCULO DE LA RECTA
            # =====================================

            pendiente, intercepto = calcular_recta(
                x,
                y
            )

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

            # =====================================
            # GRÁFICA
            # =====================================

            st.subheader(
                "3. Gráfica de la recta"
            )

            mostrar_grafica(
                x,
                y,
                pendiente,
                intercepto
            )

            # =====================================
            # INTERPOLACIÓN Y PREDICCIÓN
            # =====================================

            st.subheader(
                "4. Interpolación y predicción"
            )

            # Generar valores de X
            valores_x = generar_valores(x)

            # Calcular valores de Y
            valores_y = (
                pendiente * valores_x
                + intercepto
            )

            # Crear DataFrame
            tabla = pd.DataFrame({
                "x": valores_x,
                "y proyectado": valores_y
            })

            # Mostrar tabla
            st.write(
                "### Tabla de valores"
            )

            st.dataframe(
                tabla,
                use_container_width=True
            )