from ..models.libro import Libro

class Biblioteca(Libro):
    def __init__(self):
        self.libros = []

    def agregar_libro(self, objeto):
        self.libros.append(objeto)

    def buscar_por_autor(self, autor):
        for libro in self.libros:
            if libro.autor == autor:
                return libro
        else:
            return None

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.__repr__())

    def editar_libro(self,autor, n_titulo = None, n_autor = None, n_anio = None):
        libro = self.buscar_por_autor(autor)
        if libro:
            if n_titulo:
                libro.titulo = n_titulo
            if n_autor:
                libro.autor = n_autor
            if n_anio:
                libro.anio = n_anio
        else:
            print("No se encuentra libro en la bliblioteca.")

    def eliminar_libro(self,autor):
        libro = self.buscar_por_autor(autor)
        if libro:
            self.libros.remove(libro)
        else:
            print("No se encuentra libro en la bliblioteca.")


