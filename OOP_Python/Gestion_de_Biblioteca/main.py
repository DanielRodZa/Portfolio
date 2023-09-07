import os
from libros import libros
from usuarios import usuarios

class Libro:
    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = True

    def __str__(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, ISBN: {self.ISBN}, Disponible: {self.disponible}"

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.libros_prestados = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def agregar_a_prestados(self, libro):
        self.libros_prestados.append(libro)

    def quitar_de_prestados(self, libro):
        self.libros_prestados.remove(libro)
    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo == titulo:
                return libro
        return None

    def prestar_libro(self, titulo, usuario):
        libro = self.buscar_libro(titulo)
        if libro and libro.disponible:
            libro.disponible = False
            usuario.tomar_prestado(libro)
            self.agregar_a_prestados(libro)
            return f"Libro {titulo} prestado a {usuario.nombre}."
        elif libro and not libro.disponible:
            return f"El libro {titulo} no está disponible en este momento."
        else:
            return "Libro no encontrado en la biblioteca"

    def devolver_libro(self, titulo, usuario):
        libro = self.buscar_libro(titulo)
        if libro and not libro.disponible:
            libro.disponible = True
            usuario.devolver_libro(libro)
            self.quitar_de_prestados(libro)
            return f"Libro {titulo} devuelto por {usuario.nombre}"
        elif libro and libro.disponible:
            return f"El libro {titulo} ya está en la biblioteca."
        else:
            return "Libro no encontrado en la biblioteca"

    def verificar_disponibilidad(self, titulo):
        if self.buscar_libro(titulo):
            for libro in self.libros_prestados:
                if libro.titulo == titulo:
                    return f'El libro {libro.titulo} no se encuentra disponible.'
            return f'El libro {titulo} se encuentra disponible.'
        else:
            return f"El libro {titulo} no se encuentra en base de datos"

class Usuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario
        return None

    def __str__(self):
        return f"Lista de Usuarios: {[usuario.nombre for usuario in self.usuarios]}"

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def __str__(self):
        libros_prestados = [libro.titulo for libro in self.libros_prestados]
        return f"Usuario: {self.nombre},Libros prestados: {', '.join(libros_prestados)}"

mi_biblioteca = Biblioteca()
lista_de_usuarios = Usuarios()

def prestar():
    titulo = input("¿Qué libro deseas prestar? ")
    usuario = lista_de_usuarios.buscar_usuario(input("¿A qué usuario vas a prestar el libro? "))
    if usuario:
        return mi_biblioteca.prestar_libro(titulo, usuario)

    return f"El usuario {usuario} no existe en base de datos."

def devolver():
    titulo = input("¿Qué libro deseas devolver? ")
    usuario = lista_de_usuarios.buscar_usuario(input("¿A qué usuario va a devolver el libro? "))
    if usuario:
        return mi_biblioteca.devolver_libro(titulo, usuario)

    return f"El usuario {usuario} no existe en base de datos."


def disponibilidad():
    titulo = input("¿Qué libro deseas buscar? ")
    return mi_biblioteca.verificar_disponibilidad(titulo)

def clearScreen():
    os_name = os.name

    if os_name == 'posix':
        os.system('clear')
    elif os_name == 'nt':
        os.system('cls')

def main():
    for libro in libros:
        libro_agregar = Libro(libro['titulo'], libro['autor'], libro['ISBN'])
        mi_biblioteca.agregar_libro(libro_agregar)

    for usuario in usuarios:
        usuario_agregar = Usuario(usuario)
        lista_de_usuarios.agregar_usuario(usuario_agregar)


    while True:
        opcion = int(input(
            "¿Qué deseas hacer?\n1. Prestar un libro.\n2. Devolver un libro.\n3. Verificar disponibilidad de un "
            "libro\n4. Salir\nElegir opción: "))

        if opcion == 1:
            print(prestar())
            clearScreen()
        elif opcion == 2:
            print(devolver())
            clearScreen()
        elif opcion == 3:
            print(disponibilidad())
            clearScreen()
        elif opcion == 4:
            print("Hasta luego!!")
            clearScreen()
            break
        else:
            print("Por favor selecciona una opción válida.")


if __name__ == "__main__":
    main()