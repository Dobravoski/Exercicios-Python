valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um número: ')))
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=-' * 20)
print(f'A lista completa é: {valores}.')
print(f'A lista de pares é: {pares}.')
print(f'A lista de ímpares é: {impares}.')
print('=-' * 20)
