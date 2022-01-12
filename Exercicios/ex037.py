n = int(input('Digite um número inteiro: '))
b = int(input('Digite:\n 1 para binário;\n 2 para octal;\n 3 para hexadecimal.\n Base de conversão: '))
if b == 1:
    print(f'O número {n} em binário é {bin(n)[2:]}')
#.strip("0b")}')
elif b == 2:
    print(f'O numéro {n} em octal é {oct(n)[2:]}')
#.strip("0o")}
elif b == 3:
    print(f'O numéro {n} em hexadecimal é {hex(n)[2:]}')
#.strip("0x")}
else:
    print('Digite algo válido!')
