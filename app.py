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

    datos = pd.read_csv(archivo)

    st.write("### Datos cargados")
    st.dataframe(datos)

    if "x" not in datos.columns or "y" not in datos.columns:
        st.error("El CSV debe contener las columnas x e y.")

    elif len(datos) != 2:
        st.error("El CSV debe contener exactamente dos puntos.")

    else:
        x = datos["x"].to_numpy(dtype=float)
        y = datos["y"].to_numpy(dtype=float)
        
        

        st.success("Archivo cargado correctamente.")
    
    if x[0] == x[1]:
        st.error("Los valores de X no pueden ser iguales.")

    else:
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