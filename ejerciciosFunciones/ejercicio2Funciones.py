def vocal(caracter):
    vocales=['a','e','i','o','u']
    if caracter in vocales:
        print('Esta letra es una vocal')
    else:
        print('Esta letra no es una vocal')
letra=input('Introduce una letra y te diré si es una vocal: ')
print(vocal(letra))