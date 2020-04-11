import os
import msvcrt

def suma():
    os.system('cls')
    print("\tSuma")
    print("**************************************")
    num1 = float(input("Ingrese el primer numero >> "))
    num2 = float(input("Ingrese el segundo numero >> "))
    return num1+num2

def resta():
    os.system('cls')
    print("\tSuma")
    print("**************************************")
    num1 = float(input("Ingrese el primer numero >> "))
    num2 = float(input("Ingrese el segundo numero >> "))
    return num1-num2

def mult():
    os.system('cls')
    print("\tSuma")
    print("**************************************")
    num1 = float(input("Ingrese el primer numero >> "))
    num2 = float(input("Ingrese el segundo numero >> "))
    return num1*num2

def division():
    os.system('cls')
    print("\tDivision")
    print("**************************************")
    num1 = float(input("Ingrese el primer numero >> "))
    num2 = float(input("Ingrese el segundo numero >> "))
    return num1/num2

def frenar():
    print("Presione una tecla para continuar...")
    msvcrt.getch()

def menu():
    print("\t1 - suma")
    print("\t2 - resta")
    print("\t3 - multiplicacion")
    print("\t4 - division")
    print("\ts - salir")
    print("***********************************")



while True:

    os.system('cls')
    print("\n*********************************************************************************")
    print("Menu de operaciones matematicas")
    print("*********************************************************************************\n")
    menu()
    opcion = input("Ingrese la opcion deseada >> ")

    if opcion == "1":
        print("El resultado de la suma es", suma())
        frenar()
    elif opcion == "2":
        print("El resultado de la resta es", resta())
        frenar()
    elif opcion == "3":
        print("La multiplicacion da", mult())
        frenar()
    elif opcion == "4":
        print("La cociente de la division es", division())
        frenar()
    elif opcion == "s":
        break
    else:
        print("Opcion no valida.")
        frenar()
