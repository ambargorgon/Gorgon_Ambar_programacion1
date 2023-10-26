def multiple(a, b):
    #Evaluacion de multiplos
    if a % b == 0:
        return True
    else:
        return False

while True:
    num1 = int(input("Ingrese numero 1: "))
    num2 = int(input("Ingrese numero 2: "))

    #Condicion de ingreso valido
    if num1 >= num2 and num2 != 0:
        print(multiple(num1, num2))
    else:
        print("Ingreso invalido")
        continue
