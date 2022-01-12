from ex107_112.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}.')
print(f'O dobro de {p} é {moeda.dobro(p)}.')
print(f'Aumentando 10%, temos {moeda.acrescimo(p, 10)}.')
print(f'Reduzindo 13%, temos {moeda.decrescimo(p, 13)}')
