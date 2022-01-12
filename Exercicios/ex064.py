n = s = t = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    s += n
    t += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'No total foram digitados {t} números e a soma entre todos os números é {s}')
