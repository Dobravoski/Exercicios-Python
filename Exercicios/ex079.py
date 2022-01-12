valores = []
while True:
    add = int(input('Digite um valor: '))
    if add in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(add)
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
print('=-' * 20)
valores.sort()
print(f'Você digitou os valores: {valores}.')
