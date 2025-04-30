from Ejercicio_4.libro_model import Book

class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._borrowed_books = []

    def borrow_book(self, book):
        if book.is_available():
            self._borrowed_books.append(book)
            book.set_availability(False)
            print(f"Libro '{book.get_title()}' prestado a {self._name}.")
        else:
            print(f"Lo siento, el libro '{book.get_title()}' no está disponible.")

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.set_availability(True)
            print(f"Libro '{book.get_title()}' devuelto por {self._name}.")
        else:
            print(f"{self._name} no tiene el libro '{book.get_title}'.")

class Employee:
    def __init__(self, employee_id, name):
        self._employee_id = employee_id
        self._name = name

    def add_book(self, book_list, book):
        book_list.append(book)
        print(f"Libro '{book.get_title()}' añadido al sistema por {self._name}.")

    def remove_book(self, book_list, book):
        if book in book_list:
            book_list.remove(book)
            print(f"Libro '{book.get_title()}' eliminado del sistema por {self._name}.")
        else:
            print(f"El libro '{book.get_title()}' no se encontró en el sistema.")
