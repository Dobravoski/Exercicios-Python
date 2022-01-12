a = float(input('Digite um tamanho de um segmento de reta: '))
b = float(input('Digite mais um segmento de reta: '))
c = float(input('Digite mais um segmento de reta: '))
if b - c < a < b + c: #No vídeo é feito de uma maneira diferente, no entanto dessa maneira é mais simplificada e eu aprendi na escola assim
    print('Com esses segmentos de reta é possivel criar um triângulo!')
else:
    print('Com esses segmentos de reta NÃO é possivel criar um triângulo!')
