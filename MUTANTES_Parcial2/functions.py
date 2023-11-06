def is_mutant(matrix):
    print("ADN Analizado:")
    for row in matrix:
        print(row)

    coincidence_counter = 0
    coincidence_counter = coincidence_analysis(matrix, "horizontal" , coincidence_counter) #Analizar horizontal
    coincidence_counter = get_vertical(matrix, coincidence_counter) # Convertir Vertical
    coincidence_counter = get_diagonal(matrix, coincidence_counter) # Convertir Diagonal
    coincidence_counter = get_diagonal(mirror_rows(matrix), coincidence_counter) # Convertir diagonal inversas

    print("Cantidad de coincidencias: ", coincidence_counter)
    if coincidence_counter >= 2:
        return True
    else:
        return False

def get_vertical(matrix,coincidence_counter):
    new_vertical_matrix = [[],[],[],[],[],[]]
    #Reordenar matriz
    for j in range(6): #Iterador de columna
        for i in range(6): #Iterador de fila
            new_vertical_matrix[i] += matrix[j][i] 
    #Enviar a analizar
    coincidence_counter = coincidence_analysis(new_vertical_matrix, "vertical",coincidence_counter)
    return coincidence_counter


def get_diagonal(matrix,coincidence_counter):
    new_diagonal_matrix = [[],[],[],[],[]]
   
    #Reordenar matriz
    for i in range(6):
        if i < 4:
            new_diagonal_matrix[0] += matrix[i][i+2] 
        if i < 5:
            new_diagonal_matrix[1] += matrix[i][i+1]
        
        #Diagonal Principal
        new_diagonal_matrix[2] += matrix[i][i] 
        
        if i < 5:
            new_diagonal_matrix[3] += matrix[i+1][i]
        if i < 4:
            new_diagonal_matrix[4] += matrix[i+2][i] 
    #Enviar a analizar
    coincidence_counter = coincidence_analysis(new_diagonal_matrix, "diagonal",coincidence_counter)
    return coincidence_counter

def mirror_rows(matrix):
    mirror_matrix = []
    #Espejar matriz
    for row in matrix:
        mirrored_row = row[::-1]
        mirror_matrix.append(mirrored_row)
    return mirror_matrix


def coincidence_analysis(matrix, typeOfCoincidence, coincidence_counter):
    for row in matrix:
        range_i = 3
        if len(row) == 4: #Alterar rango para analisis diagonales
            range_i = 1
        elif len(row) == 5:
            range_i = 2
    
        for i in range(range_i):
            if row[i] == row[i+1] and row[i+1] == row[i+2] and row[i+2] == row[i+3]: #Evaluar coincidencia de 4 valores en linea
                coincidence_counter += 1 #contador de coincidencias
                print(f"Coincidencia {typeOfCoincidence}")
                break
    return coincidence_counter
                
