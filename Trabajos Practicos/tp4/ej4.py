print("Cuando quiera salir ingrese 0")
primes = 0
is_prime= False

while True:
    num = int(input("Ingrese un numero: "))
  
    if num == 0: #Condicion de salida
        break
    
    es_primo = True         #Es primo a menos que no lo sea
    for i in range(2, num):
        if num % i == 0: #Falso si se divide por otro numero
            es_primo = False
            break
    
    if es_primo:
        primes += 1 #Acumulador de numeros primos
    
print("Cantidad de numeros primos ingresados: ",primes)
