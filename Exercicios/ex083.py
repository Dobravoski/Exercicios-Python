ex = str(input('Digite uma expressão: '))
aberto = ex.count('(')
fechado = ex.count(')')
if aberto == fechado:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
