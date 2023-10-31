menu = "MENU: | 1=Imprimir numeros del 1 al 10 | 2= Imprimir solo numeros impares | 3= Mostar menu | 0=Salir"
print(menu)
while True:
    print(" ")
    election = int(input("Ingrese 0 - 1 - 2 - 3: "))
    
    if election == 1: #Opcion 1
        print("Numeros del 1 al 10") #Imprimir numeros del 1 al 10
        for i in range(1,10):
            print(i, end="-")
            continue
    elif election ==2: #Opcion 2
        print("Numeros impares") #Imprimir numeros impares del 1 al 20
        for i in range(1,20,2):
            print(i, end="-")
            continue
    elif election == 3: #Opcion 3
        print(menu) #Volver a mostrar el menu
        continue
    elif election == 0: #Opcion 0
        break #Cortar con el ciclo
    else:
        print("Invalido") #Opcion invalida
        continue    #Volver a mostrar menu
