#Subprograma
def digits_calculator(num):
    if num < 10:
        return 1
    else:
        return 1 + digits_calculator(num//10)

#Programa principal
number = int(input("Ingrese un numero: "))
print(f"La cantidad de digitos es: {digits_calculator(number)}")