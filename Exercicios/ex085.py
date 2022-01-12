num = [[], []]
verificador = 0
for c in range(1, 8):
    verificador = int(input(f'Digite o {c}º valor: '))
    if verificador % 2 == 0:
        num[0].append(verificador)
    else:
        num[1].append(verificador)
print('=-' * 20)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
