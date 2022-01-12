def linha(txt):
    s = len(txt) + 4
    print('\033[31m~' * s)
    print(f'  {txt}')
    print('~' * s)
    print('\033[m')


def ajuda():
    while True:
        linha('SISTEMA DE AJUDA PyHelp')
        pergunta = str(input('\033[34mBibilioteca ou função: \033[m')).lower().strip()
        if pergunta == 'fim':
            break
        linha(f'ACESSANDO O MANUAL DO COMANDO "{pergunta}"')
        print('\033[7m')
        help(pergunta)
        print('\033[m')


ajuda()
