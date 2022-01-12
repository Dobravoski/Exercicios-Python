from random import randint
from time import sleep
n = randint(0, 5)
print(52 * '-')
print('VOU PENSAR EM UM NÚMERO ENTRE 0 A 5. TENTE ADIVINHAR')
print(52 * '-')
u = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if u == n:
    print('VOCÊ ACERTOU!')
else:
    print('Você errou!')
print(f'O NÚMERO ERA {n}!')
