def fatorial(num, show=False):
    """
    :param num: O número a ser calculado o fatorial
    :param show: (opcional) Mostrar ou não a conta
    :return: Retorna o valor de um fatorial de um número
    """
    resul = 1
    print('-' * 30)
    for c in range(1, num + 1):
        resul *= c
    if show:
        for c in range(num, 1 - 1, -1):
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'1 = {resul}')
    else:
        print(resul)


fatorial(5)
fatorial(7, True)
help(fatorial)
