times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
         'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(f'Lista de times do brasileirão: {times}')
print('=-' * 20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('=-' * 20)
print(f'Os 4 últimos são: {times[16:]}')
print('=-' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-' * 20)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
