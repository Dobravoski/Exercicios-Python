from datetime import datetime
dados = {'nome': str(input('Nome: ')).strip().capitalize(),
         'idade': datetime.now().year - int(input('Ano de nascimento: ')),
         'ctps': int(input('Carteira de trabalho (0 não tem): '))}
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (35 - (datetime.now().year - dados['contratação'])) + dados['idade']
print('-=' * 20)
print(f'    - Nome: {dados["nome"]}.')
print(f'    - Idade: {dados["idade"]}.')
if dados['ctps'] != 0:
    print(f'    - CTPS: {dados["ctps"]}.')
    print(f'    - Contratação: {dados["contratação"]}.')
    print(f'    - Salário: R${dados["salario"]}.')
    print(f'    - Aposentadoria: {dados["aposentadoria"]} anos.')
else:
    print(f'    - CTPS: não tem.')
