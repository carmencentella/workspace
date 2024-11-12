notas = {
 'Matemáticas': 7,
 'Física': 8,
 'Historia': 9
}
minimo=10
for clave,valor in notas.items():
    if valor < minimo:
        minimo = valor
        claveMenosNota = clave
print(f'La asignatura de menor nota es {claveMenosNota}')