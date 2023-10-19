from funciones import *

print("Ingrese un numero o 0 para SALIR")
sum_result = 0
while True:
    number = int(input("Ingrese un numero: "))

    #cortar ciclo    
    if number == 0:
        print(f"La suma de los N ingresados es: {sum_result}")
        print(f"Y la suma de los digitos de {sum_result} es: {digits_sum(sum_result)}")
        print("Adios!")
        break
    else:
        print(f"{number} = {digits_sum(number)}")
        sum_result += number

    

    

