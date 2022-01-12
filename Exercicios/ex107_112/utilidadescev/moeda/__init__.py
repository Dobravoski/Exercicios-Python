def metade(num, formatar=False):
    m = num / 2
    if formatar:
        m = moeda(m)
    return m


def dobro(num, formatar=False):
    d = num * 2
    if formatar:
        d = moeda(d)
    return d


def acrescimo(num, porcent, formatar=False):
    a = (num / 100 * porcent) + num
    if formatar:
        a = moeda(a)
    return a


def decrescimo(num, porcent, formatar=False):
    d = num - (num / 100 * porcent)
    if formatar:
        d = moeda(d)
    return d


def moeda(num):
    f = f'R${num}'.replace(',', '.')
    return f


def resumo(num, porcenta, porcentd):
    print('-' * 26)
    print('RESUMO DO VALOR')
    print('-' * 26)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'35% de aumento: \t{acrescimo(num, porcenta, True)}')
    print(f'22% de redução: \t{decrescimo(num, porcentd, True)}')
    print('-' * 26)
