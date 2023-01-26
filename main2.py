from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
from time import sleep


#   FUNÇÕES 

def salvardados(itens):
    lista = itens[:]
    try:
        with open('entidades.txt', 'w+') as f:
            for item in lista:
                f.write(f'{item}.\n')
    except:
        print("erro ao inserir dados")

def nEntidades():
    content = nav.find_element(By.XPATH, conteudo).text
    num = ''
    for l in content: 
        if l.isnumeric():
            num += l
    num_entidades = int(num[-3:])
    return num_entidades

def Login(resp):
    nav.find_element(By.XPATH, xuser).send_keys(user)
    sleep(1)
    nav.find_element(By.XPATH, xsenha).send_keys(senha)
    sleep(1)
    nav.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resp}'")
    sleep(1)
    nav.find_element(By.XPATH, '/html/body/main/div/div/section/div/div/form/div[6]/button').click()

def Pegadados(prox_pag):  
    dados = []  
    c = 1
    while True:
        try:
            if c == 11:
                nav.find_element(By.XPATH, prox_pag).click()
                sleep(2)
                c = 1
                continue
            elif c < 11:
                entidade = nav.find_element(By.XPATH, f"/html/body/div[2]/div/div/div/div[2]/div/ul/li[{c}]/p/strong").text
                caixas = nav.find_element(By.XPATH, f"/html/body/div[2]/div/div/div/div[2]/div/ul/li[{c}]/div[4]/p/strong[2]").text      
                dados.append(f"{entidade}: {caixas}")
                c += 1
                continue
        except:
            break
    return dados[:]


#   CAMPOS PADRÕES

user = "assesinuvens"
senha = "t2G87T8Q#!iZYBH"
xuser = "/html/body/main/div/div/section/div/div/form/div[2]/input"
xsenha = "/html/body/main/div/div/section/div/div/form/div[3]/input"
arquivo = 'entidades.txt'
conteudo = "/html/body/div[2]/div/div/div/div[2]/div/div[6]/dir-pagination-controls/div/ul/li[2]"
prox_pag = "/html/body/div[2]/div/div/div/div[2]/div/div[6]/dir-pagination-controls/div/ul/li[3]"
link = "https://login.locaweb.com.br/login?service=https%3A%2F%2Fpainel-email.locaweb.com.br%2F"

#   INICIAR NAVEGADOR 

nav = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
nav.get(link)
nav.maximize_window() # opcional
element = nav.find_element(By.ID, "locawebRecaptcha").get_attribute("data-sitekey")

#   EXECUÇÃO DO CÓDIGO

while True:
    try:    

        #   CAPTCHA CONFIGURAÇÕES
        solver = recaptchaV2Proxyless()
        # solver.set_verbose(1)
        solver.set_key("90a16344518d3b9cad9a141c44955aa0")
        solver.set_website_url(link)
        solver.set_website_key(element)
        solver.set_soft_id(0)
        c_resposta = solver.solve_and_return_solution() # RESPOSTA DO CAPTCHA

        #   CONDICIONAL DE FUNCIONAMENTO

        if c_resposta != 0:

            # LOGIN
            Login(c_resposta)
            #   LOAD TIME 
            sleep(3)
            #   PEGAR NÚMERO DE ENTIDADES
            num = nEntidades()
            #   PEGAR DADOS DAS ENTIDADES (NOME E NUMERO DE CAIXAS EM USO)
            dados = Pegadados(prox_pag)
            #   SALVAR DADOS NUM TXT
            salvardados(dados)
            #   PEGAR NOME DAS CAIXAS
            lista_ent = list()
            for dado in dados:
                lista_ent.append(dado[:dado.index(":")])
            
            break  
    except Exception as e:
        print(e)
        print("Erro na execução... Tetando novamente...")
        try:
            nav.get(link)
            nav.find_element(By.XPATH, xuser).clear()
            nav.find_element(By.XPATH, xsenha).clear()
        except: pass
        continue

print(lista_ent)


email = "/html/body/div[2]/div/div/div[1]/table/tbody/tr/td[2]"
uso =   "/html/body/div[2]/div/div/div[1]/table/tbody/tr/td[5]"