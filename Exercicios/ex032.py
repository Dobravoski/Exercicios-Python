from datetime import date
a = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0: #Essas são as condições para ser um ano bissexto, todas informações retiradas do goole
    print('Esse ano é bissexto!')
else:
    print('Esse ano NÃO é bissexto!')
