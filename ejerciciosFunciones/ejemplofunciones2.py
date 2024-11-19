def minimo(a,b):
    if a<b:
        print(f'El mínimo de {a} y {b} es: {a}')
    elif a>b:
        print(f'El mínimo de {a} y {b} es {b}')
    else:
        print(f'Los dos números son iguales')
a=int(input('Introduce un número: '))
b=int(input('Introduce otro número: '))
minimo(a,b)