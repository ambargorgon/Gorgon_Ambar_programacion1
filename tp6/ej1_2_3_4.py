# Ejercicio 1, 2 3, y 4
list_of_numbers = []
while True:
    number = int(input("Ingrese un numero, 0 para salir: "))

    if number == 0: #Cortar ciclo
        print(list_of_numbers)
        sum = 0
        for num in list_of_numbers:
            sum += num #Generar suma de numeros
        print(f"Suma total de los numeros: {sum}")
        break

    for num in list_of_numbers:
        if number == num:  # Evaluar coincidencias
            print("Valor repetido en lista. Ultimo añadido al final")
            list_of_numbers.remove(num)  # Eliminar primer coincidencia
        break

    # Añadir nuevo numero al array
    list_of_numbers.append(number)

#Lista de elementos menores al input
list_of_minor_nums = []
bigger_number = int(input("Ingrese un numero para crear una lista con sus menores: ")) #Solicitar input

for num in list_of_numbers:
    if num < bigger_number: #Realizar comparacion
        list_of_minor_nums.append(num) #Agregar a nueva lista
        print(num, end="-")
print(" ")
