num = float(input('Digite um número: '))
num2 = 1
while num >= 1:
    num2 *= num
    num -= 1
print(f'O fatorial desse número é {num2}')
