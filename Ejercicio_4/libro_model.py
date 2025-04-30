from enum import Enum

# Clase Enumerada BookGenre
class BookGenre(Enum):
    FICTION = "Fiction"
    NONFICTION = "Non-Fiction"
    SCIENCE = "Science"
    ART = "Art"

# Clase Book
class Book:
    def __init__(self, title, author, genre, is_available=True):
        self._title = title
        self._author = author
        self._genre = genre
        self._is_available = is_available

    # Métodos Setters y Getters
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_genre(self):
        return self._genre

    def set_genre(self, genre):
        self._genre = genre

    def is_available(self):
        return self._is_available

    def set_availability(self, availability):
        self._is_available = availability
