numtot=int(input('¿Cuántos números vas a introducir? '))
numero = int(input(f'Dime el número 1: '))
mayor=numero
menor=numero
media=numero
num=2
while num!=numtot+1:
    numero=int(input(f'Dime el número {num}: '))
    num=num+1
    if (numero < menor):
        menor=numero
    elif (numero>mayor):    
        mayor=numero
    media+=numero

print(f"La media es {round(media/numtot,2)}")
print(f'El número más grande es {mayor}')
print(f'El número menor es {menor}')