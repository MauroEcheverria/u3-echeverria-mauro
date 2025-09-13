from data import load_and_prepare_iris_data


def test_dataframe_shape():
    """
    Verifica que el DataFrame de Iris tenga la forma esperada (150 filas, 5 columnas).
    """
    df = load_and_prepare_iris_data()
    assert df.shape == (150, 5)


def test_column_names():
    """
    Verifica que las columnas del DataFrame sean las esperadas.
    """
    df = load_and_prepare_iris_data()
    expected_columns = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "species",
    ]
    assert list(df.columns) == expected_columns


def test_species_column_values():
    """
    Verifica que los valores en la columna 'species' sean los correctos.
    """
    df = load_and_prepare_iris_data()
    unique_species = df["species"].unique().tolist()
    expected_species = ["setosa", "versicolor", "virginica"]
    assert sorted(unique_species) == sorted(expected_species)
