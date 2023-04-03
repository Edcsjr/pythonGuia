"""
Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:

-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%

-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%

-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.


Validar el ingreso de datos
"""
estacion=""
localidad=""
tarifa=15000

print("#######Bienvenido a la agencia de viaje########\n")

estacion=input("Ingresa la estacion en la cual viajaras i=invierno / v=verano / o=oto;o / p=primavera--> ")
localidad = input("Ingresa la localidad bar=bariloche / cat=catarata / mdp=mar de p. / c=cordoba--> ")

while estacion not in ["i","v","o","p"] or localidad not in ["bar","cat","mdp","c"]:
    estacion=input("Error selecciona stacion en la cual viajaras i=invierno / v=verano / o=oto;o / p=primavera --> ")
    localidad = input("Error la localidad bar=bariloche / cat=catarata / mdp=mar de p. / c=cordoba--> ")
    

match(estacion+localidad):
    case "ibar":
        print(f" La tarifa de invierno/bariloche es de {tarifa*1.20}")
    case "ic" | "icat":
        print(f"La tarifa de cataratas y cordoba en invierno es de: {tarifa-tarifa*0.1}")
    case "imdp":
        print(f"La tarifa de mar de plata en invierno es de: {tarifa-tarifa*0.2}")
    case "vbar":
        print(f"La tarifa de bariloche en verano es de: {tarifa-tarifa*0.2}")
    case "vcat" | "vc":
        print(f"La tarifa de verano/cordoba/cataratas es de: {tarifa*1.1}")
    case "vmdp":
        print(f"La tarifa de verano/Mar de p. es de: {tarifa*1.2}")
    case "obar" | "pbar" | "ocat" | "pcat" | "omdp" | "pmdp":
        print(f"La tarifa de oto;o/primavera/ bariloche es de: {tarifa*1.1} ")
    case "oc" | "pc":
        print(f"La tarifa a cordoba es de {tarifa}")
    case _:
        print("Error")
        exit()
        