print("\n************************************************************************")
print("Este es un programa que cuenta los numeros pares en un rango determinado")
print("************************************************************************\n")

contador = 0
num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero: "))

for i in range(num1, num2):
    if i%2 == 0:
        contador+= 1

print("Entre ", num1, " y ", num2, " se encontraron ", contador, " numeros pares.")
