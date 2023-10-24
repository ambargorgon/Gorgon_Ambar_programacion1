#funcion para descubrir nueva letra
def new_guess(guess, letter, chosen_word):
    for i in range(0, len(guess)):
        if letter == chosen_word[i]:
            guess[i] = letter
    return guess    
