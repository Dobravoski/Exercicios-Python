p = float(input("Digite o preço do produto: R$"))
print('Qual forma de pagamento quer usar?')
print("""
[1] dinheiro/cheque
[2] vista no cartão
[3] 2x no cartão
[4] 3x no cartão
""")
f = int(input('Qual deseja utilizar? '))
if f == 1:
    print(f'O valor a ser pago é de R${p - (p / 100 * 10):.2f}')
elif f == 2:
    print(f'O valor a ser pago é de R${p - (p / 100 * 5):.2f}')
elif f == 3:
    print(f'O valor a ser pago por parcela é de R${p / 2:.2f} e no total é R${p}')
elif f == 4:
    print(f'O valor a ser pago por parcela é de R${((p / 5) + p) / 3:.2f} e no total R${(p / 5) + p}')
