def leiadinheiro(num):
    global txt
    ok = False
    while not ok:
        txt = str(input(num)).replace(',', '.').strip()
        if txt.isnumeric:
            ok = True
            txt = float(txt)
        else:
            print(f'ERRO! "{txt}" é um preço inválido!')
    return txt
