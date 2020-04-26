print("\n************************************************************************")
print("Programa que cuenta vocales en una frase")
print("************************************************************************\n")

frase = input('Ingrese la frase: ')

vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for vocal in vocales:
    vocales[vocal] = frase.count(vocal)

print(vocales)

