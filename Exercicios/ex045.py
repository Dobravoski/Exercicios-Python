from random import randint
from time import sleep
print('\033[1;33m--' * 4)
print('\033[1;31mJOKENPô')
print('\033[1;33m--' * 4)
c = randint(0, 2)
i = ('Papel', 'Pedra', 'Tesoura')
print(""" Suas opções:
[ 0 ] PAPEL
[ 1 ] PEDRA
[ 2 ] TESOURA
""")
j = int(input('Sua jogada: '))
print('\033[1;31mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(0.5)
print('=-' * 11)
print(f'\033[1;32mComputador jogou {i[c]}')
print(f'Jogador jogou {i[j]}')
print('\033[1;31m=-' * 11)
if c == j:
    print('\033[1;33mEMPATE!')
elif (c == 0 and j == 1) or (c == 1 and j == 2) or (c == 2 and j == 1) or (c == 2 and j == 0):
    print('\033[1;33mCOMPUTADOR GANHOU!')
elif (j == 0 and c == 1) or (j == 1 and c == 2) or (j == 2 and c == 1) or (j == 2 and c == 0):
    print('\033[1;33mJOGADOR GANHOU!')
