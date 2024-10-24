quieressaludo='s'
MAX=4
numsaludos=0
while quieressaludo=='s':
    print('Hola qué tal!')
    numsaludos+=1
      
    
    quieressaludo=input('¿Quieres otro saludo? [s/n]')
    if quieressaludo=='n':
     print('Que tenga un buen día')
    elif quieressaludo!='s':
        quieressaludo=input('Sólo se aceptan s o n')
if numsaludos==MAX:
   print('numero maximo de saludos')
print('Que tenga un buen día')