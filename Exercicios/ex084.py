pessoas = []
peso = []
cont = 0
while True:
    pessoas.append(str(input('Nome: ')).strip().capitalize())
    peso.append((int(input('Peso: '))))
    cont += 1
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
print('=-' * 35)
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {max(peso)} kg. Peso de {pessoas[peso.index(max(peso))]}')
print(f'O menor peso foi de {min(peso)} kg. Peso de {pessoas[peso.index(min(peso))]}')
