print("Lista original: ")
words = ["pizza", "bebida", "hamburguesa", "anana", "kiwi"]
for word in words:
    print(word, end="-")
print(" ")

for i in range(len(words)):
    # Encontrar el menor indice de la iteracion
    indice_minimo = i
    for j in range(i + 1, len(words)):
        if words[j] < words[indice_minimo]:
            indice_minimo = j

    # Intercambiar el elemento actual con el mínimo encontrado
    words[i], words[indice_minimo] = words[indice_minimo], words[i]

print("Palabras ordenadas:")
for word in words:
    print(word, end="-")





