# CONDICIONALES IF / ELIF / ELSE

#Estructura de condicional IF :

if True:
    print("se ejecuta la Instrucion")
    
#EJEMPLO DE IF - ELSE

edad = 26

if edad > 18:
    print("Eres un Adulto")
else:
    print("Eres Joven")
    
# ESTRUCTURA DEL ELIF

if False:
    print("La primera Condicion")
elif True:
    print("Segunda Condicion")
elif True:
    print("Tercera Condicion")
else:
    print("Todas ñlas condiciones son False")
    
#EJERCICIO: CLASIFICACION DE EDAD

edad = 100

if edad < 18: #False
    print("Eres meno de edad")
elif edad >= 18 and edad < 65: # false
    print("Eres un adulto")
else:
    print("Eres un adulto mator")
    
#ESTRUCTURA CONDICIONAL ANIDADA

if True:
    if False:
        print("se ejecula la instrucion")
    elif True:
        print("se ejecuta la instrucion")
    else:
        print("No se ejecuta la instruscion")
else:
    print("No se ejecuta la instruscion")
  

# EJERCICIO: CLASIFICACION DE EDAD IF ANIDADO

edad = 12

if edad < 18:
    if edad >= 12 and edad < 18:
        print("Es un adolescente")
    else:
        print("Es un niño")

else:
    if edad >= 18 and edad < 60:
        print("Es un adulto")
    else:
        print("Es un adulto mayor")


# EJERCICIO PARTIDO CON IF

marcador_colombia = int(input("Ingrese el marcador de Colombia: "))
marcador_chile = int(input("Ingrese el marcador de Chile: "))

if marcador_colombia > marcador_chile:
    print("Colombia es el ganador del partido")

elif marcador_colombia == marcador_chile:
    print("Quedamos empatados")

else:
    print("Perdimos el partido")



# OPERADOR TERNARIO

numero = 4

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

print("El numero es par" if numero % 2 == 0 else "El numero es impar")





# 