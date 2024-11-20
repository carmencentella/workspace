def histograma(lista):
    for i in lista:
        print('*'*int(i))
        

lista=input('Introduce numeros separados por comas: ').split(',')

histograma(lista)