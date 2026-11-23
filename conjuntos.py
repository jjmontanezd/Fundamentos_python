#CONJUNTOS -SETS

# ESTRUCTURA BASICA DE UN CONJUNTO

conjunto = {"elemento_1", "elemento_2", "elemento_3"}
print(type(conjunto))  # class set


# DECLARAR UN CONJUNTO VACIO
conjunto_2 = set()
print(type(conjunto_2))  # class set


# CREAR UN DICCIONARIO VACIO
conjunto_3 = {}
print(type(conjunto_3))  # class dict

# CREAR UN CONJUNTO (no permite elemenyos duplicados)
programas = {"ADSO", "SST", "MINERIA", "ADSO", "SST"}
print(programas)

#metodos de los conjuntos

frutas = {"Mango", "Guayaba", "mora"}

#agregar un nuevo elemento al conjunto

frutas.add("fresas")
print(frutas) #{'Mango', 'mora', 'fresas', 'Guayaba'}

frutas.add("mora")#]elemento duplicado 
print(frutas)

#ELIMINAR UN ELEMEMENTO DEL CONJUNTO 
