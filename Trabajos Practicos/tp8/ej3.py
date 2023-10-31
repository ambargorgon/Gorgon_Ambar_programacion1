def positions(string, phrase, start = 0, times = []):
    if start > len(string): #caso base
        new_times = list(set(times)) #limpiar elementos repetidos de la lista
        return print(new_times) #retornar impresion de nueva lista
    else:
        times.append(string.find(phrase, start, len(string))) #Añadir encuentro a la lista
        positions(string, phrase, start + 1, times) #volver a llamar comenzando la busqueda una letra mas adelante

#MAIN
positions("amar a al amor amando sambar","am")