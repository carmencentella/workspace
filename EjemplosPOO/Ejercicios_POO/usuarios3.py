class usuario():
    def __init__(self,nombre,apellido,correo,año_nacimiento):
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.año=año_nacimiento
    def describir_usuario(self):
        print(f'Usuario {self.nombre} {self.apellido}, de correo {self.correo} y nacido en {self.año}')
    def saludar_usuario(self):
        print(f'¡Buenos días {self.nombre}!')
usuario1=usuario('Carmen','Centella','carcenjar@alu.edu.gva.es','2007')
usuario2=usuario('Aurora','Centella','aurcenjar@alu.edu.gva.es','2005')
usuario3=usuario('Aida','Jarque','adejarten@alu.edu.gva.es','1970')
usuario1.describir_usuario()
usuario1.saludar_usuario()
usuario2.describir_usuario()
usuario2.saludar_usuario()
usuario3.describir_usuario()
usuario3.saludar_usuario()