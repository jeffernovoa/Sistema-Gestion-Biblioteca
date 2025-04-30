from book_genre import BookGenre

class Book:
    def __init__(self, title: str, author: str, genre: BookGenre):
        self._title = title
        self._author = author
        self._genre = genre
        self._available = True  # True si está disponible, False si está prestado

    # Getters
    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_genre(self):
        return self._genre

    def is_available(self):
        return self._available

    # Setters
    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

    def set_genre(self, genre):
        if isinstance(genre, BookGenre):
            self._genre = genre

    def set_availability(self, status: bool):
        self._available = status

    # Otros métodos
    def borrow(self):
        if self._available:
            self._available = False
            return True
        return False

    def return_book(self):
        self._available = True
