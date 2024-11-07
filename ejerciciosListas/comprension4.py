#Listar los ficheros python del directorio actual que comienzan por ‘f’
import os
ficheros_python = [f for f in os.listdir('.') if f.endswith('.py') and f.startswith('L')]
print(ficheros_python)