import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris


def load_iris_data():
    """Carga y prepara el dataset de Iris."""
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df["species"] = iris.target_names[iris.target]
    return df


def create_sepal_length_histogram(df):
    """Crea un histograma de la longitud del sépalo."""
    plt.figure(figsize=(12, 6))
    sns.histplot(
        data=df, x="sepal length (cm)", hue="species", kde=True, palette="viridis"
    )
    plt.title("Distribución de la Longitud del Sépalo por Especie")
    plt.xlabel("Longitud del Sépalo (cm)")
    plt.ylabel("Frecuencia")
    plt.show()


def create_pair_plot(df):
    """Crea un pair plot del dataset."""
    sns.pairplot(df, hue="species", palette="viridis")
    plt.suptitle("Relaciones entre Variables por Especie", y=1.02)
    plt.show()


if __name__ == "__main__":
    # Este bloque solo se ejecuta cuando el script se corre directamente
    df = load_iris_data()

    # Generar visualizaciones
    create_sepal_length_histogram(df)
    create_pair_plot(df)
