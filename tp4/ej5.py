#Ingreso de años
year1 = int(input("Ingrese un año: "))
year2 = int(input("Ingrese otro año: "))

#Establecer que el año 1 sea menor que el año 2
if year2 < year1: 
    aux = year1
    year1 = year2
    year2 = aux

for i in range(year1, year2):
    if (i % 4 == 0) and i % 100 != 0 or i % 400 == 0 : #Numero divisible por 4 y no por 100, 
        print("bisiesto:", i)                           #a menos que sea 400 
        continue

    if i % 10 == 0:
        print("multiplo", i)
        continue
