print("\n************************************************************************")
print("Programa que encuentra el mayor y el menor de una lista de numeros")
print("************************************************************************\n")
lista = []
flag = True
while flag:
    num = int(input("Ingrese un numero entero (o 0 para salir): "))
    if num == 0:
        flag = False
    else:
        lista.append(num)

lista.sort()
print("El menor numero ingresado es el ", lista[0])
print("El mayor numero ingresado es el ", lista[len(lista)-1])