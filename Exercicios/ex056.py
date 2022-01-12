si = 0
mm = 0
nv = 0
im = 0
for p in range(1, 5):
    print(f'----- {p} pessoa -----')
    n = str(input('Nome: ')).strip().capitalize()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()
    si += i
    if p == 1 and s == 'M':
        mm = i
        nv = n
    if s == 'M' and i > mm:
        mm = i
        nv = n
    if s == 'F' and i < 20:
        im += 1
print(f'A média das idades de todas as pessoas é {si / 4:.0f}.')
print(f'O homem mais velho tem {mm} anos e se chama {nv}.')
print(f'Ao todo tem {im} mulher(es) com menos de 20 anos.')
