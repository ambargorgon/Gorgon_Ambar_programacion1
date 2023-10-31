# EJERCICIO 1
"""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

displacement = int(input("Ingrese el corrimiento de la encriptacion: "))

#Repeticion por cada uno de los oficiales
for k in range(1,6):
    word = input(f"Ingrese la palabra a encriptar para el oficial {k}: ").lower()
    word_list = list(word)

    for j in range(0, len(word_list)):
        for i in range(0, len(alphabet)):
            if word_list[j] == alphabet[i]:
                #Asignacion de nueva letra
                word_list[j] = alphabet[(i+displacement)%27]
                break


    print(f"Mensaje para oficial {k}")

    for letter in word_list:
        print(letter, end="")
    print("")
"""


# EJERCICIO 2
"""
nums_array = []

num = int(input("Ingrese un numero: "))

while num != 0 or num < 0:
    nums_array.append(num)
    num = int(input("Ingrese otro numero o 0 para salir: "))

total_evens = 0
total_odds = 0

for n in nums_array:
    qtt_even = 0

    qtt_odd = 0

    aux = n

    while aux != 0:
        digit = aux % 10

        if digit % 2 == 0:
            qtt_even += 1
            total_evens += 1
        else:
            qtt_odd += 1
            total_odds += 1

        aux = int(aux / 10)

    print(f"{n}: PARES {qtt_even} | IMPARES {qtt_odd}")

print("-------------------------")
print("TOTAL PARES:", total_evens)
print("TOTAL IMPARES:", total_odds)
"""