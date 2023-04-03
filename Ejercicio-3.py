"""
Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:

e. Producto de los negativos.
"""

ingreso = 0
cont_pares=0
cont_impares=0
mayor= 1000000
flag = 0
flag_mayor=0
menor=0
suma_positivos=0
producto_negativo=0
numero=""



while ingreso < 5:
    i=0
    numero= input(f"Ingresa numero {i+1} ----> ")
    numero=int(numero)
    ingreso += 1
    
    
    if numero >= 0:
        suma_positivos += numero
    else:
        producto_negativo *= numero



    #menor numero ingresado
    if numero < menor or flag == 0:
        menor = numero
        flag = 1

    if numero % 2 == 0 :
        cont_pares += 1
        #umero_par=numero
        if numero > mayor:
            mayor =numero

         #Mayor numero ingresado
        if numero > mayor or flag_mayor == 0:
            mayor = numero
            flag_mayor = 1
    





print(f"Cantidad de pares: {cont_pares}")
print(f"Cantidad de impares: {cont_impares}  ")
print(f"Menor numero: {menor}  ")
print(f"mayor de los pares:  {mayor}  ")
print(f"suma de los positivos:  {suma_positivos}  ")
print(f"producto de los negativos:  {producto_negativo}")


