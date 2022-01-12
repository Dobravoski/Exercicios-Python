p = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite uma razão de uma PA: '))
d = p + 9 * r
print('OS 10 PRIMEIROS TERMOS DESSA PA É:')
for c in range(p, d + r, r):
    print(c, end=' ')
