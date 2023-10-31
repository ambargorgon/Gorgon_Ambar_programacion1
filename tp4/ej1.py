num = 0 # Inicial value of 0
while num < 30: #Condicion menor a 30
    num += 1 #Incremento de valor en 1
    if num==15: #Cortar ejecucion si llega a 15
        print("El loop se rompio cuando el numero valia ", num)
        break

    if num ==4 or num ==6 or num==10: #Saltear ejecucion en 4,6 y 10
        print("El numero ", num, "fue salteado")
    else:    
        print( num)

