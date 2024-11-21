def transformarasegundos(horas,minutos,segundos):
    horasasegundos=horas*3600
    minutosasegundos=minutos*60
    segundostot=segundos+horasasegundos+minutosasegundos
    print(f'Los segundos totales son {segundostot} s')

def transformararesto(segundostot):
    horas=segundostot//3600
    minutos=(segundostot-horas*3600)//60
    segundos=segundostot-horas*3600-minutos*60
    print(f'La hora en horas, minutos y segundos es: {horas} h {minutos} min y {segundos} s')
while True:
    respuesta=int(input('Si quieres transformar de horas a segundos pulsa 1, si quieres transformar de segundos a horas pulsa 2, si quieres salir del programa pulsa 3: '))
    match respuesta:
        case 1:
            horas=int(input('Introduce las horas: '))
            minutos=int(input('Introduce los minutos: '))
            segundos=int(input('Introduce los segundos: '))
            print(transformarasegundos(horas,minutos,segundos))
        case 2:
            segundostot=int(input('Introduce los segundos totales: '))
            print(transformararesto(segundostot))
        case 3:
            break