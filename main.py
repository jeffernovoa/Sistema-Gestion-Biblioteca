import gradio as gr
from book import Book
from book_genre import BookGenre
from employee import Employee
from user import User
from utils import save_data, load_data

# Cargar estado o iniciar
books = load_data("data/books.pkl")
users = load_data("data/users.pkl")
empleado = Employee("Admin", 1)

# Funciones para Gradio
def registrar_usuario(nombre, user_id):
    if any(u.user_id == user_id for u in users):
        return "El ID ya está registrado."
    user = empleado.register_user(users, nombre, user_id)
    save_data(users, "data/users.pkl")
    return f"Usuario {nombre} registrado."

def agregar_libro(titulo, autor, genero_str):
    genero = BookGenre[genero_str]
    libro = empleado.add_book(books, titulo, autor, genero)
    save_data(books, "data/books.pkl")
    return f"Libro '{titulo}' agregado."

def prestar_libro(user_id, titulo):
    user = next((u for u in users if u.user_id == user_id), None)
    book = next((b for b in books if b.get_title() == titulo), None)
    if not user or not book:
        return "Usuario o libro no encontrado."
    if book.is_available():
        user.borrow_book(book)
        save_data(books, "data/books.pkl")
        return f"{user.name} ha prestado '{book.get_title()}'."
    return f"'{book.get_title()}' no está disponible."

def devolver_libro(user_id, titulo):
    user = next((u for u in users if u.user_id == user_id), None)
    book = next((b for b in books if b.get_title() == titulo), None)
    if not user or not book:
        return "Usuario o libro no encontrado."
    user.return_book(book)
    save_data(books, "data/books.pkl")
    return f"{user.name} ha devuelto '{book.get_title()}'."

def disponibilidad_libro(titulo):
    book = next((b for b in books if b.get_title() == titulo), None)
    if not book:
        return "Libro no encontrado."
    return f"'{titulo}' está {'disponible' if book.is_available() else 'prestado'}."

# Opciones de género
generos = [g.name for g in BookGenre]

# Interfaces Gradio
with gr.Blocks(title="Biblioteca") as demo:
    gr.Markdown("# 📚 Sistema de Gestión de Biblioteca")

    with gr.Tab("Registrar Usuario"):
        nombre = gr.Textbox(label="Nombre")
        user_id = gr.Number(label="ID de Usuario", precision=0)
        salida_usuario = gr.Textbox(label="Resultado")
        btn_usuario = gr.Button("Registrar")
        btn_usuario.click(fn=registrar_usuario, inputs=[nombre, user_id], outputs=salida_usuario)

    with gr.Tab("Agregar Libro"):
        titulo = gr.Textbox(label="Título")
        autor = gr.Textbox(label="Autor")
        genero = gr.Dropdown(generos, label="Género")
        salida_libro = gr.Textbox(label="Resultado")
        btn_libro = gr.Button("Agregar")
        btn_libro.click(fn=agregar_libro, inputs=[titulo, autor, genero], outputs=salida_libro)

    with gr.Tab("Prestar Libro"):
        uid_prestamo = gr.Number(label="ID de Usuario", precision=0)
        titulo_prestamo = gr.Textbox(label="Título del Libro")
        salida_prestamo = gr.Textbox(label="Resultado")
        btn_prestar = gr.Button("Prestar")
        btn_prestar.click(fn=prestar_libro, inputs=[uid_prestamo, titulo_prestamo], outputs=salida_prestamo)

    with gr.Tab("Devolver Libro"):
        uid_devolver = gr.Number(label="ID de Usuario", precision=0)
        titulo_devolver = gr.Textbox(label="Título del Libro")
        salida_devolver = gr.Textbox(label="Resultado")
        btn_devolver = gr.Button("Devolver")
        btn_devolver.click(fn=devolver_libro, inputs=[uid_devolver, titulo_devolver], outputs=salida_devolver)

    with gr.Tab("Consultar Disponibilidad"):
        titulo_consulta = gr.Textbox(label="Título del Libro")
        salida_consulta = gr.Textbox(label="Estado")
        btn_consultar = gr.Button("Consultar")
        btn_consultar.click(fn=disponibilidad_libro, inputs=titulo_consulta, outputs=salida_consulta)

demo.launch()
