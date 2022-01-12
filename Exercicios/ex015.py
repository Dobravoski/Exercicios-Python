d = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km você andou? '))
print(f'O preço a pagar é de R${(d * 60) + (km * 0.15):.2f}')
