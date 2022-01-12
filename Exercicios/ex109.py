from ex107_112.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.')
print(f'Aumentando 10%, temos {moeda.acrescimo(p, 10, True)}.')
print(f'Reduzindo 13%, temos {moeda.decrescimo(p, 13, True)}')
