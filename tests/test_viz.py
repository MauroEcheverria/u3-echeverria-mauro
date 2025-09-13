from unittest.mock import patch

from viz import create_pair_plot, create_sepal_length_histogram, load_iris_data


def test_load_iris_data_columns():
    """Verifica que las columnas del DataFrame sean las correctas."""
    df = load_iris_data()
    expected_cols = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "species",
    ]
    assert list(df.columns) == expected_cols


def test_load_iris_data_shape():
    """Verifica que el DataFrame de Iris tenga la forma esperada (150 filas, 5 columnas)."""
    df = load_iris_data()
    assert df.shape == (150, 5)


@patch(
    "viz.plt.show"
)  # "Mockea" (simula) la función plt.show para que el gráfico no se muestre
def test_create_sepal_length_histogram(mock_show):
    """
    Verifica que la función del histograma se ejecute sin errores.
    No se comprueba el gráfico en sí, sino que la función no falle.
    """
    df = load_iris_data()
    create_sepal_length_histogram(df)
    mock_show.assert_called_once()  # Se asegura de que plt.show fue llamado una vez


@patch("viz.plt.show")
def test_create_pair_plot(mock_show):
    """
    Verifica que la función del pair plot se ejecute sin errores.
    """
    df = load_iris_data()
    create_pair_plot(df)
    mock_show.assert_called_once()
