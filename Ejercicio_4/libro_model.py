from enum import Enum

class BookGenre(Enum):
    FICTION = "Fiction"
    NONFICTION = "Non-Fiction"
    SCIENCE = "Science"
    ART = "Art"

class Book:
    def __init__(self, title, author, genre, is_available=True):
        self._title = title
        self._author = author
        self._genre = genre
        self._is_available = is_available

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def is_available(self):
        return self._is_available

    def set_availability(self, availability):
        self._is_available = availability
