print("Hola Mundo")

# TIPO DE ESCRITURA DE LAS VARIABLES -----------------

#CAMELCASE
aprendizSena = "SENA"

#pascalcase
AprndizSena = "SEna"

#snake_case - OK
aprendiz_sena = "SENA"

#REGLAS DE LAS VARIABLES :

nombre_completo_1 = "John Jairo"


# tipos de datos primitivos -------------
nombre = "John"
print(type(nombre))   #str

edad = 32
print(type(edad))     # int

altura = 1.77
print(type(altura))   # float

activo = True
print(type(activo))     # bool

complejo = 2 + 3j
print(type(complejo))#complex

byte = b"Hola"
print(type(byte))#bytes

nulo = None
print(type(nulo))# 

#TIPOS DE DATOS ESTRUCTURAS ----------------------
lista = ["python", "Javascript"] 
print(type(lista))    #list

conjunto = {"Html", "Css"} 
print(type(conjunto))   # set

tupla = ("Java", "Css")
print(type(tupla)) #tuple

diccionario = {"nombre": "John", "edad": 26}
print(type(diccionario)) # dict

rango = range(5)
print(type(rango)) #range

#converscion de tipos de datos o casteo --------------------

#casteo de entero a texto
telefono = 3106557602 # int
print(type(telefono), telefono)

telefono_str = str(telefono) # string
print(type(telefono_str), telefono_str)

#casteo de texto a entero
cedula = "15548858" # string
print(type(cedula), cedula)

cedula_int = int(cedula) # entero
print(type(cedula_int), cedula_int)

#casteo: booleano a entero
matriculado = False
print(type(matriculado)) # bool

matriculado_int = int(matriculado)
print(type(matriculado_int),matriculado_int) # entero 

# cateo de entero a booleano
activo = 1
print(type(activo))# int

activo_bool = bool(activo)
print(type(activo_bool),activo_bool)# bool

# casteo de entero a decimal
promedio = 4.13
print(type(promedio), promedio)# float

promedio_int =int(promedio)
print(type(promedio_int), promedio_int)#entero

#casteo de entero a decimal

edad = 26
print(type(edad),edad) #int

edad_float = float(edad)
print(type(edad_float),edad_float) #float

#casteo de un booleano a un flotante o decimal

beneficio = True
print(type(beneficio), beneficio)# bool

beneficio_float = float(beneficio)
print(type(beneficio_float),beneficio_float)#float

# casteo de decimal a booleANO

descuento = 10.5
print(type(descuento),descuento)#float

descuento_bool = bool(descuento)
print(type(descuento_bool),descuento_bool) # bool

# este es un comentario de una sola linea
"""este es un comentario de varias lineas que se utiliza para esplicar el codigo de manera mas detallada"""

# LA IDENTACION EN PYTHON ---------

# condicional if

if 5 > 2:
    print("5 es mayor que 2")
    
else:
    print("5 no es mayor que 2")
    

# INPUT: ENTRADA DE DATOS

nombre_completo = input("Ingrese tu nombre completo: ")
programa = input("¿Cuál es tu programa de formación? ")

# OUTPUT: SALIDA DE DATOS

print("Hola " + nombre_completo + " Bienvenido al curso de Python")

print("Hola mi nombre es: ", nombre_completo, "y estoy en el programa de: ", programa)

# IMPRESION CON F-STRING

print(f"Hola mi nombre es {nombre_completo}, y estoy en el programa de: {programa}")
