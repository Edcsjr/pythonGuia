"""
Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).
"""

edad=input("ingresa edad: ")

edad=int(edad) #transforma el dato en entero y lo asigna a la variable edad
if edad > 18:
    print('eres mayor de edad')
elif edad >= 13 and edad <=17:
    print('eres  adolecente')

else:
    print('eres menor de 13 a;os')
