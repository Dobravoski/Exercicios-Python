time = []
dados = {}
gol = []
cont = 0
while True:
    dados.clear()
    dados = {'nome': str(input('Nome do jogador: ')).strip().capitalize()}
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gol.clear()
    for c in range(1, partidas + 1):
        gol.append(int(input(f'Quantos gols na {c}ª partida? ')))
    dados['totgols'] = sum(gol)
    dados['gols'] = gol[:]
    time.append(dados.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
print('-=' * 25)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 25)
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    elif busca > len(time):
        print(f'ERRO! Não existe jogador com código {busca} na lista.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} --')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No {i + 1}º jogo, {g} gols.')
    print('-' * 30)
print('<< VOLTE SEMPRE! >>')
