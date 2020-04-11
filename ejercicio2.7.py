print("\n*********************************************************************************")
print("Programa que identifica si una palabra ya existe en una lista")
print("*********************************************************************************\n")

listaPalabras = list()
for palabra in range(10):
    listaPalabras.append(input("Ingrese una palabra para agregar a la lista: "))

palabra = input("Bien, ahora ingrese una palabra para ver si esta en la lista: ")

if palabra in listaPalabras:
    print(palabra, "esta en la lista")
else:
    print(palabra, "no esta en la lista")