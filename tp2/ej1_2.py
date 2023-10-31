pc_years = float(input("Ingrese la antiguedad de su pc: "))

if pc_years < 0: #Condicion de valor negativo
    print("Incorrecto, valor negativo")

if pc_years <= 2: #Condicion de antiguedad
    print("Computador nuevo")
else:
    print("Computador viejo")