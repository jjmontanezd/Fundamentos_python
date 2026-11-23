
# Actividad 3: Gestion de Lista de Reproduccion Musical

# Lista inicial de canciones
canciones = ["Mi Historia", "Adios Amor", "El Aventurero", "Me Bebere Tu Recuerdo", "Nadie Es Eterno"]

print("Lista inicial:", canciones)

# Agregar una cancion al final
canciones.append("Como Duele El Frio")
print("Despues de append:", canciones)

# Agregar una cancion en la segunda posicion
canciones.insert(1, "La Mejor De Todas")
print("Despues de insert:", canciones)

# Agregar varias canciones
canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print("Despues de extend:", canciones)

# Eliminar una cancion por su nombre
canciones.remove("Adios Amor")
print("Despues de remove:", canciones)

# Eliminar la ultima cancion y guardar su valor
eliminada = canciones.pop()
print("Cancion eliminada:", eliminada)
print("Despues de pop:", canciones)

# Ordenar las canciones alfabeticamente
canciones.sort()
print("Lista ordenada:", canciones)

# Responder las preguntas
print("Cantidad de canciones:", len(canciones))
print("Posicion de la primera cancion agregada:", canciones.index("Como Duele El Frio") + 1)
print("Veces que aparece Bonus Track 1:", canciones.count("Bonus Track 1"))
