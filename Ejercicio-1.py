"""
Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona
"""

nombre = input("Ingresa tu nombre: ")
sueldo = input("Ingresa tu sueldo: ")
sueldo=int(sueldo)

aumento= sueldo * 1.1
monto_aumento= sueldo * 0.1


print(f"El  aumento de 10% es igual a: {monto_aumento}")
print(f"El nuevo sueldo con el aumento de 10% es igual a: {aumento}")

