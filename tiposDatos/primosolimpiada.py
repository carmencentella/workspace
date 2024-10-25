#decidir si un número es primo o no
t=int(input('Indica el nombre de casos a procesar: '))
for i in range(0,t):
    k=int(input('Introduce un número entre 0 y 100: '))
    n= int(input('Introduce un número entero entre 1 y 1000 '))
    if k==0:
        if (n % 2==0):
            print('no es primo')
        else:
            print('sí')