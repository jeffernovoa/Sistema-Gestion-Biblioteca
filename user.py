from book import Book

class User:
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id
        self.loan_history = []  # historial de todos los libros tomados
        self.borrowed_books = []  # libros actualmente prestados

    def borrow_book(self, book: Book):
        if book.is_available():
            book.borrow()
            self.borrowed_books.append(book)
            self.loan_history.append(book)
            print(f"{self.name} ha tomado prestado: {book.get_title()}")
        else:
            print(f"{book.get_title()} no está disponible para préstamo.")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} ha devuelto: {book.get_title()}")
        else:
            print(f"{self.name} no tiene este libro para devolver.")
