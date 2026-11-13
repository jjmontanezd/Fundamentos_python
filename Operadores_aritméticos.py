# OPERADORES ARITMETICOS

a = 10
b = 3

# SUMA

suma = a + b
print(f"La suma de {a} y {b} es: {suma}")

# RESTA

resta = a - b
print(f"La resta de {a} y {b} es: {resta}")

# MULTIPLICACION 

multiplicacion = a * b
print(f"La multiplicacion de {a} y {b} es: {multiplicacion}")

# DIVISION FLOTANTE O DECIMAL

division = a / b
print(f"La division de {a} y {b} es: {division}")

#divicion entera

division = a //b
print(f"La division de {a} y {b} es: {division}")

#MODULO O RESIDUO

modulo = a % b
print(f" el nodulo de {a} entre {b} es: {modulo}")

# PONENCIA O EXPONENCIACION

potencia = a ** b
print(f"la potencia de {a} elevado a {b} es: {potencia}")

#PRECEDENCIA DE OPERADORES ---------------

resultadodo = a + b * 2
print(f"El resultado de la operacion 10 + 3 * 2 es: {potencia}") # 16

resultadodo_2 = (10 + 3 * 2)
print(f"El resusltado de la operacion (10 + 3 ) * 2 es: {resultadodo_2}") # 26

resultadodo_3 = 10 * 3 // 3
print(f"El resusltado de la operacion  10 * 3 // 3 es: {resultadodo_3}") #10

ejercicio = ((a + b) * (b - a) / (a * b)) - ((a**b) % 3)
print(f"el resultado de la operacion es: {ejercicio}")


# LIBRERIAS EN PYTHON 

import math

print(math.pi)
print(math.e)
print(math.sqrt(16))


import random
print(random.random()) # NUMEROS ALEATORIOS ENTRE 0 Y 1

