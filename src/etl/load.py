"""Módulo de carregamento dos datos transformados para o diretório .data/output."""
import os

import pandas as pd


def load_data(df, file: str):
    """
    Função para realizar o carregamento dos dados transformados para o diretório .data/output.

    Input: df (DataFrame) - DataFrame com os dados transformados.
    """
    path = '.data/output/'

    try:
        if not os.path.exists(path):
            os.makedirs(path)

        df.to_csv(
            path + 'trasations-pix-transformed-{}.csv'.format(file),
            index=False,
        )

    except Exception as e:
        raise Exception('Erro no módulo de carregamento: {}'.format(e))
