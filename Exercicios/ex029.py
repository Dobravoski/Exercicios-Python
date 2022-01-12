v = float(input('Digite a velocidade do seu carro em km/h: '))
if v > 80:
    print(f'Como você estava a {v - 80} km/h a mais do que o limite, você foi multado em R${(v - 80) * 7}')
else:
    print('Você ainda está abaixo do limite, continue assim.')
