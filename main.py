from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
from time import sleep


def salvardados(itens):
    lista = itens[:]
    try:
        with open('entidades.txt', 'w+') as f:
            for item in lista:
                f.write(f'{item}.\n')
    except:
        print("erro ao inserir dados")


nav = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
nav.get("https://login.locaweb.com.br/login?service=https%3A%2F%2Fpainel-email.locaweb.com.br%2F")
nav.maximize_window()






user = "assesinuvens"
senha = "t2G87T8Q#!iZYBH"
xuser = "/html/body/main/div/div/section/div/div/form/div[2]/input"
xsenha = "/html/body/main/div/div/section/div/div/form/div[3]/input"
addserv = "/html/body/div[2]/div/div/div/a" # click
campodominio = "/html/body/div[2]/div/div/div/div[1]/div[2]/form/div[1]/div[1]/input"

opcpacote = "/html/body/div[2]/div/div/div/div[1]/div[2]/form/div[1]/div[2]/select/option[1]" # primeira opc
# nav.close()
confirmar = "/html/body/div[2]/div/div/div/div[1]/div[2]/form/div[2]/input" # click
filtrod = "/html/body/div[2]/div/div/div/ul/li[4]/div/input"
site = "piquetcarneiro.ce.gov.br"
element = nav.find_element(By.ID, "locawebRecaptcha").get_attribute("data-sitekey")
arquivo = 'entidades.txt'
solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key("90a16344518d3b9cad9a141c44955aa0")
solver.set_website_url("https://login.locaweb.com.br/login?service=https%3A%2F%2Fpainel-email.locaweb.com.br%2F")
solver.set_website_key(element)
#set optional custom parameter which Google made for their search page Recaptcha v2
#solver.set_data_s('"data-s" token from Google Search results "protection"')

#
solver.set_soft_id(0)
dados = []
g_response = solver.solve_and_return_solution()
if g_response != 0:
    # print("g-response: " + g_response)
    nav.find_element(By.XPATH, xuser).send_keys(user)
    sleep(1)
    nav.find_element(By.XPATH, xsenha).send_keys(senha)
    sleep(1)
    nav.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{g_response}'")
    sleep(1)
    nav.find_element(By.XPATH, '/html/body/main/div/div/section/div/div/form/div[6]/button').click()
    # nav.get('https://painel-email.locaweb.com.br/domains/altosanto.ce.gov.br/mailboxes')
    btn = '/html/body/div[2]/div/div/div[1]/table/tbody/tr[1]/td[6]/div/a[2]'
    #     '/html/body/div[2]/div/div/div[1]/table/tbody/tr[2]/td[6]/div/a[2]'
    novasenha = "Altosanto@ssesi07"
    nvsenha = '/html/body/div[2]/div/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[1]/input'
    #          '/html/body/div[2]/div/div/div[1]/table/tbody/tr[2]/td[6]/div/a[2]'
    attsenha = '/html/body/div[2]/div/div/div[1]/div[2]/form/div[2]/button'
    c = 1
    while True:
        try:
            if c == 11:
                nav.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div/div/div[2]/div/div[6]/dir-pagination-controls/div/ul/li[3]').click()
                sleep(3)
                c = 1
                continue
            elif c < 11:
                name = nav.find_element(By.XPATH, f"/html/body/div[2]/div/div/div/div[2]/div/ul/li[{c}]/p/strong").text
                
                sleep(1)
                dados.append(name)
                c += 1
                continue
        except:
            break
    salvardados(dados)

else:
    print("task finished with error " + solver.error_code)


























    

"""
# selecionar o dominio 
# nav.get("https://painel-email.locaweb.com.br/domains/"+site)


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
"""    
while True:
        try:
            if c == 11:
                nav.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div/div/div[2]/div/div[6]/dir-pagination-controls/div/ul/li[3]').click()
                sleep(3)
                c = 1
                continue
            elif c < 11:
                name = nav.find_element(By.XPATH, f"/html/body/div[2]/div/div/div/div[2]/div/ul/li[{c}]/p/strong").text
                dados.append(name)
                c += 1
                continue
        except:
            break
    salvardados(dados)






    while True:
        try:
            if c == 11:
                nav.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[3]/div[1]/ul/li[8]/a').click()
                c = 1
                sleep(2)
                continue
            if nav.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[3]'):
                sleep(1)
                nav.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[1]/table/tbody/tr[{c}]/td[6]/div/a[2]').click()
                sleep(1)
                nav.find_element(By.XPATH, nvsenha).clear()
                sleep(1)
                nav.find_element(By.XPATH, nvsenha).send_keys(novasenha)
                sleep(1)
                nav.find_element(By.XPATH, attsenha).click()
                sleep(1)
                try:
                    if nav.find_element(By.CLASS_NAME, 'help-inline').text == 'Utilize uma senha diferente das 3 últimas':
                        nav.find_element(By.XPATH, '//*[@id="modal_change_pass"]/div/button').click()
                        sleep(2)
                        c += 1
                        continue
                    else:
                        sleep(2)
                        c += 1
                        continue
                except:
                    nav.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/div/button').click()
                    c += 1
                    continue

        except:
            print("erro")
            c += 1
sleep(10000)
"""


