from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os

load_dotenv()

driver = webdriver.Chrome()

otrs_triagem_url = os.getenv("otrs_triagem_url")
usuario = os.getenv("usuario")
senha = os.getenv("senha")

"""
acesso ao login 
"""
driver.get(otrs_triagem_url)
input_usuario = driver.find_element(By.ID, "User")
input_usuario.send_keys(usuario)
input_senha = driver.find_element(By.ID, "Password")
input_senha.send_keys(senha)
botao_login = driver.find_element(By.ID, "LoginButton")
botao_login.click()

sleep(60)

"""
busca tabela 
"""
tabela_chamados = driver.find_element(By.CLASS_NAME, "DataTable")
corpo_da_tabela = tabela_chamados.find_element(By.TAG_NAME, "tbody")
lista_chamados = corpo_da_tabela.find_elements(By.TAG_NAME, "tr")

print("passeiaqui")
print(lista_chamados)

for chamado in lista_chamados:
    # title="Triagem
    print(f"1 - : {chamado}")
    chamado_td = chamado.find_elements(By.TAG_NAME, "td")
    
    for coluna in chamado_td:
        try:
            coluna_div = coluna.find_element(By.TAG_NAME, "div")
            print(f"2 - {coluna_div} ----- {coluna_div.text}")
        except NoSuchElementException as e:
            print(f"nao achou a div para o elemento {coluna}")        



driver.close()

sleep(30)

