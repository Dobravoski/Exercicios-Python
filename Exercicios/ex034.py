s = float(input('Digite o valor do seu salário: '))
if s > 1250:
    print(f'Seu salário aumentou para R${s + (s / 100 * 10)}')
else:
    print(f'Seu salário aumentou para R${s + (s / 100 * 15)}')
