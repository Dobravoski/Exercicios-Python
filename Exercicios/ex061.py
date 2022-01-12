p = int(input('Digite o primeiro número de uma PA: '))
r = int(input('Digite uma razão de uma PA: '))
c = 0
print('OS 10 PRIMEIROS TERMOS DESSA PA É:')
while c < 10:
    a = p + r
    p = a
    c += 1
    print(a, end=' - ')
print('FIM')
