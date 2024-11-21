nombreycontraseña=['usuario1','asdasd']    
intentos=1
while True:
    respuesta=input('Introduce el nombre de usuario y la contraseña separados por comas: ').split(',')
    if respuesta==nombreycontraseña:
        print(f'Verdadero, te ha costado {intentos} intentos.')
        break
    else:
        intentos+=1
        print('Incorrecto.')
    if intentos>3:
        print('Se ha alcanzado el número máximo de intentos.')
        break