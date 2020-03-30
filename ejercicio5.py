print("\n************************************************************************")
print("Programa que busca divisores")
print("************************************************************************\n")
lista = []
num = int(input("Ingrese un numero entero mayor que 0: "))

for i in range(2,10):
    if num%i == 0:
        lista.append(i)

if len(lista)==0:
    print("No se encontraron divisores exactos.")
else:
    lista.reverse
    print("Se encontraron los siguientes divisores:")
    print(lista)