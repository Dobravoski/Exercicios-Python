f = str(input('Digite uma frase: ')).strip().lower()
print(f'Na sua frase aparece {f.count("a")} As')
print(f'A primeira letra A está na posição {f.find("a")}')
print(f'A ultima letra A está na posição {f.rfind("a")}')
