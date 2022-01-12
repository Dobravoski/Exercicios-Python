from datetime import date
a = int(input('Digite seu ano de nascimento: '))
i = date.today().year - a
if i < 18:
    print(f'Você não tem idade o suficiente para se alistar, volte daqui {18 - i} anos')
elif i == 18:
    print(f'Você já tem a idade necessária, vá se alistar no exército brasileiro.')
elif i > 18:
    print(f'Você está a {i - 18} anos atrásado, vá se alistar!')
