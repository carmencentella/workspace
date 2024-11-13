usuarios= {
    'Centella':{
        'nombre':'Carmen',
        'ocupación':'estudiante',
        'aficiones': ['cocinar','coser','viajar'],
        'edad':17
    }
}
while True:
    i=int(input('1 - listar usuarios, 2 - añadir un usuario, 3 - borrar un usuario, 4 - buscar un usuario, 5 - salir:'))
    match i:
        case 1:

            print(f'Listado de todos los usuarios:')
            for clave,valor in usuarios.items():
                    print(f'{clave} , {valor}\n')
        case 2: 
            apellido=input('Introduce el apellido del usuario: ')
            usuarios[apellido]= {
                'nombre':input('introduce el nombre: '),
                'ocupación':input('introduce su ocupación: '),
                'aficiones': input('introduce tres aficiones separadas con comas: '). split(','),
                'edad': int(input('introduce tu edad: '))
                }
        case 3:
            borrar=input('Qué usuario quieres borrar? ')
            if borrar in usuarios:
                del usuarios[borrar]
                print('Se ha borrado este usuario')
            else:
                print('Este usuario no existe')
        case 4:
            buscar=input('Introduce el apellido a buscar:')
            if buscar in usuarios:
                    print(f'{usuarios[buscar]}')
            else :
                print('Este usuario no existe')

        case 5: 
            break