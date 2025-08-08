from app.models.libro import Libro
from app.gestorLibros.biblioteca import  Biblioteca

biblioteca = Biblioteca()

libros = [
    Libro("El despertar", "Miguel Mestal", 2024),
    Libro("Aurora", "Eduardo Muñoz González", 2023),
    Libro("Vidas aleatorias", "Yolanda Pérez Pérez", 2023),
    Libro("El hombre entre las máquinas", "Blas M. Vinagre", 2023),
]
for libro in libros:
    biblioteca.agregar_libro(libro)

biblioteca.mostrar_libros()
biblioteca.editar_libro("Yolanda Pérez Pérez","Vidas aleatorias", "Yolanda Pérez Pérez", 2024)
biblioteca.mostrar_libros()
biblioteca.eliminar_libro("Blas M. Vinagre")
biblioteca.mostrar_libros()


