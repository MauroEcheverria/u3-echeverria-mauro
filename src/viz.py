# %% [markdown]
# ### TEP IA
#
# # Construcción de un Modelo de Clasificación Base
#
# ## Objetivo del Modelo
#
# El objetivo de esta sección es utilizar los datos limpios para entrenar un **modelo de machine learning** que pueda predecir la especie de una flor basándose en sus medidas de sépalo y pétalo. Esto nos permitirá validar si las diferencias observadas en el análisis exploratorio son lo suficientemente significativas para una clasificación automática.
#
# ## Explicación del Modelo y Métricas
#
# Se ha elegido un modelo de clasificación **K-Nearest Neighbors (KNN)**, que es un algoritmo simple pero eficaz. Su funcionamiento se basa en la proximidad: predice la especie de una nueva flor en función de las especies de sus **'k' vecinos más cercanos**.
#
# Para evaluar el rendimiento del modelo, utilizamos la **precisión (accuracy)** como métrica. La precisión nos indica el porcentaje de predicciones correctas que el modelo realizó en un conjunto de datos que no vio durante el entrenamiento (conjunto de prueba). Una alta precisión sugiere que el modelo ha aprendido con éxito a diferenciar entre las tres especies de flores de Iris.
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

# Histograma
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x="sepal length (cm)", hue="species", kde=True, palette="viridis")
plt.title("Distribución de la Longitud del Sépalo por Especie")
plt.xlabel("Longitud del Sépalo (cm)")
plt.ylabel("Frecuencia")
plt.show()

# Pair Plot
sns.pairplot(df, hue="species", palette="viridis")
plt.suptitle("Relaciones entre Variables por Especie", y=1.02)
plt.show()
