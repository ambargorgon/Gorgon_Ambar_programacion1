import math

def area_calculator(ratio):
    area = math.pi * ratio**2
    
    # Calcular la circunferencia del círculo (C = 2 * π * r)
    circunferencia = 2 * math.pi * ratio
    
    return area, circunferencia


ratio_input = float(input("Ingrese el radio de la circunferencia: "))
area, circunferencia = area_calculator(ratio_input)

print(f"Área del círculo: {area}")
print(f"Circunferencia del círculo { circunferencia}")