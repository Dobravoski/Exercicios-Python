homem = mulher = pessoas = 0
while True:
    print('-' * 19)
    print('CADASTRE UMA PESSOA')
    print('-' * 19)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    continuar = str(input('Quer continuar? [S/N]:  ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]:  ')).strip().upper()[0]
    if idade >= 18:
        pessoas += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if continuar == 'N':
        break
print(f""" ======FIM DO PROGRAMA======
Total de pessoas com mais de 18 anos: {pessoas};
Total de homens cadastrados: {homem};
Total de mulheres com menos de 20 anos: {mulher}""")
