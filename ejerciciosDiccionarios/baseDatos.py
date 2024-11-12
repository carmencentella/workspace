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
                print(f'{clave} , {valor}')
        case 2: 
            usuario2={
                'nombre':input('introduce el nombre: '),
                'ocupación':input('introduce su ocupación: '),
                'aficiones': input('introduce tres aficiones separadas con comas: '). split(','),
                'edad': int(input('introduce tu edad: '))
                }
            usuarios.update(usuario2)