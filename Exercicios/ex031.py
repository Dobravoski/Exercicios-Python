d = float(input('Digite a distância da sua viagem em km: '))
if d <= 200:
    print(f'O valor da sua viagem será de R${d * 0.50}')
else:
    print(f'O valor da sua viagem será de R${d * 0.45}')
