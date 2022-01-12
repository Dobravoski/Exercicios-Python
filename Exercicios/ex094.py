grupo = []
somai = 0
dados = {}
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('Por favor digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    grupo.append(dados.copy())
    somai += dados['idade']
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar == 'N' or continuar == 'S':
            break
    if continuar == 'N':
        break
print(f'O grupo tem {len(grupo)} pessoas.')
print(f'A média de idade é {somai / len(grupo):5.2f}')
print(f'A mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(p['nome'], end=', ')
print()
print(f'Lista das pessoas que estão acima da média: ', end='')
for p in grupo:
    if p['idade'] >= somai / len(grupo):
        print(p['nome'], end=', ')
print()
print('<< ENCERRANDO >>')
