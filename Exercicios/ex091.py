from random import randint
from time import sleep
from operator import itemgetter

num = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = sorted(num.items(), key=itemgetter(1), reverse=True)
print('-=' * 13)
print('RANKING DOS JOGADORES')
print('-=' * 13)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
