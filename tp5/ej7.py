def higher_lower(nums):
    higher = 0
    lower = nums[0]
    for num in nums:
        if num > higher:
            higher = num
        elif num < lower:
            lower = num
    print(f"El mayor es: {higher}")
    print(f"El menor es: {lower}")

numbers_array = []

for i in range(0,6):
    number = int(input("Ingrese un numero: "))
    numbers_array.append(number)
#Llamada a funcion
higher_lower(numbers_array)
