# %% [markdown]
# ### TEP IA
#
# **Notebook EDA**
#
# # Análisis Exploratorio del Dataset de Iris
#
# ## Objetivo del Proyecto
#
# El objetivo de este análisis es explorar el famoso dataset de sklearn para entender las características de las diferentes especies de flores. Buscaremos identificar patrones en las medidas de los pétalos y sépalos que nos permitan distinguir entre las tres especies: **setosa**, **versicolor** y **virginica**. Realizaremos un resumen estadístico y visualizaciones clave para lograr este entendimiento.
#
# ## Visualizaciones
#
# A continuación, presentamos dos visualizaciones para explorar las relaciones entre las variables y las especies.
#
# 1.  **Gráfico de dispersión (Scatter Plot):** Muestra la relación entre la longitud y el ancho de los sépalos, coloreados por especie. Esto nos ayudará a ver si hay agrupaciones visuales.
# 2.  **Gráfico de violín (Violin Plot):** Muestra la distribución de la longitud de los pétalos para cada especie, ofreciendo una visión de la densidad y el rango de valores.
#
# ## Limpieza y Transformación de Datos
#
# El dataset de Iris ya está notablemente limpio y no requiere una limpieza exhaustiva. Sin embargo, hemos realizado una transformación clave para facilitar el análisis:
#
# -   **Transformación de la columna `target`:** La columna numérica original `target` ha sido transformada a la columna `species`, que contiene los nombres de las especies (`setosa`, `versicolor`, `virginica`). Esto hace que el análisis sea más intuitivo y las visualizaciones más informativas. No se detectaron valores nulos o atípicos significativos que requieran una limpieza adicional.
#
# ## IMPORTANTE... !!!!
#
# Se comentan las lineas de codigo para la generación de gráfico debido a que en los REQUISITOS Y PASOS, usted indica que en el lietral D: NO EMBEBER IMAGENES PESADAS EN EL .ipynb


import matplotlib.pyplot as plt

# %%
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

# Cargar el dataset de Iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["species"] = iris.target_names[iris.target]

# Resumen estadístico
print("Resumen estadístico del dataset:")
print(df.describe())

# Ver las primeras 5 filas
print("\nPrimeras 5 filas del dataset:")
print(df.head())

# Visualización 1: Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x="sepal length (cm)", y="sepal width (cm)", hue="species", data=df)
plt.title("Longitud vs. Ancho del Sépalo por Especie")
plt.xlabel("Longitud del Sépalo (cm)")
plt.ylabel("Ancho del Sépalo (cm)")
plt.show()

# Visualización 2: Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x="species", y="petal length (cm)", data=df)
plt.title("Distribución de la Longitud del Pétalo por Especie")
plt.xlabel("Especie")
plt.ylabel("Longitud del Pétalo (cm)")
plt.show()
