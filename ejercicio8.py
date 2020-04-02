print("\n************************************************************************")
print("Programa que separa las vocales del resto de letras")
print("************************************************************************\n")

vocales = []
consonantes = []

def vocal(frase):
    #funcion que extrae las vocales
    for letra in frase:
        if letra in ("aeiouAEIOU"):
            vocales.append(letra)
        
    return(vocales)

def consonante(frase):
    #funcion que extrae las consonantes
    for letra in frase:
        if letra not in ("aeiouAEIOU"):
            consonantes.append(letra)

    return(consonantes)



frase = input("Ingrese una frase: ")

print("\nfrase original: ", frase)
print("\nVocales: ", vocal(frase))    
print("\nConsonantes: ", consonante(frase))
