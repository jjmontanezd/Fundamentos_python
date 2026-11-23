
# Actividad 2: Analisis de Temperaturas Semanales

# Lista de temperaturas de los 14 dias
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# 1. Mostrar temperaturas usando indices
print("Temperatura del primer dia:", temperaturas[0])
print("Temperatura del ultimo dia:", temperaturas[-1])
print("Temperatura del dia 7:", temperaturas[6])
print("Temperatura del penultimo dia:", temperaturas[-2])

# 2. Mostrar temperaturas usando slicing
primera_semana = temperaturas[0:7]
segunda_semana = temperaturas[7:14]

print("Primera semana:", primera_semana)
print("Segunda semana:", segunda_semana)

# Temperaturas de los dias pares
dias_pares = temperaturas[1:14:2]
print("Temperaturas de los dias pares:", dias_pares)

# Lista en orden invertido
invertidas = temperaturas[::-1]
print("Temperaturas en orden invertido:", invertidas)

# 3. Calcular el promedio de cada semana
promedio1 = sum(primera_semana) / len(primera_semana)
promedio2 = sum(segunda_semana) / len(segunda_semana)

print("Promedio de la primera semana:", round(promedio1, 2))
print("Promedio de la segunda semana:", round(promedio2, 2))

# 4. Comparar los promedios
if promedio1 > promedio2:
    print("La primera semana tuvo mayor temperatura promedio.")
elif promedio2 > promedio1:
    print("La segunda semana tuvo mayor temperatura promedio.")
else:
    print("Las dos semanas tuvieron el mismo promedio.")
