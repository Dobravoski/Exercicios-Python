valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
print('=-' * 25)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}.')
if 5 in valores:
    print('O 5 faz parte da lista!')
else:
    print('O 5 NÃO foi encontrado na lista!')
