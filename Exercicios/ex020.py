from random import sample
a = input('Nome do primeiro aluno: ')
b = input('Nome do segundo aluno: ')
c = input('Nome do terceiro aluno: ')
d = input('Nome do quarto aluno: ')
print(f'A ordem de apresentação sorteada é: {sample([a, b, c, d], k=4)}')
