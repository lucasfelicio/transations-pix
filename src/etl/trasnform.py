'''
Módulo de tranformação do arquivo CSV armazenado no diretório .data/input
e gravação no diretório .data/output
'''

import pandas as pd
import os

def transform(database:str):
    '''
    Função para realizar a transformação dos dados extraidos do diretório .data/input
    e gravação no diretório .data/output

    Input: database (str) - Ano e Mês (YYYYMM)
    '''
    path = '.data/output/'
    try:
        df = pd.read_csv('.data/input/transations-pix-{}.csv'.format(database))
                
        #df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d')
        
        if not os.path.exists(path):
            os.makedirs(path)
        
        df.to_csv(path + 'transations-pix-202301.csv', index=False)

        
    except Exception as e:
        print('Erro ao realizar a transformação dos dados: {}'.format(e))