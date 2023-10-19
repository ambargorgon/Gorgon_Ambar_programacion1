# Maquina expendedora
#GRUPO G = GORGON - GUERRERO
products = [
    "Coca Cola",
    "Coca Zero",
    "Sprite",
    "Fanta",
    "Agua sin gas",
    "Agua con gas",
    "Lata Coca",
    "Lata Coca Zero",
    "Lata Sprite",
    "Lata Fanta",
]
prices = [500, 500, 500, 500, 400, 400, 300, 300, 300, 300]
stock = [5,6,4,0,10,9,6,6,5,4]

cart = []
menu = "1-10: Indice de producto a comprar | 11: Mostrar menu | 0: Finalizar Compra"
organizator = "----------------------------"

#imprimir Menu inicial
print("-------MENU--------")
for i in range(0, len(products)):
    print(f"{i+1}-{products[i]}---${prices[i]}---{stock[i]} unidades")
print(organizator)
print(menu)
print(organizator)

while True:
    choice = int(input("Ingrese numero: "))
    print(organizator)

    #Numero invalido
    if choice < 0 or choice > 11:
        print("Numero invalido, ingrese nuevamente")
        print(menu)
        continue

    #Mostrar menu
    if choice == 11:
        for i in range(0, len(products)):
            print(f"{i+1}-{products[i]}---${prices[i]}---{stock[i]} unidades")
        print(organizator)
        print(menu)
        continue

    #Finalizar compra
    if choice == 0:
        #Finalizar sin compra
        if len(cart) == 0:
            print("Adios!")
            break
        #Carrito
        print("Compra finalizada")
        print("Tu carrito:")
        print(organizator)
        total = 0
        for item in cart:
            print(f"{products[item-1]}---${prices[item-1]}")
            total += prices[item - 1]
        print(f"TOTAL: ${total}")
        break

    #Añadir indice al carrito
    if choice >=1 and choice <=10:
        if stock[choice-1] != 0:
            cart.append(choice)
            print(f"{products[choice-1]} agregado")
            #Disminuir stock
            stock[choice-1] -= 1
            print(f"{stock[choice-1]} unidades restantes")
        else:
            print("No hay mas stock, seleccione otro producto")
            continue