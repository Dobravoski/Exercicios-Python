f = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
if f == f[::-1]:
    print('A frase é um palíndromo.')
else:
    print('A frase NÃO é um palíndromo')
