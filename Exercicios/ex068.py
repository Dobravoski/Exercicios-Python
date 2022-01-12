from random import randint
num = cont = 0
jogada = 'P'
print('=-' * 13)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-' * 13)
while True:
    pc = randint(0, 10)
    num = int(input('Digite um valor: '))
    jogada = str(input('Par ou Ímpar [P/I]: ').strip().upper())[0]
    while jogada not in 'PI':
            jogada = str(input('Par ou Ímpar [P/I]: ').strip().upper())[0]
    if (num + pc) % 2 != 0:
        print('-' * 50)
        print(f'Você jogou {num} e o computador {pc}. Total deu {num + pc}, ÍMPAR')
        print('-' * 50)
        if jogada == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        if jogada == 'P':
            print('Você PERDEU!')
            print('=-' * 40)
            break
    if (num + pc) % 2 == 0:
        print('-' * 50)
        print(f'Você jogou {num} e o computador {pc}. Total deu {num + pc}, PAR')
        print('-' * 50)
        if jogada == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        if jogada == 'I':
            print('Você PERDEU!')
            print('=-' * 40)
            break
print(f'GAME OVER! Você venceu {cont} vez(es)')
