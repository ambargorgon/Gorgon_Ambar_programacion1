def login(username, password, tries):
    if username == "usuario1" and password == "asdasd":
        print("Login correcto")
        return True, tries
    else:
        tries += 1
        print(f"Usuario o contraseña incorrectos, te quedan {3-tries} intento/s: ")
        return False, tries
    
tries = 0
repetition = False
while tries < 3 and repetition == False:
    username_input = input("Ingresa nombre de usuario: ")
    password_input = input("Ingresa contraseña: ")
    repetition, tries= login(username_input, password_input, tries)