def validator_card(item, card, row):
    # Buscar repeticion en carton
    if item in row:
        return True

    for row in card:
        for num in row:
            if item == num: # Numero repetido 
                return True


def random_validator(num, matrix):
    # Match de random number y numero en carton
    for i in range(0,5):
        row = matrix[i]
        for j in range(0,5):
            if num == row[j]: #Existe match
                print("-------------")
                print(f"MATCH CON {num}")
                row[j] = "X"

                #Imprimir carton
                for row in matrix:
                    print(row)
                print("-------------")
                return matrix #Retornar matriz actualizada
            
    return matrix #Retornar matriz sin coincidencia


def row_validator(matrix):
    # Buscar coincidencia linea vertical
    for i in range(0,5):
        row = matrix[i]  # Recorrer fila
        match = True
        for j in range(0,5):  # Recorrer items
            if row[j] != "X":
                match = False  # No hay match

        if match:
            return True
        else:
            continue
    return False


def column_validator(matrix):
    # Buscar coincidencia linea horizontal
    for column in range(0, 5):  # Posicionar columna
        match = True
        for row in matrix:  # Recorrer filas
            if row[column] != "X":
                match = False  # No hay match

        if match:
            return True
        else:
            continue
    return False


def diagonal_validator(matrix):
    # Buscar coincidencia en diagonal principal
    match = True
    for i in range(0, 5):
        row = matrix[i] #Posicion en fila
        if row[i] != "X": #Posicion en item
            match = False  # No hay match

        if not match:
            return False
        
    return True

    
