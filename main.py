from book import Book
from book_genre import BookGenre

def main():
    # Crear algunos libros
    libro1 = Book("Cien años de soledad", "Gabriel García Márquez", BookGenre.FICTION)
    libro2 = Book("Una breve historia del tiempo", "Stephen Hawking", BookGenre.SCIENCE)

    # Mostrar estado inicial
    print(f"¿{libro1.get_title()} disponible? {libro1.is_available()}")

    # Prestar libro
    if libro1.borrow():
        print(f"{libro1.get_title()} ha sido prestado.")
    else:
        print(f"{libro1.get_title()} no está disponible para préstamo.")

    # Intentar prestar nuevamente
    if not libro1.borrow():
        print(f"{libro1.get_title()} ya está prestado.")

    # Devolver libro
    libro1.return_book()
    print(f"{libro1.get_title()} ha sido devuelto. Disponible? {libro1.is_available()}")

if __name__ == "__main__":
    main()
