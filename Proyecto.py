# Esto es una recreación ficticia del programa de admisiones en vez de un programa autorizado por la Espol
import random as r
import numpy as np
def menu():
    opcion = -1
    print ("")
    print("-----Bienvenidos al programa de admisiones Espol-----")
    print("1. Registrar Usuario")
    print("2. Listado de estudiantes")
    print("3. Simulador de cupos")
    print("4. Registrar calificaciones")
    print("5. Salir")
    while opcion > 5 or opcion < 1:
        print("Ingrese la opcion del menu (1-5): ")
        opcion = int(input())
    return opcion

def agg_usuario(estudiantes, nombres):
    sen = "S"
    while sen == "S":
        extra = []
        # Para evitar problemas de transcripción se escribe en minuscula
        a = input ("Ingrese nombres y apellidos del estudiante: ").lower()
        nombres.append(a)
        o = input("Ingrese el número de cedula: ")
        extra.append(o)
        b = input ("Ingrese el correo electronico: ")
        extra.append(b)
        c = input ("Ingrese numero telefonico: ")
        extra.append(c)
        d = input("¿Es la primera vez que cursa el proceso de nivelación? (S/N)").upper()
        if d == "S":
            extra.append("primera")
        else:
            extra.append("segunda")
        # Esa es la nota inicial al comienzo de la matricula
        extra.append (0)
        estudiantes [a] = extra
        print ("Desea ingresar otro estudiante(S/N):")
        sen = input().upper()
    return estudiantes, nombres

def listado (estudiantes):
    for key, value in estudiantes.items():
        print(key, value)
    for k in estudiantes:
        articuno = 0 in estudiantes[k][4]
        if articuno == True:
            print("Desea modificar alguna ponderación (S/N): ")
            steelix = input().upper()
            if steelix == "S":
                calificaciones(estudiantes)
    return estudiantes

# Esta sección del simluador es satira y no refleja la selección de cupos autorizada de la Espol
# Esta simulación no influye en la ponderación final
def simulador (estudiantes):
    print("Bienvenidos al simulador de cupos de la Espol")
    charmander = input("Desea probar con una ponderación aleatoria (S/N): ").upper()
    if charmander == "S":
        nota = r.randint(0, 10)
        print ("La ponderación seleccionada es: ", nota)
    else:
        nota = float(input("Elija su ponderación final: "))
    if nota < 6:
        print("Su ponderación no es suficiente")
        print("Ha reprobado el curso de nivelación")
        geodude = r.randint(0,100)
        if geodude == 60:
            exit(0)
    elif nota >= 6 and nota < 10:
        print ("No se han encontrado cupos disponibles")
        print ("Acérquese al edificio de admisiones para más información")
    elif nota == 10:
        print("Se ha encontrado un cupo disponible")
        print("Le damos la bienvenida a Espol")
        print("Pronto le enviaremos la información pertinente para la creación de una cuenta Espol")
    else:
        print ("Valor incorrecto")
        print ("Ingrese una nota entre 0 a 10")
    return estudiantes

def calificaciones (estudiantes):
    promedio = 0
    sus = "S"
    while sus == "S":
        print(nombres)
        pika = input("Elija al estudiante: ")
        indice = validar_estudiante(nombres, pika)
        if indice >= 0:
            for k, v in estudiantes.items():
                if k == pika:
                    nota = input("Ingrese su ponderación final: ")
                    for k in estudiantes:
                        estudiantes[pika][4] = nota
                        promedio = calc_promedio(estudiantes)
            print ("Desea modificar alguna ponderación (S/N): ")
            sus = input().upper()
        else:
            "No se ha encontrado el usuario"
    torchic = open("Listado_estudiantes.txt", "w")
    torchic.write("nombres cedula  correo electronico   numero telefonico  matricula  ponderación. \n")
    for k, v in estudiantes.items():
        torchic.writelines(f"{k} {v[0]} {v[1]} {v[2]} {v[3]} {v[4]}\n")
    for k in estudiantes:
        zapdos = any(not 0 for estudiantes[k][4] in estudiantes)
        print(zapdos)
        if zapdos == True:
            torchic.write("El promedio total es: " + repr(promedio))
    torchic.close()
    return estudiantes

def validar_estudiante (nombres, pika):
    j = -1
    for i in range(len(nombres)):
        if pika == nombres[i]:
            j = i
    return j

def calc_promedio (estudiantes):
    magikarp = np.array(list(estudiantes.values()))
    pidgeot = magikarp[:, 4]
    cubone = pidgeot.astype(float)
    staryu = sum(cubone)
    starmie = len(pidgeot)
    promedio = staryu / starmie
    return promedio


nombres = []
estudiantes = {}
while True:
  op= menu()
  if op==1:
      estudiantes, nombres = agg_usuario(estudiantes, nombres)
  if op==2:
      estudiante = listado (estudiantes)
  if op==3:
      estudiantes = simulador (estudiantes)
  if op==4:
      estudiantes = calificaciones (estudiantes)
  if op==5:
    print("Le agradecemos por usar el programa de admisiones Espol")
    exit(0)
