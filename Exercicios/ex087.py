matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna = maior_linha = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
print('-=' * 20)
print(f'A soma dos valores pares é {soma_pares}.')
for v in range(0, 3):
    soma_coluna += matriz[v][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior_linha:
        maior_linha = matriz[1][c]
print(f'O maior valor da segunda linha é {maior_linha}.')
