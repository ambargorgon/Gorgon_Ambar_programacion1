def validator (num):
    #Tomar longitud del numero convertido a String
    number_length = len(str(num))
    #Evaluar longitud
    if number_length == 8 or number_length == 7:
        return True
    else:
        return False
        
#Solicitud de Datos
dni = int(input("Ingrese numero de DNI: "))

#Imprimir segun retorno
if validator(dni):
   print("Correcto")
else:
    print("No es un numero de dni")


