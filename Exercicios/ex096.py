def area(a, b):
    mult = a*b
    print(f'A área de um terreno de {l}x{c} é de {mult}m².')


print('   Controle de terrenos')
print('-' * 17)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
