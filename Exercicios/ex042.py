l1 = float(input('Digite o primeiro segmento de reta do triângulo: '))
l2 = float(input('Digite o segundo segmento de reta do triângulo: '))
l3 = float(input('Digite o terceiro segmento de reta do triângulo: '))
if l2 - l3 < l1 < l2 + l3 and l1 - l3 < l2 < l1 + l3 and l1 - l2 < l3 < l1 + l2:
    if l1 == l2 == l3:
        print('É possivel formar um triângulo EQUILÁTERO.')
    elif l1 == l2 != l3 or l3 == l2 != l1 or l3 == l1 != l2:
        print('É possivel formar um triângulo ISÓCELES.')
    elif l1 != l2 != l3 != l1:
        print('É possivel formar um triângulo ESCALENO.')
else:
    print('NÃO é possivel formar um triângulo com esses segmentos de reta.')
