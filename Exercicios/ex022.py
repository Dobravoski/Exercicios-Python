n = input('Digite seu nome completo: ')
print(f'Seu nome com letras minúsculas é {n.lower()}')
print(f'Seu nome com letras maiúsculas é {n.upper()}')
#print(f'Total de letras que contem seu nome é {len(n.replace(" ", ""))}')
#Da para utilizar dessa formar também, no entanto o de baixo foi utilizado no vídeo
print(f'Total de letras que contem seu nome é {len(n) - n.count(" ")}')
print(f'Seu primeiro nome tem {n.find(" ")} letras.')
#print(f'Seu primeiro nome tem {len(n.split()[0])} letras')
#Ou também da pelo método acima