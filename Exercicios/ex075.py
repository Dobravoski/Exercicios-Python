a = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'Você digitou os seguintes valores: {a}')
print(f'O valor 9 apareceu {a.count(9)} vez(es).')
if 3 in a:
    print(f'O valor 3 apareceu na {a.index(3) + 1}ª posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')
print(f'Os valores pares digitados foram:')
for n in a:
    if n % 2 == 0:
        print(n, end=' ')
