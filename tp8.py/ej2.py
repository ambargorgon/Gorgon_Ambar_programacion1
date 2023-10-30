def is_power(n, b):
    if n == 1:
        return True
    if n < b or n % b != 0:
        return False
    return is_power(n // b, b)


num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print(f"{num2} es potencia de {num1}? = {is_power(num1, num2)}")
