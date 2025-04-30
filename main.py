from Ejercicio_4.libro_model import Book, BookGenre

### Ejercico 4 ###
# Crear un objeto de libro y mostrar su información
book1 = Book("El Principito", "Antoine de Saint-Exupéry", BookGenre.FICTION)

# Mostrar información del libro
print(f"Título: {book1.get_title()}, Autor: {book1.get_author()}, Género: {book1.get_genre().value}, ¿Disponible?: {book1.is_available()}")
