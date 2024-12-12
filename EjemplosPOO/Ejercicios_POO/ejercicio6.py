class usuario():

    def __init__(self,nombre,apellido,correo,año_nacimiento):
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.año=año_nacimiento
        self.intentos_inicio=0
    def describir_usuario(self):
        print(f'Usuario {self.nombre} {self.apellido}, de correo {self.correo} y nacido en {self.año}')
    def saludar_usuario(self):
        print(f'¡Buenos días {self.nombre}!')
    def incrementar_intentos_inicio(self):
        self.intentos_inicio+=1
    def restablecer_intentos_inicio(self):
        self.intentos_inicio=0
class admin(usuario):
    def __init__(self,nombre,apellido,correo,año_nacimiento):
        super().__init__(nombre,apellido,correo,año_nacimiento)
        self.privilegios=['Añadir comentarios','Borrar comentarios','Vetar usuarios','Añadir usuarios']
    def muestra_privilegios(self):
        print('Los privilegios del administrador son:')
        for i in self.privilegios:
            print(i)
USUARIO=usuario('Carmen','Centella','carcenjar@alu.edu.gva.es','2007')
USUARIO.incrementar_intentos_inicio()
USUARIO.incrementar_intentos_inicio()
USUARIO.incrementar_intentos_inicio()
USUARIO.incrementar_intentos_inicio()
USUARIO.incrementar_intentos_inicio()
print(USUARIO.intentos_inicio)
USUARIO.restablecer_intentos_inicio()
print(USUARIO.intentos_inicio)
administrador=admin('Carmen','Centella','carcenjar@alu.edu.gva.es','2007')
administrador.muestra_privilegios()
