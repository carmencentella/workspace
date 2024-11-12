claves = ['Diez', 'Veinte', 'Treinta']
valores = [10, 20, 30]
diccionario={}
j=0
for i in claves:
    diccionario[i]=valores[j]
    j+=1
print(f'El contenido del diccionario es: {diccionario}')