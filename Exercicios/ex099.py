def maior(*num):
    lista = []
    print('-=' * 20)
    print('Analisando os valores passados...')
    for c in num:
        lista.append(c)
        print(c, end=' ')
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {max(lista)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
