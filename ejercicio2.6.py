print("\n*********************************************************************************")
print("Programa que permite ingresar una lista determinada de palabras")
print("*********************************************************************************\n")

contador = int(input("Ingrese el numero de palabras a ingresar: "))

frase = list()

for palabra in range(contador):
    frase.append(input("Ingrese una palabra: "))

print("las palabras ingresadas son: ")
for palabra in frase:
    print(palabra, end=',')

