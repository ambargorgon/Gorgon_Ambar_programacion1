def validator(num):
    # Evaluar longitud
    if len(num) == 8 or len(num) == 7:
        return True
    else:
        return False

print("INGRESO DE DATOS")
print("Deje el apartado de nombre vacio si desea salir")
iterator = 1
while True:
    # Ingreso nombre/s
    name = input(f"Ingrese nombre del socio {iterator}: ").title()

    # SALIR
    if name == "":
        print("Adios!")
        break

    # Separacion primer nombre
    first_name = name[0 : name.find(" ")]

    # Ingreso apellido
    last_name = input("Ingrese Apellido: ").title()

    while True:
        # Ingreso de Dni
        dni = input("Ingrese numero de DNI: ")
        if validator(dni):
            break
        else:
            print("DNI invalido, ingrese nuevamente")
            continue
    
    print("USUARIO INGRESADO:")
    print(f"Nombre Completo: {name} {last_name}")
    print(f"DNI: {dni}")
    print(f"ID: {first_name}{len(last_name)}{dni[0:3]}")
    iterator += 1
