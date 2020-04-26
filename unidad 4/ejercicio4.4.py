print("\n************************************************************************")
print("Programa que muestra los numeros mas repetidos de una lista")
print("************************************************************************\n")

import random

################################################
# declaracion de variables y listas
masRepetido1 = []
masRepetido2 = []
rep1 = 0
rep2 = 0

################################################
# genrar lista random de numeros
lista = []
for i in range(1,21):
    lista.append(random.randint(1,5))

print('Lista random:', lista)
lista.sort()

################################################
# usamos los numeros de la lista sin repetir como claves del diccionario
contador = dict.fromkeys(set(lista))

################################################
# contamos cuantas veces se repite cada numero y se lo asigna a la clave que le corresponde
for numero in contador:
    contador[numero] = lista.count(numero)

print('\nveces que se repite cada numero:', contador)

################################################
# recorremos el diccionario y vamos ubicando los mas repetidos en su lista correspondiente
for clave in contador:
    if contador[clave]>rep1:
        rep2=rep1
        rep1=contador[clave]
        masRepetido2.clear()
        masRepetido2.extend(masRepetido1)
        masRepetido1.clear()
        masRepetido1.append(clave)
    elif contador[clave]==rep1:
        masRepetido1.append(clave)
    elif contador[clave]>rep2 and contador[clave]<rep1:
        rep2=contador[clave]
        masRepetido2.clear()
        masRepetido2.append(clave)
    elif contador[clave]==rep2:
        masRepetido2.append(clave)
    
################################################
# mostramos por consola las listas obtenidas
print('\nNumero/s mas repetido/s : ', masRepetido1 , 'veces repetido:',rep1)
print('\nSegundo/s Numero/s mas repetido/s : ', masRepetido2 , 'veces repetido:',rep2)

# excelente ejercicio! me hizo pensar un rato!!!