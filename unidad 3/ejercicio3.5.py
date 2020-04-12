print("\n************************************************************************")
print("Programa que eleva al cubo los numeros ingresados")
print("************************************************************************\n")

def cubo(numero):
    return numero**3

while True:
    numero = int(input("Ingrese un numero (0 para salir) >> "))
    if numero == 0:
        break
    
    print("El cubo de", numero, "es", cubo(numero))