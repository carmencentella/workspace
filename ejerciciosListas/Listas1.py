largo=int(input('¿Cuántas palabras tiene la lista? '))
numero=1
list=[]
largo+=1
while numero!=largo:
    lista=input(f'Dime la palabra {numero}: ')
    numero+=1
    list.append(lista)
print(f'La lista es: {list}')
eliminar=input('Dime qué palabra eliminar: ')
while eliminar in list:
    list.remove(eliminar)
print(f'Tu lista ahora es {list}')