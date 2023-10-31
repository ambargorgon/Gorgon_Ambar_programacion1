total = 0 #Declarar sumador
while True:
    #Ingreso de operacion y monto
    user_input = input("Ingrese D para depositar o R para retirar + valor: ").upper()
    
    if user_input == "": #Cortar ejecucion si el input esta vacio
        print("Operacion Finalizada")
        break
    
    operation = user_input[: user_input.find(" ")] #Extraer tipo de operacion
    amount = int(user_input[user_input.find(" ")+1:]) #Extraer monto

    if operation != "D" and operation !="R": #Operaciones invalidas
        print("operacion invalida, comience nuevamente: ")
        continue
    else:
        if operation == "D": #Suma de operaciones Deposito
            total += amount
        else:
            total -= amount #Suma de operaciones Retiro

print("TOTAL:", total)

