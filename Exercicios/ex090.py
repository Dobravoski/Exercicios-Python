aluno = {'nome': str(input('Nome: ')).strip().capitalize()}
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 7:
    aluno['situacao'] = 'reprovado'
elif 5 <= aluno['media'] >= 7:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'aprovado'
for k, v in aluno.items():
    print(f'{k}: {v}')
