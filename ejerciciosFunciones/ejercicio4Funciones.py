def areayperimetro(radio):
    area=3.14159*radio**2
    perimetro=2*3.14159*radio
    print(f'El área del circulo es {area}m², y su perímetro es {perimetro}m')
radio=float(input('Introduce el radio de una circunferencia y de diré su radio y perímetro: '))
print(areayperimetro(radio))