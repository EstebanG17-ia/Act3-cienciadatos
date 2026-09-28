"""
Actividad: Ajuste de Recta y Predicción Interactiva con Streamlit

Alumno: TU NOMBRE COMPLETO
Matrícula: TU MATRÍCULA
Asignatura: Ciencia de Datos
Fecha: 27/09/2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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