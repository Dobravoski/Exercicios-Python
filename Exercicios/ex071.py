print("""
===========================================
            BANCO DOBRAVOSKI
===========================================""")
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 50
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
#Também pode ser assim, no entanto o de cima é a ideia do vídeo, e eu achei mais interessante(mesmo ela sendo maior)
#print(f"""
#===========================
#Total de {valor // 50} cédulas de R$50
#Total de {(valor % 50) // 20} cédulas de R$20
#Total de {((valor % 50) % 20) // 10} cédulas de R$10
#Total de {((valor % 50) % 20) % 10} cédulas de R$1
#============================
#Volte sempre ao Banco Dobravoski! Tenha um bom dia.""")
