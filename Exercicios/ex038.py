n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
if n1 > n2:
    print(f'O {n1} é o maior e o segundo maior é o {n2}.')
elif n1 < n2:
    print(f'O {n2} é o maior e o segundo maior é o {n1}.')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
