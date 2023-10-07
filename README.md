# ⬇️📑 FLUXO DE CRIAÇÃO E DOWNLOAD DE RELATÓRIO ANALÍTICO NO SOC COM PROCEDURE SQL ⬇️📑
![Python Version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![Selenium Version](https://img.shields.io/badge/Selenium-3.141%2B-brightgreen)
![PyODBC Version](https://img.shields.io/badge/PyODBC-4.0.39%2B-brightgreen)

Este projeto oferece uma solução automatizada para o processo de criação, elaboração e download de relatórios analíticos dentro do sistema SOC.
## Funcionalidades


- **INTEGRAÇÃO COM BANCO DE DADOS**: Ao iniciar o código ele tenta conexão com um banco de dados S3 para retornar em uma lista, dados de EMPRESAS que necessitam de um relatório analítico dentro do sistema SOC.

- **AUTENTICAÇÃO SOC e CRIAÇÃO DO RELATÓRIO**: Utilizando o (SELENIUM), me autentico no sistema SOC e entro na empresa utilizando os dados da lista em variáveis para conseguir criar o relatório analítico, após isso ele realiza o download.

- **DOWNLOAD E TRATAMENTO DO ARQUIVO**: Utilizando algumas funções de (OS), juntamente com a biblioteca 'zipfile' eu realizo o tratamento do arquivo extraindo e renomeando para inserção de forma correta no banco de dados S3.

- **REMOÇÃO DO ARQUIVO E INTEGRAÇÃO COM BANCO DE DADOS**: Após executar a sequência de tratamentos com o arquivo, realizo o envio do relatório analítico pro banco de dados S3 em seguida removendo-o do pc. E insiro os dados da iteração que tiver sido concluída em uma lista (feitos) para ele não repetir caso o script feche e seja aberto denovo.

## Como Usar

1. **Configuração do Ambiente**:
   - Certifique-se de ter Python 3.8+ instalado.
   - Instale as bibliotecas necessárias com `pip install selenium pyodbc boto3`.
   - Informe uma chave AWS que retorne uma lista de empresas que vão ser feitas a parte do relatório analítico.
   - Informe o diretório de download na variável correspondente.
   - Informe os seus dados para autenticação no sistema SOC.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests.

## Autor

- Richard Borges do Amaral
