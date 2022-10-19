from mimetypes import init


print("Sistema de gestion de animales en un zoologico")

def menu():
    opcion = int(input("""Ingrese un numero para acceder a lo que desea: 
    1.- Vacunas
    2.- Tiempo al aire
    3.- Alimentación
    4.- Tipo de animal
    5.- Caracteristicas del animal
    6.- 
    7.- Ingreso a los animales
    8.- Salida del animal
    Ingrese: """))
    while True:
        if opcion == 1:
            print()
            break
        elif opcion == 2:
            print()
            break
        elif opcion == 3:
            print()
            break
        elif opcion == 4:
            menu_animal()
            break
        elif opcion == 5:
            print()
            break
        elif opcion == 6:
            print()
            break


def menu_animal():
    opcion = int(input("""Que tipo de animal desea: 
    1.- Vertebrados
    2.- Mamíferos
    3.- Aves
    4.- Peces
    5.- Reptiles
    6.- Anfibios
    7.- Invertebrados"""))

    while True:
        print("Hola mundo")
        break

menu()