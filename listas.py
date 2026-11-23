#LISTAS 

#ESTRUCTURA DE UNA LISTA

lista = ["dato_ 1","dato_2","dato_3"]
print(type(lista)) #class list

#LISTA MIXTA
lista_nixta = ["Hola", "123", 3.14, True, ["ADSO", "SST"]]

#LISTA DE APRENDICES SENA ADSO 3233140

# indice:          0          1         2         3       4 
aprendices = ["miguel", "sebastian", "lizeth", "John", "Dayana"]
print(aprendices)

#acceder a un elemento de la lista
print(aprendices[2]) #lizerh

#modificar un elementp de la lista
aprendices[0] = "Luis" 
print(aprendices)

#consultar rando de elemento en las listas
print(aprendices[0:4]) #['Luis', 'sebastian', 'lizeth', 'John']
print(aprendices[2:4]) # ['lizeth', 'John']
print(aprendices[0::2]) # ['Luis', 'lizeth', 'Dayana']


#concatenar listas 
programas_tecnicos=["Sistemas Teleinformáticos","Redes"]
programas_tecnologicos=["ADSO","Topografia"]
programas_SENA= programas_tecnicos+programas_tecnologicos
print(programas_SENA)#se unen los dos

#Extender listas con .extend()
nuevos_programas_tecnicos= ["Inteligencia Artificial","Mineria de Datos","Redes"]
programas_tecnicos.extend(nuevos_programas_tecnicos)
print(programas_tecnicos)#se agregan los nuevos datos 

#Medir la longitud de una lista usando el operador .len()
print(len(programas_tecnicos))#4 elementos tiene la lista
print(len(programas_tecnologicos))#2 elementos tiene 

#contar o buscar elementos repetidos en una lista
print(programas_tecnicos)
print(programas_tecnicos.count("Redes"))#se repite dos veces "Redes" en la lista

# OBTENER EL INDICE DE UN ELEMENTO  .index()