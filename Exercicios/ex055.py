ma = 0
me = 0
for c in range(1, 6):
    p = float(input(f'Digite o peso da {c}º pessoa: Kg '))
    if c == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print(f'O menor peso é {me} e o maior é {ma}')
