n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        t += 1
print(f'O número {n} foi divisível {t} vezes,', end=' ')
if t == 2:
    print('e por isso ele é PRIMO.')
else:
    print('e por isso ele NÃO É PRIMO.')
