v = float(input('Digite o valor da casa que você deseja comprar: R$'))
s = float(input('Digite o seu salário: R$'))
a = int(input('Digite em quantos anos você deseja quitar a casa: '))
m = v / (a * 12)
if m <= s / 100 * 30:
    print(f'Você pode pegar um empréstimo conosco, a mensalidade será de R${m:.2f} e você terá {a} anos para quita-la')
else:
    print('Você não tem permissão para pegar um empréstimo conosco.')
