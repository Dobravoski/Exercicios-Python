def notas1(*num, sit=False):
    notas = {}
    notas['total'] = len(num)
    notas['maior'] = max(num)
    notas['menor'] = min(num)
    notas['media'] = sum(num) / len(num)
    if sit:
        if notas['media'] < 5:
            notas['situacao'] = 'RUIM'
        elif notas['media'] >= 7:
            notas['situacao'] = 'BOM'
        else:
            notas['situacao'] = 'RAZOAVEL'
    print(notas)


notas1(3.5, 2, 6.5, 2, sit=True)
