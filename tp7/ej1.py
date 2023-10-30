# Lista original
list_numbers = [55,623,1,45,7,89,323,44]
print("Lista original:")
for elemento in list_numbers:
    print(elemento, end=" ")
print()

for i in range(0, len(list_numbers)):
    exchange = False

    for j in range(0, len(list_numbers) - i - 1):
        if list_numbers[j] > list_numbers[j + 1]:
            # Intercambiar los elementos si están en el orden incorrecto
            list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]
            exchange = True

    # Enviar si no existen mas intercambios
    if not exchange:
        break

#Imprimir resultado
print("Arreglo ordenado:")
for elemento in list_numbers:
    print(elemento, end=" ")