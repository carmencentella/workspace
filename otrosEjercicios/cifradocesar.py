alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cesar(texto,desplazamiento,direccion):
    if direccion=='decodifica':
        desplazamiento*=-1
    palabra=""
    for letra in texto:
        posicion=alfabeto.index(letra)
        nuevaposicion=(posicion+desplazamiento)%27
        letra=alfabeto[nuevaposicion]
        palabra+=letra
    print(palabra)   
'''
def codifica(texto,desplazamiento):
    palabra=""
    for letra in texto:
        posicion=alfabeto.index(letra)
        nuevaposicion=(posicion+desplazamiento)%27
        letra=alfabeto[nuevaposicion]
        palabra+=letra
    print(palabra)
def descodifica(texto,desplazamiento):    
    palabra=""
    for letra in texto:
        posicion=alfabeto.index(letra)
        nuevaposicion=(posicion-desplazamiento)%27
        letra=alfabeto[nuevaposicion]
        palabra+=letra
    print(palabra)
'''    
direccion = input("Escribe 'codifica' para codificar o 'decodifica' para decodificar: ")
texto = input("Escribe tu mensaje: ").lower()
desplazam = int(input("Escribe un número para el desplazamiento: "))
print(cesar(texto,desplazam,direccion))
