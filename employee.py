from user import User
from book import Book

class Employee:
    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.employee_id = employee_id

    def register_user(self, user_list: list, name: str, user_id: int):
        new_user = User(name, user_id)
        user_list.append(new_user)
        print(f"Usuario registrado: {name} (ID: {user_id})")
        return new_user

    def add_book(self, book_list: list, title: str, author: str, genre):
        new_book = Book(title, author, genre)
        book_list.append(new_book)
        print(f"Libro agregado: {title} de {author}")
        return new_book
