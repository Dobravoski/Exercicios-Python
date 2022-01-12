from datetime import date
a = int(input('Digite o ano de nascimento do atleta: '))
i = date.today().year - a
if i <= 9:
    print(f'Como esse atleta tem {i} anos, ele(a) é da categoria Mirim.')
elif i <= 14:
    print(f'Como esse atleta tem {i} anos, ele(a) é da categoria Infantil.')
elif i <= 19:
    print(f'Como esse atleta tem {i} anos, ele(a) é da categoria Junior.')
elif i == 20:
    print(f'Como esse atleta tem {i} anos, ele(a) é da categoria Sênior.')
elif i > 20:
    print(f'Como esse atleta tem {i} anos, ele(a) é da categoria Master.')
