def temperatureCalculator(min_temp, max_temp):
    media = (min_temp + max_temp) / 2
    return media 

print("Calculador de temperatura media")
min_input = int(input("Ingrese temperatura minima: "))
max_input = int(input("Ingrese temperatura maxima: "))
print(f"La temperatura media del dia es: {temperatureCalculator(min_input, max_input)}")