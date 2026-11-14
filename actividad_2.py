
# ACTIVIDAD 2: CALCULADORA DE NOTAS

# Solicitar las tres calificaciones
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# calcular promedio
promedio = (nota1 + nota2 + nota3) / 3

# Calcular los puntos que faltan para llegar a 5.0
faltante = 5.0  - promedio

# Determinar si el estudiante aprueba
aprueba = promedio >= 3.0

# Mostrar los resultados

print("Primera nota:", nota1)
print("Segunda nota:", nota2)
print("Tercera nota:", nota3)
print("Promedio:", round(promedio, 2))
print("Puntos para llegar a 5.0:", round(max(0, faltante), 2))

if aprueba:
    print("Resultado: Aprobado")
else:
    print("Resultado: Reprobado")


























