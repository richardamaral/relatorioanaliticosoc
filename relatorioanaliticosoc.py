import time
import pyodbc
from selenium import webdriver
from selenium.common import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common import by
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By 
import os
import zipfile
from datetime import datetime, timedelta
import boto3

while True:
    s3 = boto3.client('s3')
    APP = "PARÂMETRO PARA INSERÇÃO"
    SECRET_KEY = "PARÂMETRO PARA INSERÇÃO"

    nome_bucket = "PARÂMETRO PARA INSERÇÃO"

    # CONEXÃO COM BANCO DE DADOS
    cn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=PARÂMETRO PARA INSERÇÃO;DATABASE=PARÂMETRO PARA INSERÇÃO;UID=PARÂMETRO PARA INSERÇÃO;PWD=PARÂMETRO PARA INSERÇÃO')
    cncursor = cn.cursor()

    cncursor.execute("GetDocumentoPCMSOPython")
    # PEGA OS VALORES DE RETORNO DA PROCEDURE GetClientesocPython pra pegar o código soc de todas empresas
    resultados = cncursor.fetchall()

    for linha in resultados:
        try:
            DocumentoPCMSOId = str(linha[1])
            codigoSoc = linha[2]
            senha = ('PARÂMETRO PARA INSERÇÃO')
            driver = webdriver.Chrome()

            driver.get("https://sistema.soc.com.br/WebSoc/")
            driver.maximize_window()  # maximizando a janela
            login = driver.find_element(By.XPATH, '//*[@id="usu"]').send_keys("usuario")  # Colocando o usuario no campo user
            senha = driver.find_element(By.XPATH, '//*[@id="senha"]').send_keys(senha)  # Colocando a senha no campo pass
            time.sleep(0.5)
            # Fazendo a declaração de todos os botões do ID
            botao1 = driver.find_element(By.XPATH, '//*[@id="bt_1"]')
            botao2 = driver.find_element(By.XPATH, '//*[@id="bt_2"]')
            botao3 = driver.find_element(By.XPATH, '//*[@id="bt_3"]')
            botao4 = driver.find_element(By.XPATH, '//*[@id="bt_4"]')
            botao5 = driver.find_element(By.XPATH, '//*[@id="bt_5"]')
            botao6 = driver.find_element(By.XPATH, '//*[@id="bt_6"]')
            botao7 = driver.find_element(By.XPATH, '//*[@id="bt_7"]')
            botao8 = driver.find_element(By.XPATH, '//*[@id="bt_8"]')
            botao9 = driver.find_element(By.XPATH, '//*[@id="bt_9"]')
            botao0 = driver.find_element(By.XPATH, '//*[@id="bt_0"]')
            # Fazendo a declaração de todos os botões do ID
            # VERIFICANDO SE O VALOR DO ATRIBUTO CORRESPONDE AO VALOR DO MEU ID: 6266, PROCURANDO POR TODOS BOTÕES
            # QUANDO ELE ACHAR O BOTÃO DO ID DE VALOR 6 ELE CLICA, 2 ELE CLICA, E ASSIM SUCESSIVAMENTE COMO UM SCAN DOS BOTOES
            def click_button_by_value():
                for i in range(1, 10):  # Loop de 1 a 9
                    xpath = f'//*[@id="bt_{i}"]'
                    button = driver.find_element(By.XPATH, xpath)
                    for i in range(3):
                        if button.get_attribute("value") == "6":
                            button.click()
                            time.sleep(1.5)
                    for i in range(1):
                        if button.get_attribute("value") == "5":
                            button.click()
                            time.sleep(1.5)


            click_button_by_value()
            entrar = driver.find_element(By.XPATH, '//*[@id="bt_entrar"]').click()  # CLICANDO EM ENTRAR

            time.sleep(1.5)
            try:  # TRY PARA PEGAR O ALERTA QUE TRAVA A AUTOMAÇÃO DEPOIS QUE FAZ O LOGIN "Não foi possível carregar o conteúdo"
                wait = WebDriverWait(driver, 10)
                alertasoc = Alert(driver)
                alertasoc.accept()
                print("Alerta OK")
                time.sleep(0.8)
                driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[2]/a/img').click()
            except NoAlertPresentException:
                print('Não foi encontrado nenhum alerta!')

            wait = WebDriverWait(driver, 30)
            iframe = driver.find_element(By.XPATH, '//*[@id="socframe"]')  # MUDANDO O FRAME PRA PODER INTERAGIR COM OS ELEMENTOS DESSE FRAME ESPECIFICO DA PAGINA
            driver.switch_to.frame(iframe)
            time.sleep(0.8)

            try:  # TENTAR ACHAR O CAMPO DE DIGITAR EMPRESA, CASO ACHE ELE ENVIA O QUE ESTÁ ALI DENTRO DOS ('*')
                campoempresa = driver.find_element(By.XPATH, '/html/body/form[1]/div[4]/div[2]/p/input')
                if campoempresa.is_displayed():
                    campoempresa.send_keys(codigoSoc)  #
                else:
                    print('Campo para digitar unidade não localizado!')
            except:
                print('As vezes quando o soc carrega ele não carrega o campo de digitar empresa')

            try:
                campoempresa1 = driver.find_element(By.XPATH, '//*[@id="procuraModalBtn"]/img')
                if campoempresa1.is_displayed():
                    campoempresa1.click()
                else:
                    print('Campo para digitar empresa não localizado!')
            except:
                print('Caso o problema persista contate-me 11 91798-3347')

            time.sleep(1.0)

            try:
                empresaclick = driver.find_element(By.XPATH, '//*[@id="listaemop"]/table/tbody/tr[1]/td[2]/a')
                if empresaclick.is_displayed():
                    empresaname = empresaclick.text
                    empresaclick.click()
                    print("Empresa selecionada:", empresaname)

                else:
                    print('A empresa', (empresaname), 'não foi localizada')

            except:
                print('A empresa', empresaname,
                      'não foi localizada. [Por favor, reinicie o software e tente localiza-la no SOC manualmente!]')
                time.sleep(10000)

            driver.switch_to.default_content()
            campocod111 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/input[1]').click()
            campocod11 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/input[1]').send_keys(Keys.BACKSPACE)
            campocod = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/input[1]').send_keys(int('1292'))
            time.sleep(1.2)
            campocod1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/input[2]').click()
            time.sleep(0.2)
            try:
                iframe1 = driver.find_element(By.XPATH, '/html/body/div[8]/iframe')
                driver.switch_to.frame(iframe1)

                datarelatorioanalitico = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[2]/fieldset/div[1]/div/div/div/input')
                datarelatorioanalitico.clear()

                # campo de conversão da data para um ano anterior
                data_original = linha[4]
                data_formatada = datetime.strptime(data_original, "%Y-%m-%d")
                data_ajustada = data_formatada - timedelta(days=365)
                data_ajustada_formatada = data_ajustada.strftime("%d-%m-%Y")

                data_formatada1 = datetime.strptime(data_original, "%Y-%m-%d")
                data_original_formatada = data_formatada1.strftime("%d-%m-%Y")

                # campo de conversão da data para um ano anterior
            
                datarelatorioanalitico.send_keys(data_ajustada_formatada)
                time.sleep(0.5)
                datarelatorioanalitico.send_keys(data_original_formatada)
                print(data_ajustada_formatada)
                print(data_original_formatada)

                # unidade

                unidade = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[2]/fieldset/div[7]/div/div/div[1]/input').click()
                time.sleep(0.4)
                unidade1 = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[2]/fieldset/div[7]/div/div/div[1]/input').send_keys(linha[7])
                time.sleep(3.8)
                try:
                    unidadeclick = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[2]/fieldset/div[7]/div/div/div[2]/ul/li[1]').click()


                except:
                    print('A unidade: ', linha[7], ' não foi localizada!')
                    driver.close()
                time.sleep(2.6)

                # setor

                setor = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[2]/fieldset/div[8]/div/div/div[1]/input').click()
                time.sleep(0.4)
                setortodos = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[2]/fieldset/div[8]/div/div/div[2]/ul/li[2]/span[1]').click()
                time.sleep(0.4)

                # cargo

                cargo = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[2]/fieldset/div[9]/div/div/div[1]/input').click()
                time.sleep(0.4)
                cargotodos = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[2]/fieldset/div[9]/div/div/div[2]/ul/li[2]').click()
                time.sleep(0.4)

                # retirar checkbox (assinatura, cabeçalho)
                assinatura = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[2]/fieldset/div[10]/div/div/label/span').click()
                time.sleep(0.4)

                cabeçalho = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[2]/fieldset/div[11]/div/div/label/span').click()
                time.sleep(0.4)

                # colocar checkbox (quadro comparativo, origem dos dados)

                quadrocomparativo = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[3]/fieldset[2]/div[7]/div/div/label/span').click()
                time.sleep(0.4)
                origemdosdados = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[4]/fieldset[2]/div[2]/div[7]/div/div/label/span').click()
                time.sleep(1)
                origemdosdados2 = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[5]/fieldset[2]/div[2]/div[7]/div/div/label/span').click()
                time.sleep(1)
                origemdosdados3 = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/section/form/section/div[6]/fieldset[2]/div[2]/div[6]/div/div/label/span').click()
                time.sleep(0.4)
                # gerar documento

                gerardocumento = driver.find_element(By.XPATH, '/html/body/div[4]/div/header/div/div[2]/div[2]/button').click()
                time.sleep(0.6)
                gerardocumentopdf = driver.find_element(By.XPATH, '/html/body/div[4]/div/header/div/div[2]/div[2]/ul/li[1]/a').click()
                time.sleep(1.8)
                # Código pega o texto da mensagem que aparece juntamente com o botão "consultar processo"
                retirarcodigo = driver.find_element(By.XPATH, '/html/body/div[7]/div')
                textodocodigo = retirarcodigo.text
                print(textodocodigo)
                parte_numerica = "".join(filter(str.isdigit, textodocodigo))
                print(parte_numerica)
                time.sleep(1.9)
                clicar = driver.find_element(By.XPATH, '/html/body/div[7]/div/button').click()
                time.sleep(30)

                tabela = driver.find_elements(By.XPATH, '/html/body/div[2]/div/form[1]/table/tbody/tr[2]/td/table/tbody/tr/td//a')
                # Percorra os elementos de link
                for elemento in tabela:
                    texto_link = elemento.text

                    # Verifique se o texto do link corresponde ao código
                    if parte_numerica in texto_link:
                        elemento.click()
                        time.sleep(2.5)
                        botaodownload = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/table[1]/tbody/tr[2]/td[11]/a').click()
                        time.sleep(2.2)
                        driver.close()
                        break
                # Diretório de download (verifique o caminho correto)
                time.sleep(3.5)
                download_dir = "C:/Users/ADMINISTRATOR/Downloads"

                # Nome do arquivo ZIP com o código dinâmico
                zip_filename = "Consulta.zip"

                # Nome desejado para o arquivo PDF extraído
                pdf_filename = DocumentoPCMSOId + "_arquivo_analitico.pdf"

                # Caminho completo para o arquivo ZIP baixado
                zip_path = os.path.join(download_dir, zip_filename)

                # Caminho completo para o arquivo PDF extraído
                pdf_path = os.path.join(download_dir, pdf_filename)

                # Extrair o arquivo PDF do arquivo ZIP
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(download_dir)

                # Renomear o arquivo extraído para o nome desejado
                extracted_pdf_path = os.path.join(download_dir, zip_ref.namelist()[0])
                os.rename(extracted_pdf_path, pdf_path)
                ACCESS_KEY = "PARÂMETRO PARA INSERÇÃO"
                SECRET_KEY = "PARÂMETRO PARA INSERÇÃO"
                s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
                nome_bucket = "PARÂMETRO PARA INSERÇÃO"
                caminho_arquivo_local = "C:/Users/ADMINISTRATOR/Downloads/{}".format(pdf_filename)
                nome_arquivo_s3 = "Cliente/Soc/{}/PCMSO/{}".format(codigoSoc, pdf_filename)
                s3.upload_file(caminho_arquivo_local, nome_bucket, nome_arquivo_s3, ExtraArgs={'ACL': 'public-read'})
                time.sleep(10)
                cncursor.execute("Exec SetDocumentoPCMSOAnaliticoPython @ArquivoAnalitico = ?, @DocumentoPCMSOId = ?",
                                 (pdf_filename, DocumentoPCMSOId))
                cn.commit()
                time.sleep(0.3)

                # CÓDIGO PARA APAGAR O ARQUIVO ZIP E PDF ANTERIORES
                removerarquivopdf = os.remove(pdf_path)
                removerarquivozip = os.remove(zip_path)
            except:
                print("ocorreu algum problema na execução do programa")
                driver.close()
                time.sleep(4.2)
                continue
        except:
            print('full code except--------------------')
            continue
