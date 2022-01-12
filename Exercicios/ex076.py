listagem = ('Caneta', 1.50, 'Garrafinha', 27.50, 'lápis', 1.50, 'lapiseira', 4.50, 'Grafite', 3)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=''),
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
