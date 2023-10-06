# ⚙️🔎 FLUXO DE CRIAÇÃO E DOWNLOAD DE RELATÓRIO ANALÍTICO NO SOC COM PROCEDURE SQL 🔎⚙️
![Python Version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![Selenium Version](https://img.shields.io/badge/Selenium-3.141%2B-brightgreen)
![PyODBC Version](https://img.shields.io/badge/PyODBC-4.0.39%2B-brightgreen)

Este projeto oferece uma solução automatizada para o processo de manter sincronia dos dados cadastrais dentro do SOC que foram coletados no eSocial.
## Funcionalidades


- **INTEGRAÇÃO COM BANCO DE DADOS**: Ao iniciar o código ele tenta conexão com um banco de dados S3 para retornar em uma lista, dados de EMPRESAS que necessitam de um relatório analítico dentro do sistema SOC.

- **AUTENTICAÇÃO SOC**: Utilizando o (https://img.shields.io/badge/Selenium-3.141%2B-brightgreen), me autentico no sistema SOC e entro na empresa utilizando os dados da lista em variáveis para conseguir realizar o relatório analítico.

- **INTEGRAÇÃO COM BANCO DE DADOS**: Após executar a parte do relatório analítico, eu insiro a variável que informa o código SOC em uma outra lista para não repetir novamente quando eu reiniciar o script.

## Como Usar

1. **Configuração do Ambiente**:
   - Certifique-se de ter Python 3.8+ instalado.
   - Instale as bibliotecas necessárias com `pip install selenium pyodbc boto3`.
   - Informe uma chave AWS que retorne uma lista de empresas que vão ser feitas a parte do relatório analítico.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests.

## Autor

- Richard Borges do Amaral
