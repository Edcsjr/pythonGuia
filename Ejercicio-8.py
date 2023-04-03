"""
Ejercicio 7:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar los numeros repetidos.

"""

lista=[82, 3, 49, 38, 94, 38, 97, 92, 64, 8, 75, 37, 67, 45, 78, 55, 48, 78, 29, 58]


for numero in lista:
    if lista.count(numero) >1:
        print(numero, end=" ")