#Ejercicio 1

# 1. Campus requiere administrar algunos datos de sus Campers
# como por ejemplo, la creación, eliminación o búsqueda de los
# developers, entre otros, por tal razón, ha solicitado el diseño de
# un programa que cuente con el siguiente menú como panel de
# control:

from os import system
from time import sleep 
from res.operations import operations_ftc

def restaure():
    sleep(2)
    system("cls")
    exec_validation()

def program():
    menu = input(
    """
    ----------------Menu-------------------
    1.  CREAR GRUPO ARTEMIS:
    1.1 LISTAR CAMPERS DE ARTEMIS
    1.2 AGREGAR CAMPERS DE ARTEMIS
    1.3 ELIMINAR CAMPERS DE ARTEMIS
    1.4 ORDERAR ALFABETICAMENTE DE LISTA DE ARTEMIS
    1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS
    2.  CREAR GRUPO DE SPUTNIK:
    2.1 LISTAR CAMPERS DE SPUTNIK
    2.2 AGREGAR CAMPERS A SPUTNIK
    2.3 ELIMINAR CAMPERS DE SPUTNIK
    2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK
    2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK 
    3.  SALIR DEL MENU
    Digite opcion: """)
    return menu


def exec_validation():
    options = ["1","1.1","1.2","1.3","1.4","1.5","2","2.1","2.2","2.3","2.4","2.5","3"]
    menuOpcion = program()
    if menuOpcion in options:
        operations_ftc(menuOpcion, restaure)
    else: 
        print("La opcion no esta disponible")
        return restaure()
    
# program in curse    
exec_validation()