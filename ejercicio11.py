print("\n************************************************************************")
print("Programa que encuentra los numeros primos en un rango determinado")
print("************************************************************************\n")

primos = []
def primo(num):
    #un numero n es primo si (n-1)! + 1 es multiplo de n
    factorial = 1

    for i in range(1, num):
        factorial*=i

    if (factorial+1)%num == 0:
        primos.append(num)

min = int(input("Ingrese el numero donde comienza el intervalo: "))
max = int(input("Ingrese el numero en el que termina el intervalo: "))

if min<max:
    for i in range(min, max):
        primo(i)
else:
    print("El segundo numero debe ser mayor que el primero.")

print("Los numeros primos entre",min,"y",max,"son",primos)