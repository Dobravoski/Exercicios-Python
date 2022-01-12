def ficha(nome, gols):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.strip() == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 20)
nome = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Número de gols: '))
ficha(nome, gols)
