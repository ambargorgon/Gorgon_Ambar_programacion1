def word_cutter(latest):
    #Generar array con las palabras
    phrase_list = latest.split()
    #Tomar la ultima y calcular su longitud
    return len(phrase_list[-1])

word = input("Ingrese una frase: ")
print(f"La longitud de la ultima palabra es de: {word_cutter(word)} caracteres")
