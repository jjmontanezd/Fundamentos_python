# Sistema de Registro de Aprendices

# 1. Crear diccionario de aprendices

grupo = {
    101: {"nombre": "Ana", "edad": 20, "notas": [4.0, 3.5, 4.0, 4.5], "ciudad": "Bogota"},
    102: {"nombre": "Luis", "edad": 22, "notas": [2.5, 3.0, 2.8, 3.0], "ciudad": "Cali"},
    103: {"nombre": "Maria", "edad": 19, "notas": [4.5, 4.0, 4.8, 5.0], "ciudad": "Tunja"},
    104: {"nombre": "Carlos", "edad": 21, "notas": [2.0, 2.5, 3.0, 2.5], "ciudad": "Sogamoso"}
}

# 2. Funcion para calcular promedio

def calcular_promedio(notas):
    return sum(notas) / 4

# 3. Mostrar reporte

print("REPORTE DE APRENDICES")

for ficha, aprendiz in grupo.items():
    promedio = calcular_promedio(aprendiz["notas"])

    if promedio >= 3.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    print("Ficha:", ficha)
    print("Nombre:", aprendiz["nombre"])
    print("Edad:", aprendiz["edad"])
    print("Promedio:", round(promedio, 2))
    print("Estado:", estado)
 

# 4. Agregar un nuevo aprendiz

grupo[105] = {
    "nombre": "Pedro",
    "edad": 23,
    "notas": [4.0, 4.5, 4.0, 3.5],
    "ciudad": "Bogota"
}

# Actualizar ciudad

grupo[102]["ciudad"] = "Nueva Ciudad"

# 5. Ordenar por promedio de mayor a menor

ordenados = sorted(grupo.items(),
                   key=lambda x: calcular_promedio(x[1]["notas"]),
                   reverse=True)

print("APRENDICES ORDENADOS")

for ficha, aprendiz in ordenados:
    print(ficha, aprendiz["nombre"],
          round(calcular_promedio(aprendiz["notas"]), 2))