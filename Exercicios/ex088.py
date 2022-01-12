from random import randint
from time import sleep
cont = 0
num = []
print('-' * 18)
print('JOGO DA MEGA SENA')
print('-' * 18)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  SORTEANDO {jogos} jJOGOS -=-=-=')
for c in range(1, jogos + 1):
    num.clear()
    cont = 0
    while True:
        numa = randint(1, 60)
        if numa not in num:
            num.append(numa)
            cont += 1
        if cont >= 6:
            break
    num.sort()
    print(f'JOGO {c}: {num}')
    sleep(0.5)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
