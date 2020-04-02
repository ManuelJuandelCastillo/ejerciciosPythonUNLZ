print("\n************************************************************************")
print("Programa que calcula el factorial de un numero")
print("************************************************************************\n")

def factor(num):
    factorial = 1
    for i in range(1, num+1):
        factorial=factorial*i
    return factorial

numero = int(input("Ingrese el numero para calcular su factorial: "))

print("El factorial de ", numero, " es ", factor(numero))