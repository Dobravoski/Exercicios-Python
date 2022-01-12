words = ('Oi', 'eu', 'aprendo', 'Python', 'pelo', 'Curso', 'em', 'video')
for p in words:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
