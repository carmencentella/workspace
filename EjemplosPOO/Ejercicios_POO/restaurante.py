class restaurante():
    def __init__(self,nombre,tipo_horno,numero_servido):
        self.nombre_restaurante=nombre
        self.tipo_cocina=tipo_horno
        self.clientes=numero_servido
        self.abierto=False
    def describir_restaurante(self):
        print(f'El restaurante {self.nombre_restaurante} tiene un tipo de cocina {self.tipo_cocina} y ha servido a {self.clientes} clientes')
    def abrir_restaurante(self):
        self.abierto=True
        print('El restaurante está abierto')
    def establecer_como_servido(self): 
        self.clientes=int(input(f'¿Cuántos clientes se han servido en {self.nombre_restaurante}? '))
        print(f'{self.nombre_restaurante} ha servido a {self.clientes} clientes')
    def incrementar_numero_servido(self):
        self.clientesincrementados=int(input(f'¿Cuántos clientes se han servido hoy en {self.nombre_restaurante}? '))
        self.clientes+=self.clientesincrementados
        print(f'{self.nombre_restaurante} ha servido a {self.clientes} clientes en total')
