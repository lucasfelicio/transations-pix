'''
Pipeline principal do projeto
'''

from pipeline.extract import extract

if __name__ == '__main__':
    response = extract('202301')
    print(response)