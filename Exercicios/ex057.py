s = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo [M/F]: ')).strip().upper()
if s == 'M':
    print('Olá senhor.')
else:
    print('Olá, senhora.')
