# Analisis de Matriculas del Centro de Formacion

# 1. Crear los conjuntos

python_curso = {"Ana", "Luis", "Marta", "Carlos", "Sofia", "Pedro"}
java_curso = {"Luis", "Carlos", "Pedro", "Laura", "Diego"}
bd_curso = {"Marta", "Sofia", "Laura", "Ana", "Miguel"}

# 2. Operaciones de conjuntos

# Total de aprendices unicos
todos = python_curso | java_curso | bd_curso
print("Total de aprendices:", len(todos))
print("Aprendices:", todos)

# Aprendices en Python y Java
python_java = python_curso & java_curso
print("Estan en Python y Java:", python_java)

# Solo estan en Python
solo_python = python_curso - java_curso - bd_curso
print("Solo en Python:", solo_python)

# Estan en exactamente dos programas
dos_programas = (python_curso & java_curso) | (python_curso & bd_curso) | (java_curso & bd_curso)
dos_programas = dos_programas - (python_curso & java_curso & bd_curso)
print("En exactamente dos programas:", dos_programas)

# 3. Eliminar nombres repetidos

inscripciones = ["Ana", "Luis", "Ana", "Marta", "Carlos",
                 "Luis", "Sofia", "Pedro", "Ana"]

unicos = set(inscripciones)

print("Aprendices unicos:", len(unicos))
print("Nombres unicos:", unicos)

# 4. Crear diccionario con cantidad de programas

conteo_programas = {
    nombre: (nombre in python_curso) +
            (nombre in java_curso) +
            (nombre in bd_curso)
    for nombre in todos
}

print("Cantidad de programas por aprendiz:")
print(conteo_programas)

# 5. Aprendiz en los tres programas

tres_programas = python_curso & java_curso & bd_curso

print("Aprendices en los tres programas:", tres_programas)