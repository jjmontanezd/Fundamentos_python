
nota=5
primera_nota=float(input("ingrese la primera nota "))
segunda_nota=float(input("ingrese la segunda nota "))
tercera_nota=float(input("ingrese la tercera nota "))


promedio= (primera_nota + segunda_nota + tercera_nota)/3

faltante=5.0 -promedio

if nota >=3.0:
    print("Has pasado la materia ")

else:
    print("perdiste la materia ")

print("Primera nota",primera_nota)
print("segunda nota",segunda_nota )
print("tercera nota", tercera_nota)
print("promedio",round(promedio,2))
print("te hace falta llegar a 5", round(max(0, faltante),2))