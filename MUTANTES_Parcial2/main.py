from functions import *

ejemplo1 = ["AGTTAA",
            "TCATGC",
            "ATAGTA",
            "CGTATT",
            "CTCGAA",
            "TTAAGG"]; #1 Coincidencia diagonal | NO mutante

#Evaluar ejemplo 1
print(f"ADN 1 es mutante? = {is_mutant(ejemplo1)}")
ejemplo2 = ["TTACGA",
            "CCGAGC",
            "TTGTAG",
            "AGATGA",
            "CCCCAT",
            "TCACTA"]; #MUTANTE | Horizontal, Diagonal, vertical

#Evaluar ejemplo 2
print(f"ADN 2 es mutante? = {is_mutant(ejemplo2)}")


# #Validador de input
input_dna = []
iterator = 0
print("Ingrese 6 secuencias de 6 letras. Estas solo pueden ser 'A','C','G','T'")
while iterator < 6:
    isValid = True
    input_row = input(f"Ingrese fila {iterator+1}: ").upper() #Ingreso de fila por fila

    if len(input_row) != 6: #Evaluacion de longitud de fila
        isValid = False

    for letter in input_row: #Evaluacion letra por letra del String ingresado
        if letter != 'A' and letter != 'C' and letter != 'G' and letter != 'T':
            isValid = False
            
    #Ingreso correcto
    if isValid:
        input_dna.append(input_row) #Añadir String al array
        iterator += 1
    else:
        print("Error: fila invalida, debe tener 6 letras que pueden ser: 'A','C','G','T'")

#Evaluar ejemplo ingresado
print(f"El ADN ingresado es mutante? = {is_mutant(input_dna)}")
