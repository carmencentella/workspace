with open('ficheros/temps.dat') as f:
    for linea in f:
        temp_min, temp_max=linea.strip().split()
        print(temp_min, temp_max)