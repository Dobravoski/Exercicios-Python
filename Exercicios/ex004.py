a1 = input('Digite algo: ')
print('Seu tipo primitivo é...', type(a1))
print('É alfanumérico?', a1.isalnum())
print('É alfabético?', a1.isalpha())
print('Ta em ascii?', a1.isascii())
print('É um dígito?', a1.isdigit())
print('Ta tudo em minúsculo?', a1.islower())
print('Que porra é essa', a1.isidentifier())
print('É em decimal?', a1.isdecimal())
print('É printável?', a1.isprintable())
print('É tudo espaço?', a1.isspace())
print('É numérico?', a1.isnumeric())
print('Esta capitalizada?', a1.istitle())
print('Sei lá que porra é essa', a1.__init_subclass__())
print('Ta tudo em maiúsculo?', a1.isupper())
