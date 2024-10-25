quieressaludo='s'
MAX=4
numsaludos=0
while quieressaludo=='s' and numsaludos!=MAX:
    print('Hola qué tal!')
    numsaludos+=1
      
    
    quieressaludo=input('¿Quieres otro saludo? [s/n]')
    if quieressaludo=='n':
     break
    while quieressaludo not in ('s' , 'n'):
        quieressaludo=input('Sólo se aceptan s o n')
if numsaludos==MAX:
    print('Número máximo de saludos alcanzado')
print('Que tenga un buen día')