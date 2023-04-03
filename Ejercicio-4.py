"""
Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.'
"""


edad=int(input("ingresa tu edad: "))
while edad < 1 or edad >100:
    edad=int(input("Error ingresa una edad correcta por favor: "))
    
ecivil=input("Ingresa tu estado civil s/ soltero | c/ casado")
while ecivil not in ["s","c"]:
    ecivil=input("Error ingresa tu estado civil s/ soltero | c/ casado")
    
    
if edad < 18 and ecivil=="c" :
    print("Eres muy chico para no estar soltero")