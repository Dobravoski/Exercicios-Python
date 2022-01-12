from datetime import date
s = 0
n = 0
for c in range (1, 8):
    p = date.today().year - int(input('Digite o ano de nascimento: '))
    if p >= 21:
        s += 1
    else:
        n += 1
print(f'{s} Pessoas já atingiram a maioridade e {n} pessoas ainda não atingiram a marioriodade.')
