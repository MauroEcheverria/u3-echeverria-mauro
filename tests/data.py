import pandas as pd
from sklearn.datasets import load_iris


def load_and_prepare_iris_data():
    """
    Carga el dataset de Iris, lo convierte en un DataFrame de pandas
    y añade una columna de nombres de especies.

    Retorna:
        pd.DataFrame: Un DataFrame con los datos de Iris.
    """
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df["species"] = iris.target_names[iris.target]
    return df


if __name__ == "__main__":
    # Este bloque solo se ejecuta cuando el script se corre directamente
    df = load_and_prepare_iris_data()

    # Aquí puedes mantener la lógica de visualización y análisis
    import matplotlib.pyplot as plt
    import seaborn as sns

    print("Resumen estadístico del dataset:")
    print(df.describe())
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
