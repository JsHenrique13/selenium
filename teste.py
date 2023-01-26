from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
from time import sleep
from datetime import datetime


nav = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
nav.maximize_window()
nav.get("https://login.locaweb.com.br/login?service=https%3A%2F%2Fpainel-email.locaweb.com.br%2F")

sleep(10)

user = "assesinuvens"
senha = "t2G87T8Q#!iZYBH"
xuser = "/html/body/main/div/div/section/div/div/form/div[2]/input"
xsenha = "/html/body/main/div/div/section/div/div/form/div[3]/input"
button = "/html/body/main/div/div/section/div/div/form/div[6]/button"
filtrod = "/html/body/div[2]/div/div/div/ul/li[4]/div/input"
site = "piquetcarneiro.ce.gov.br"
addserv = "/html/body/div[2]/div/div/div/a" # click
campodominio = "/html/body/div[2]/div/div/div/div[1]/div[2]/form/div[1]/div[1]/input"
opcpacote = "/html/body/div[2]/div/div/div/div[1]/div[2]/form/div[1]/di2]/select" # primeira opc
confirmar = "/html/body/div[2]/div/div/div/div[1]/div[2]/form/div[2]/input" # click
opc = []
# logar no site locaweb
nav.find_element(By.XPATH, xuser).send_keys(user)
sleep(1)
nav.find_element(By.XPATH, xsenha).send_keys(senha)
sleep(1)
nav.find_element(By.XPATH, button).click()
sleep(1)
nav.find_element(By.XPATH, addserv).click()
sleep(1)
nav.find_element(By.XPATH, campodominio).send_keys("TESTE123")
sleep(1)
options = nav.find_elements(By.TAG_NAME, "option")
for i in options:
    if len(i.text)>17:
        print(i.text)

"""for c in range
    try:
        a = nav.find_element(By.XPATH, f"/html/body/div[2]/div/div/div/div[1]/div[2]/form/div[1]/di2]/select/option[{c}]").text()
        print(a)
        c+=1
    except:
        pass
    else:
        print("nao consegui")
"""
sleep(1)
"""
c = 1
while nav.find_element(By.TAG_NAME, "ul"):
    d = nav.find_element(By.XPATH, f"/html/body/div[2]/div/div/div/div[2]/div/ul/li[{c}]")
    content = d.text
    itens = content.split("\n")
    
    if site != itens[0]:
        c+=1
        continue
    else:
        break
    

# selecionar o dominio 
nav.get("https://painel-email.locaweb.com.br/domains/"+site)


# criar caixa unica

xaddemail = "/html/body/div[2]/div/div/div[1]/section[2]/div[1]/a[1]" # caixa unica
nemail = "input do novo email a ser criado "
xnemail = "/html/body/div[2]/div/div/div/div/form/fieldset/div[1]/input[3]" # endereço novo de email 
nsite = site.split(".")
dia = datetime.today().day
dia = str(dia)
if len(dia) < 2:
    dia = '0'+dia

nsenha = nsite[0].capitalize+"@ssesi"+dia
xnsenha = "/html/body/div[2]/div/div/div/div/form/fieldset/div[5]/label/div/div/div[1]/input" # nova senha
xcriar = "/html/body/div[2]/div/div/div/div/form/fieldset/div[8]/button" # criar email

nav.find_element(By.XPATH, xaddemail).click()
nav.find_element(By.XPATH, xnemail).send_keys(nemail)
nav.find_element(By.XPATH, xnsenha).send_keys(nsenha)
nav.find_element(By.XPATH, xcriar).click()


"""
