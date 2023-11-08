"""pipeline principal do projeto."""

from etl import extract, load, transform


def etl_pipeline(data_base):
    """Função principal do Pipeline ETL."""
    try:
        response = extract.extract_data(data_base)
        if response == 200:
            df = transform.transform_data(data_base)
            load.load_data(df, data_base)
            print("Pipeline ETL concluído com sucesso")
        else:
            print("A requisição HTTP retornou o seguinte status: {}".format(response))
    except Exception as e:
        print("Erro ao realizar o Pipeline ETL -> {}".format(e))


if __name__ == "__main__":
    etl_pipeline("202301")
