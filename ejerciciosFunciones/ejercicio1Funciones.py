def max_de_tres(primero,segundo,tercero):
    if primero>segundo:
        maximo=primero
    elif segundo>primero:
        maximo=segundo
    if tercero>maximo:
        maximo=tercero
    print(maximo)
uno=int(input(f'introduce el primer número: '))
dos=int(input(f'introduce el segundo número: '))
tres=int(input(f'introduce el tercer número: '))
print(f'El máximo es {max_de_tres(uno,dos,tres)}')