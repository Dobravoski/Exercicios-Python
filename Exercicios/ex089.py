boletim = []
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    dados = [[nome, [nota1, nota2]]]
    boletim += dados
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar == 'N' or continuar == 'S':
            break
    if continuar == 'N':
        break
print('-=' * 25)
print(f'{"No.":<4}  {"NOME":<10}    {"MÉDIA":>8}')
print('-' * 35)
for n in range(0, len(boletim)):
    print(f'{n:<4}     {boletim[n][0]:<10}     {(boletim[n][1][0] + boletim[n][1][1]) / 2:>8.1f}')
print('-' * 35)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    print(f'As notas de {boletim[mostrar][0]} são {boletim[mostrar][1]}')
    print('-' * 30)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
