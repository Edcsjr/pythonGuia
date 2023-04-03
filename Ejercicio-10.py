"""
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5]

"""
nombres = []
sexo = []
nota = []

contar_nota=0
sumar_nota =0



for i in range(2):
    
    
        
    name=input(f"Ingresa el {i+1} nombre de alumno---> ")
    while  type(name) != str:
        name=input(f"#Error# Ingresa el {i+1}  nombre del alumo--->")
    nombres.append(name)
    
    genero=input("Ingresa sexo de alumno m/f--->")
    while genero not in ["m","f"]:
        genero=input("#ERROR#  Ingresa sexo de alumno m/f--->")
    sexo.append(genero)
   

    
    
    puntaje=int(input(f"Ingresa nota de alumno {name} ---->"))
    while type(puntaje) !=int or puntaje < 0 :
        puntaje=int(input(f"#ERROR#Ingresa nota de alumno {name} ---->"))
    nota.append(puntaje)
    

    
    if genero =="f":
        contar_nota +=1e.fromkeys(x, y)
        sumar_nota += puntaje

promedio = sumar_nota/contar_nota
    
minima=min(nota)
posicion=nota.index(minima)
hombre_baja_nota=nombres[posicion]



print(f"La nota minima es de {minima} y pertenece a {hombre_baja_nota}")
    
print(f"promedio de nota de chicas {promedio}")