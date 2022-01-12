escolha = 0
maior = 0
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
while escolha != 5:
    print("""----MENU----
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    """)
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        print(f'A soma entre os números é {num1 + num2}.')
    if escolha == 2:
        print(f'O produto entre esses números é {num1 * num2}.')
    if escolha == 3:
        maior = num1
        if num2 > maior:
            maior = num2
        print(f'O maior número é o {maior}.')
    if escolha == 4:
        num1 = int(input('Digite o 1º número: '))
        num2 = int(input('Digite o 2º número: '))
print('VOCÊ ESCOLHEU SAIR DO PROGRAMA.')
