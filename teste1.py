from datetime import datetime


dia = datetime.today().day
dia = str(dia)
if len(dia) < 2:
    dia = '0'+dia
lista = ["Email Locaweb Basic 200 (utilizando 677 caixas de 681)",
"Email Locaweb Basic 200 (utilizando 332 caixas de 336)",
"Email Locaweb Basic 200 (utilizando 288 caixas de 295)",
"Email Locaweb Initial 100 (utilizando 0 caixas de 100)",
"Email Locaweb Initial 200 (utilizando 397 caixas de 410)",
"Email Locaweb Initial 200 (utilizando 207 caixas de 220)",
"Email Locaweb Initial 200 (utilizando 300 caixas de 300)",
"Email Locaweb Initial 200 (utilizando 189 caixas de 200)"]
dados = list()
num = list()
for i in lista:
    
    a = i.split(" ")
    
    for p in a:
        if p[0].isnumeric():
            dados.append(p)
for item in dados:
    for l in item:
        if l == ")":
            print("tem") 
            item = list(item)
            item.pop()
            num.append("".join(item))
        
            

print(num)
       
