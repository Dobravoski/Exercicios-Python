n = str(input('Digite seu nome completo: ')).strip()
print(f'Primeiro nome: {n.split()[0]}')
print(f'Segundo nome: {n.split()[len(n.split()) - 1]}')
