Ecuación de la recta como alternativa de predicción

Este proyecto es una aplicación realizada en Python utilizando Streamlit.

El programa permite cargar un archivo CSV que contiene dos puntos (x, y) y, a partir de ellos, calcular una recta.

¿Qué hace el programa?

El programa realiza las siguientes acciones:

Permite cargar un archivo CSV.
Comprueba que el archivo tenga las columnas x e y.
Comprueba que existan exactamente dos puntos.
Calcula la pendiente de la recta.
Calcula la ordenada al origen.
Muestra la ecuación de la recta.
Genera una gráfica con los puntos y la recta.
Genera nuevos valores para realizar predicciones.
Muestra los resultados en una tabla.
Tecnologías utilizadas
Python
Streamlit
Pandas
NumPy
Matplotlib
Archivo CSV

El archivo debe tener dos columnas llamadas x e y.

Ejemplo:

x,y
2,5
4,9

Estos datos representan los puntos:

(2,5)
(4,9)
¿Cómo funciona?

Primero se cargan los datos utilizando Pandas. Después, el programa obtiene los valores de los dos puntos y calcula la recta utilizando la fórmula:

y = mx + b

Donde:

m representa la pendiente.
b representa la ordenada al origen.

Después se utiliza Matplotlib para mostrar los puntos y la recta en una gráfica.

Finalmente, se generan nuevos valores de x y se calcula su valor de y para realizar predicciones.

Ejecución

Para ejecutar el programa se utiliza:

streamlit run app.py

Después de ejecutar el comando, la aplicación se abrirá en el navegador.

Objetivo

El objetivo del proyecto es utilizar Python, procesamiento de datos y gráficas para calcular y representar una recta a partir de dos puntos.