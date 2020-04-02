import random

print("\n*********************************************************************************")
print("Programa que genera una lista de 50 numeros aleatorios y muestra el mas repetido")
print("*********************************************************************************\n")

lista = []

def buscar_mas_repetido():
    listaSet = set(lista)
    el_mas_repetido = -1
    veces_repetido = 0
    for i in listaSet:
        if lista.count(i) > veces_repetido:
            veces_repetido = lista.count(i)
            el_mas_repetido = i

    return el_mas_repetido

for i in range(50):
    lista.append(random.randint(0,100))

print(lista)
print("El numero mas repetido es el",buscar_mas_repetido())
