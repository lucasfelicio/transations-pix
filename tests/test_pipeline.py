from etl.transform import transform_data


def test_pipeline():
    """
    Função para testar a função transform_data.
    """
    data_base = "202301"
    df = transform_data(data_base)

    assert df.shape[1] == 16
