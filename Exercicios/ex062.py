p = int(input('Digite o primeiro número de uma PA: '))
r = int(input('Digite uma razão de uma PA: '))
c = 1
total = 0
m = 10
print('OS 10 PRIMEIROS TERMOS DESSA PA É:')
while m != 0:
    total += m
    while c <= total:
        a = p + r
        p = a
        c += 1
        print(a, end=' - ')
    print('Pausa')
    m = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
