n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('REPROVADO!')
elif m > 7:
    print('APROVADO!')
else:
    print('RECUPERAÇÃO!')
