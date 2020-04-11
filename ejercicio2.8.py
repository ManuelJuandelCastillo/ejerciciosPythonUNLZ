import random

print("\n*********************************************************************************")
print("Programa que busca y reemplaza los numeros pares en una lista")
print("*********************************************************************************\n")

listaNumeros = []
for i in range(10):
    listaNumeros.append(random.randint(1,100))
print("Lista original: ", listaNumeros)


for i in range(10):
    if listaNumeros[i]%2==0:
        listaNumeros[i]="PAR"

print("La lista queda de la siguiente manera: ", listaNumeros)