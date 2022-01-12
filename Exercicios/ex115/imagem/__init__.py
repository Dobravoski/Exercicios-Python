from ex115.sistema import *


def leiaInt(num):
    while True:
        try:
            valorInt = int(input(num))
            return valorInt
        except:
            print('\nInforme um valor inteiro corretamente!')


def linha(total=40):
    print('-' * total)


def titulo(txt):
    linha()
    print(f'{txt:^40}')
    linha()


def telaInicial():
    print('\033[32m')
    titulo('Opções')
    print('\033[31m1     Adicionar pessoas')
    print('2     Ver as pessoas adicionadas')
    print('3     Sair\033[32m')
    linha()
    print('\033[m')
    a = leiaInt('\033[33mResposta: \033[m')
    return a


def menu():
    print('\033[34m')
    titulo('Menu')
    a = open('pessoas.txt', 'rt')
    for cada in a:
        print(f'\033[33m{cada}')
    print('\033[34m')
    linha()
    print('\033[m')
