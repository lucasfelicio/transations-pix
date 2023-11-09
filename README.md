# Transatios Pix

<img src='/docs/static/ETL.png'>

## Sobre o projeto

Este projeto tem como finalidade praticar os conceitos aprendidos no [Workshop](https://lvgalvaofilho.com/) do meste [Luciano Filho](https://github.com/lvgalvao).

Neste projeto é extraido dados de transações de pix da API dos dados públicos do Banco Central do Brasil (BCB).

### Dentre as principais atividades praticadas estão:

* A criação de estrutura de projeto padronizada;
* Trabalhar com ferramentas de desenvolvimento como pyenv e poetry
* Praticar o versionamento de código
* Criar testes unitários e de integração
* Produzir documentações do código desenvolvido
* Desenvolver automatizações e CI/CD

### Requisitos do projeto
* [Pyenv](https://github.com/pyenv/pyenv/#installation)
* [Poetry](https://python-poetry.org/docs/#installation)

### Instalaçao e configuração

1. Clone o repositório e navegue até ele:

```bash
git clone https://github.com/lucasfelicio/transations-pix.git
cd transations-pix
```

2. Configure a versão do Python utilizada no projeto:

```bash
pyenv install 3.12.0
pyenv local 3.12.0
```

3. Instale as dependências do projeto:

```bash
poetry install
```

4. Ative o ambiente virtual:

```bash
poetry shell
```

Com os passos acima o ambiente está pronto para uso.

5. Para executar o projeto
```bash
task run
```

6. Para ver a documentação do projeto

7. Para executar os testes do projeto
```bash
task test
```

### Documentação

[Transations Pix](https://lucasfelicio.github.io/transations-pix/)
