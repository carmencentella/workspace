class restaurante():
    def __init__(self,nombre,tipo_horno):
        self.nombre_restaurante=nombre
        self.tipo_cocina=tipo_horno
        self.abierto=False
    def describir_restaurante(self):
        print(f'El restaurante {self.nombre_restaurante} tiene un tipo de cocina {self.tipo_cocina}')
    def abrir_restaurante(self):
        self.abierto=True
        print('El restaurante está abierto')

restaurante=restaurante('Telepizza','horno de piedra')
restaurante.describir_restaurante()
restaurante.abrir_restaurante()