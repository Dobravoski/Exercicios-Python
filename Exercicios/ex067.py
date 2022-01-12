num = cont = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 33)
    if num < 0:
        break
    cont = 0
    while True:
        cont += 1
        print(f'{num} x {cont} = {num * cont}')
        if cont >= 10:
            break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
