print("\n************************************************************************")
print("Programa que cuenta los numeros pares en un rango")
print("************************************************************************\n")

num1 = int(input("Ingrese un numero entero positivo: "))
num2 = int(input("Ingrse otro entero positivo: "))
contador = 0
if num1>num2:
    for numero in range(num2, num1+1):
        if numero%2==0:
            contador+=1
else:
    for numero in range(num1, num2+1):
        if numero%2==0:
            contador+=1

print("Entre los numeros dados hay ", contador , "numeros pares")