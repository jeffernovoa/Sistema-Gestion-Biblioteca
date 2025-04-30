from book_genre import BookGenre
from employee import Employee
from user import User

def main():
    # Listas para almacenar libros y usuarios
    books = []
    users = []

    # Crear un empleado
    empleado = Employee("Ana", 1)

    # Registrar un usuario
    usuario = empleado.register_user(users, "Carlos", 100)

    # Agregar libros
    libro1 = empleado.add_book(books, "1984", "George Orwell", BookGenre.FICTION)
    libro2 = empleado.add_book(books, "El origen de las especies", "Charles Darwin", BookGenre.SCIENCE)

    # Usuario toma prestado un libro
    usuario.borrow_book(libro1)

    # Usuario intenta tomar prestado el mismo libro nuevamente
    usuario.borrow_book(libro1)

    # Usuario devuelve el libro
    usuario.return_book(libro1)

    # Usuario intenta devolver un libro que no tiene
    usuario.return_book(libro2)

if __name__ == "__main__":
    main()
