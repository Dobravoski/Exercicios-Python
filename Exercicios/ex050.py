s = 0
count = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        s += n
        count += 1
print(f'Você informou {count} números pares, e a some deles é {s}')
