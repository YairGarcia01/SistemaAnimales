animales = [{"Especie": "", "Genero": "", "Edad": "", "Estado": "", "Alimentación": ""}]
animales.remove({"Especie": "", "Genero": "", "Edad": "", "Estado": "", "Alimentación": ""})

#numero = int(input("¿Cuántos usuarios deseas agregar? "))
#for i in range(numero):
especie = input("\nIngrese especie: ")
genero = input("Ingrese el genero: ")
edad = input("Ingrese su edad: ")
salud = input("Ingrese su estado de salud acutal: ")
comida = input("Ingrese tipo de alimentación: ")
animales.append({"Especie": especie, "Genero": genero, "Edad": edad, "Salud": salud, "Alimentación": comida})
print("\n")
#for contacto in animales:
#    print(f"Nombre del contacto: {contacto['nombre']} " 
#    + f" Numero del telefono: {contacto['telefono']}\n")
