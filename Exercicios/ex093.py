gol = []
cont = 0
dados = {'nome': str(input('Nome do jogador: ')).strip().capitalize()}
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(1, partidas + 1):
    gol.append(int(input(f'Quantos gols na {c}ª partida? ')))
dados['totgols'] = sum(gol)
dados['gols'] = gol[:]
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c in range(1, partidas + 1):
    print(f'    => Na {c}ª partida, {dados["gols"][cont]} gols.')
    cont += 1
print(f'Foi um total de {dados["totgols"]} gols.')
