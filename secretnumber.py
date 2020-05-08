"""
Diseña tu juego "Adivina el número secreto" de manera que cada resultado se almacene como un objeto.
Cree un modelo llamado Resultado, que tome los siguientes datos:
.- Puntuación
.- Nombre del jugador
.- fecha
Luego guarde los objetos en un archivo -> results.txt(use el método __dict__, como en la tarea anterior).
"""

import random
import datetime


class Resultado():
    def __init__(self, puntuacion, nombre_jugador, fecha):
        self.puntuacion = puntuacion
        self.nombre_jugador = nombre_jugador
        self.fecha = fecha


def jugar():

    usuario = input("Introduce tu nombre de usuario: ")
    secret = random.randint(1, 30)
    intentos = 0

    while True:
        num_usuario = int(input("Introduzca el numero secreto (Entre 1 y 30)"))
        intentos += 1

        if num_usuario == secret:

            jugador = Resultado(puntuacion=intentos, nombre_jugador=usuario, fecha=str(datetime.datetime.now()))

            with open("results.txt", "a") as results_file:
                results_file.write(str(jugador.__dict__))

            print("Enhorabuena acertaste el numero secreto: " + str(secret))

            print("\nDatos del jugador en la partida: ", jugador.__dict__)

            break

        elif num_usuario > secret:
            print("El numero introducido no es correcto... Prueba con un numero mas pequeño")

        elif num_usuario < secret:
            print("El numero introducido no es correcto... Prueba con un numero mas grande")


while True:
    print("""
    [1].- Jugar a Adivina el numero secreto --->
    [2].- Mostrar registro de todas las puntuaciones --->
    [3].- Salir del juego --->
    """)

    opcion = input("Seleccione la opcion para empezar: ")

    if opcion == "1":
        jugar()

    elif opcion == "2":
        with open("results.txt", "r") as results_file:
            results_file = results_file.readlines()
            print("\nRegistro de puntuaciones: ", results_file)

    elif opcion == "3":
        print("Saliendo de la aplicacion....")

        break

    else:
        print("OPCION INCORRECTA! INTRODUZCA LA OPCION CORRESPONDIENTE (1-3)")