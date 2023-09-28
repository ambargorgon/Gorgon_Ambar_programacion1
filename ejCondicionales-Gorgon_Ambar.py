date = input("Ingrese fecha actual en formato dia, DD/MM: ").lower()

week_day = date[0:date.find(',')]
day= int(date[date.find(' ')+1:date.find('/')])
month = int(date[date.find("/")+1:])

week_days = ["lunes",'martes','miercoles','jueves','viernes']

#validacion de fecha
if week_day not in week_days or day <1 or day>12 or month <1 or month >12:
    print('Error: fecha invalida')
    pass
else:
    print("wk:",week_day," day:", day," month:", month)


if week_day == week_days[0] or week_day == week_days[1] or week_day == week_days[2]:
    #porcentaje aprobados
    print('DIA DE EXAMEN')
    aprovved =int(input("Ingrese la cantidad de alumnos aprobados: "))
    failed = int(input("Ingrese la cantidad de alumnos desaprobados: "))

    total = aprovved + failed
    aprovved_percentage = int((aprovved *100)/total)
    print(aprovved_percentage,"% de alumnos aprobados")
elif week_day == week_days[3]: 
    #porcentaje asistencia
    print('PRACTICA HABLADA')
    attendance = int(input("Ingrese porcentaje de asistencia: "))
    if attendance > 50:
        print("Asistio la mayoria")
    else:
        print("No asistio la mayoria")
elif week_day == week_days[4]:
   #Prueba nuevo ciclo
    if day == 1 and month == 1 or month ==7:
       print("Comienzo de nuevo ciclo")
       students_amount = int(input("Ingrese cantidad de alumnos: "))
       students_tariff = float(input("Ingrese el arancel: "))
       total_tariff = students_amount*students_tariff
       print("Total: $", total_tariff)
    else:
        print("No es comienzo de ciclo")
        


      


