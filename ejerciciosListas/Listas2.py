largo=int(input('¿Cuántas palabras tiene la lista? '))
numero=1
list=[]
largo+=1
while numero!=largo:
    lista=input(f'Dime la palabra {numero}: ')
    numero+=1
    list.append(lista)
print(f'La lista es: {list}')
long=len(list)
for i in (0,long):
    list.append(i)
print(f'La lista inversa es: {list}')