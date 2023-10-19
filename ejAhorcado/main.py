import random
from funciones import *

words = ["break", "continue", "while", "switch", "print"]
chosen_word = random.choice(words)
print("Palabra", chosen_word)

# imprimir espacio incial
guess = ["_"]*len(chosen_word)
print(" ".join(guess))

tries = 5

while tries > 0:
    letter = input("Ingresa letra: ")
    # imprimir situacion actual
    if letter in chosen_word:
        guess = new_guess(guess, letter, chosen_word)
    else:
        tries -= 1 
        print(f"Incorrecto, te quedan {tries} intentos")
          
    print(" ".join(guess))
    if letter == chosen_word or chosen_word == ''.join(guess):
        break

if tries != 0:
    print("Ganaste")
