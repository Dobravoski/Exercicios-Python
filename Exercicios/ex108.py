from ex107_112.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.acrescimo(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.decrescimo(p, 13))}')
