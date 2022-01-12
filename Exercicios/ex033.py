a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um outro número: '))
# De acordo com o vídeo, agora vamos chutar um valor menor, depois verificar essa informação
me = a
if b < a and b < c:
    me = b
if c < a and c < b:
    me = c
# Agora o mesmo procedimento, mas com o maior
ma = a
if b > a and b > c:
    ma = b
if c > a and c > b:
    ma = c
# Terminado o procedimento
print(f'O menor valor é {me} e o maior é {ma}')
# Existem outros métodos, como por exemplo as das bibiliotecas, no entanto essa é a maneira mostrada no vídeo
