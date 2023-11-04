'''
Módulo de extração de dados da API dos dados públicos do Banco Central do Brasil (BCB)
'''
import os
import requests
import pandas as pd

def extract(database:str):
    '''
    Função para extrair os dados da API de dados públicos do Banco Central do Brasil (BCB)

    Input: database (str) - Ano e Mês a serem extraidos os dados (YYYYMM)

    Output: status_code (int) - Status da requisição HTTP: 200 - OK, 404 - Not Found
    '''
    path = '.data/input/'
    url = f'https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase=@DataBase)?@DataBase={repr(database)}&$top=50&$format=json'
    
    try:        
        if not os.path.exists(path):
            os.makedirs(path)
        
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json().get('value', [])
            df = pd.DataFrame(data)
            df.to_csv(path + 'transations-pix-{}.csv'.format(database), index=False)
            return response.status_code
        else:
            return response.status_code
    
    except requests.exceptions.RequestException as e:
        return e
    except Exception as e:
        return e


