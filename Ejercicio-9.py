"""
Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven
"""

edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]


joven = min(edades)

#print(joven)

posicion=edades.index(joven)

#print(posicion)

name=nombre[posicion]

print(f"El mas joven es {name} con la edad de {joven}")

 