"""
Módulo de tranformação do arquivo CSV armazenado no diretório .data/input
e gravação no diretório .data/output.
"""
import pandas as pd


def transform_data(data_base: str):
    """
    Função para realizar a transformação dos dados extraidos do diretório .data/input
    e gravação no diretório .data/output.

    Input: data_base (str) - Ano e Mês (YYYYMM).
           file (str) - Diretório de armazenamento dos dados extraidos.

    Return: df (DataFrame) - DataFrame com os dados transformados.
    """
    filename = '.data/input/transations-pix-{}.csv'.format(data_base)

    try:
        df = pd.read_csv(filename)

        df['AnoMes'] = df['AnoMes'].astype(str)
        df['Ano'] = df['AnoMes'].str[:4]
        df['Mes'] = df['AnoMes'].str[4:]
        df = df.drop(['AnoMes'], axis=1)

        return df

    except Exception as e:
        raise Exception('Erro no módulo de transformação: {}'.format(e))
