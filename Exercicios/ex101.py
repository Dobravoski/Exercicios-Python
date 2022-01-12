def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 18:
        return f'com {idade} anos: NÃO VOTA'
    elif 18 <= idade <= 65:
        f'com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade > 65:
        f'com {idade} anos: VOTO OPCIONAL'


print('-' * 25)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
