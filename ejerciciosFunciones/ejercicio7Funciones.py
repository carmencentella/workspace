def MCD(numero1,numero2):
    if numero1>numero2:
        maximo=numero1
        minimo=numero2
    else:
        maximo=numero2
        minimo=numero1
    d=0
    while d!=minimo:
        division=maximo%minimo
        if division==0:
            d=minimo
        else:
            maximo=minimo
            minimo=division
    print(d)
