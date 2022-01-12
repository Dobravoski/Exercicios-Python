from random import randint
from time import sleep
tentativas = 1
print('-=' * 28)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 10! TENTE ADIVINHA-LO!')
print('-=' * 28)
jogador = int(input('EM QUE NÚMERO EU PENSEI? '))
pc = randint(0, 10)
while jogador != pc:
    sleep(0.5)
    print('VOCÊ ERROU, TENTE NOVAMENTE')
    jogador = int(input('EM QUE NÚMERO EU PENSEI? '))
    tentativas += 1
print(f'AEEEEE, VOCÊ ACERTOU, VOCÊ PRECISOU DE {tentativas} PALPITE(S)!')
print(f'O NÚMERO ERA {pc}!')
