#ordenador genera numero y el usuario tiene que adivinar
import random

valor_min=int(input('Introduce el valor minimo: '))
valor_max=int(input('Introduce el valor máximo: '))
secreto = random.randint(valor_min, valor_max)
print(f'Adivina un número entero entre {valor_min} y {valor_max}.')
intentos=1
num=int(input('Escribe un número: '))
while num!=secreto:
    if num>secreto:
        num=int(input('Demasiado grande, inténtalo otra vez:'))
    elif num<secreto:
        num=int(input('Demasiado pequeño, inténtalo otra vez: '))
    intentos += 1 
print(f'Correcto, te ha costado {intentos} intentos')
