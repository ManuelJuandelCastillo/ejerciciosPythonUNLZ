print("\n************************************************************************")
print("Programa que determina si el numero ingresado es primo")
print("************************************************************************\n")

def primo(num):
    #un numero n es primo si (n-1)! + 1 es multiplo de n
    factorial = 1
    resultado = ""

    for i in range(1, num):
        factorial*=i

    if (factorial+1)%num == 0:
        resultado = "es primo"
    else:
        resultado = "no es primo"

    return resultado

numero = int(input("Ingrese un numero entero: "))

print("El numero",numero, primo(numero))