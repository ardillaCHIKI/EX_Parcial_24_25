import gradio as gr
from Ejercicio_4.libro_model import Book, BookGenre
from Ejercicio_5.personas import User, Employee

# Estado global de la biblioteca
book_list = []
users = []
employee = Employee(1, "Admin")

# Funciones principales
def add_book(title, author, genre):
    try:
        genre_enum = BookGenre[genre.upper()]
        new_book = Book(title, author, genre_enum)
        book_list.append(new_book)
        return f"Libro '{title}' añadido exitosamente."
    except KeyError:
        return f"Género '{genre}' no es válido. Usa FICTION, NONFICTION, SCIENCE o ART."

def add_user(user_id, name):
    new_user = User(user_id, name)
    users.append(new_user)
    return f"Usuario '{name}' añadido exitosamente."

def borrow_book(user_name, book_title):
    user = next((u for u in users if u._name == user_name), None)
    book = next((b for b in book_list if b.get_title() == book_title), None)
    if not user:
        return f"Usuario '{user_name}' no encontrado."
    if not book:
        return f"Libro '{book_title}' no encontrado."
    if not book.is_available():
        return f"El libro '{book_title}' no está disponible."
    user.borrow_book(book)
    return f"Usuario '{user_name}' tomó prestado el libro '{book_title}'."

def return_book(user_name, book_title):
    user = next((u for u in users if u._name == user_name), None)
    book = next((b for b in book_list if b.get_title() == book_title), None)
    if not user:
        return f"Usuario '{user_name}' no encontrado."
    if not book:
        return f"Libro '{book_title}' no encontrado."
    user.return_book(book)
    return f"Usuario '{user_name}' devolvió el libro '{book_title}'."

def list_books():
    if not book_list:
        return "No hay libros disponibles en la biblioteca."
    response = "Libros en la biblioteca:\n"
    for book in book_list:
        status = "Disponible" if book.is_available() else "Prestado"
        response += f"- {book.get_title()} ({status})\n"
    return response

# Interfaz Gradio
def biblioteca_interface(action, param1="", param2=""):
    if action == "Añadir Libro":
        title, author, genre = param1, param2.split(",")[0], param2.split(",")[1]
        return add_book(title, author, genre)
    elif action == "Añadir Usuario":
        user_id, name = int(param1), param2
        return add_user(user_id, name)
    elif action == "Prestar Libro":
        user_name, book_title = param1, param2
        return borrow_book(user_name, book_title)
    elif action == "Devolver Libro":
        user_name, book_title = param1, param2
        return return_book(user_name, book_title)
    elif action == "Listar Libros":
        return list_books()
    else:
        return "Acción no válida."

# Configuración de la interfaz Gradio
actions = ["Añadir Libro", "Añadir Usuario", "Prestar Libro", "Devolver Libro", "Listar Libros"]
interface = gr.Interface(
    fn=biblioteca_interface,
    inputs=[
        gr.Dropdown(choices=actions, label="Acción"),
        gr.Textbox(label="Primer parámetro"),
        gr.Textbox(label="Segundo parámetro"),
    ],
    outputs="text",
    title="Sistema de Gestión de Biblioteca"
)

interface.launch()


