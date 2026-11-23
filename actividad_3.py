
# Actividad 3: Clasificador de IMC

# Solicitar los datos al usuario
peso = float(input("Digite su peso en kilogramos: "))
estatura = float(input("Digite su estatura en metros: "))

# Calcular el IMC
imc = peso / (estatura ** 2)

# Clasificar el resultado
if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < 25:
    clasificacion = "Normal"
elif imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

# Mostrar el resultado
print("Su IMC es:", round(imc, 2))
print("Su clasificacion es:", clasificacion)
