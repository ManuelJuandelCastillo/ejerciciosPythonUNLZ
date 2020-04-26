print("\n************************************************************************")
print("Programa que trabaja con listas de numeros")
print("************************************************************************\n")

import random

def modificar(lista):
    sinRepetir = list(set(lista))
    sinRepetir.sort(reverse=True)
    listaFinal = []

    for numero in sinRepetir:
        if numero % 2 == 0:
            listaFinal.append(numero)
    print('Lista ordenada, sin repetidos ni impares: ', listaFinal)
    suma = 0
    for numero in listaFinal:
        suma += numero

    listaFinal.insert(0, suma)
    print('Lista final con la suma de sus elementos en la primera posición: ', listaFinal)


listaOriginal = []
for i in range (1,21):
    listaOriginal.append(random.randint(1, 50))

print('La lista original: ', listaOriginal)
modificar(listaOriginal)
