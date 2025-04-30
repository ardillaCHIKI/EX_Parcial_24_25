from Ejercicio_4.libro_model import Book, BookGenre
from Ejercicio_5.personas import User, Employee

### Ejercico 4 ###
# Crear un objeto de libro y mostrar su información
book1 = Book("El Principito", "Antoine de Saint-Exupéry", BookGenre.FICTION)

# Mostrar información del libro
print(f"Título: {book1.get_title()}, Autor: {book1.get_author()}, Género: {book1.get_genre().value}, ¿Disponible?: {book1.is_available()}")


### Ejercico 5 ###
# Lista de libros
book_list = []

# Crear algunos libros
book1 = Book("El Principito", "Antoine de Saint-Exupéry", BookGenre.FICTION)
book2 = Book("Cien años de soledad", "Gabriel García Márquez", BookGenre.FICTION)

# Crear un empleado
employee1 = Employee(1, "María")

# Añadir libros al sistema
employee1.add_book(book_list, book1)
employee1.add_book(book_list, book2)

# Crear un usuario
user1 = User(101, "Juan")

# Préstamos de libros
user1.borrow_book(book1)
user1.borrow_book(book2)

# Devolución de libros
user1.return_book(book1)

# Eliminar un libro del sistema
employee1.remove_book(book_list, book2)

