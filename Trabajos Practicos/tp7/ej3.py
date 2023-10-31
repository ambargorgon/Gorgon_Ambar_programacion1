#Lista original
book_list = [
    {
        "name": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year_published": 1925
    },
    {
        "name": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "year_published": 1967
    },
    {
        "name": "1984",
        "author": "George Orwell",
        "year_published": 1949
    },
    {
        "name": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year_published": 1960
    },
    {
        "name": "Don Quixote",
        "author": "Miguel de Cervantes",
        "year_published": 1605
    }
]

#imprimir lista original
for book in book_list:
    print("Titulo:", book["name"])
    print("Autor:", book["author"])
    print("Año de Publicacion:", book["year_published"])
    print("-------------------------------------")

while True:
    print("Elija como desea ordenar el listado de libros")
    choice = int(input("1: Por Titulo | 2: Por Autor | 3: Por Año: ")) #Selector de opciones

    if choice == 1:
        #ORDENAR POR NOMBRE
        by_name = True
        book_list = sorted(book_list, key=lambda x: x["name"]) #sorted() devuelve una nueva secuencia ordenada
    elif choice == 2:
        #ORDENAR POR AUTOR
        by_author = True
        book_list = sorted(book_list, key=lambda x: x["author"])
        break
    elif choice == 3:
        #ORDENAR POR AñO
        by_year = True
        book_list = sorted(book_list, key=lambda x: x["year_published"])
        break
    else:
        #OPCION INVALIDA
        print("Opcion invalida")
        continue

#IMPRIMIR ARRAY ORDENADO    
for book in book_list:
    print("Titulo:", book["name"])
    print("Autor:", book["author"])
    print("Año de Publicacion:", book["year_published"])
    print("-------------------------------------")
    