from random import randint
from time import sleep

numeros = []


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(0, 9))
    print('Sorteando 5 valors da lista: ', end='')
    for c in numeros:
        print(c, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somapar():
    s = 0
    for c in numeros:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares: ', end='')
    for c in numeros:
        print(c, end=' ')
        sleep(0.3)
    print(f'temos {s}.')


sorteia()
somapar()
