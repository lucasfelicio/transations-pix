'''
Pipeline principal do projeto
'''

from etl.extract import extract
from etl.trasnform import transform

def full_pipeline(database):
    if extract(database) == 200:
        transform(database)
    else:
        print('Erro na execução do pipeline!')