n = m = s = me = ma = 0
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Você quer continuar [S/N]: ')).strip().upper()[0]
    m += 1
    s += n
    if m == 1:
        ma = me = n
    else:
        if ma < n:
            ma = n
        if me > n:
            me = n
print(f'A média entre todos os números digitados é {s / m:.2f}.')
print(f'O maior número digitado é {ma} e o menor é {me}.')
