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

Telepizza=restaurante('Telepizza','horno de piedra')
Dominos=restaurante('Dominos','horno de leña')
Giulianis=restaurante('Giulianis','horno eléctrico')
Telepizza.describir_restaurante()
Dominos.describir_restaurante()
Giulianis.describir_restaurante()
Telepizza.abrir_restaurante()