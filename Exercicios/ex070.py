total = caro = preço = barato = cont = 0
name = 'name'
continuar = 'S'
namepreço = ' '
print("""        ---------------------------------
                SUPER BARATÃO!
        ---------------------------------""")
while True:
    name = str(input('Nome do produto: ')).strip().capitalize()
    preço = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N]:  ')).strip().upper()[0]
    while continuar not in 'SN':
       continuar = str(input('Quer continuar? [S/N]:  ')).strip().upper()[0]
    total += preço
    cont += 1
    if preço > 1000:
        caro += 1
    if cont == 1 or barato > preço:
        barato = preço
        namepreço = name
    if continuar == 'N':
        break
print(f"""----------FIM DAS COMPRAS----------
O total das compras foi R${total};
Tem {caro} produtos custando mais de R$1.000;
O produto mais barato foi {namepreço} que custa R${barato}.""")
