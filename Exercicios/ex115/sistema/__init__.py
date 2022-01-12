from ex115.imagem import *


def leiaInt(num):
    while True:
        try:
            valorInt = int(input(num))
            return valorInt
        except:
            print('\nInforme um valor inteiro corretamente!')


def criarArquivo():
    try:
        a = open('pessoas.txt')
        a.close()
    except FileNotFoundError:
        a = open('pessoas.txt', 'wt+')
        a.close()
        print('Arquivo criado')
    else:
        print('Arquivo já existente')


def escreverArquivo(txt):
    with open('pessoas.txt', 'at') as pessoas:
        pessoas.write(f'\n{txt}')


def opcoes():
    while True:
        num = telaInicial()
        if num == 1:
            nome = str(input('Nome: ')).strip().capitalize()
            idade = int(input('Idade: '))
            txt = f'{nome}; {idade}'
            escreverArquivo(txt)
        elif num == 2:
            menu()
        elif num == 3:
            print('Você escolheu sair.')
            break
        else:
            print('\033[31mDigite um valor da lista.\033[m')
