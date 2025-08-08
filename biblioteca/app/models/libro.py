
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self._anio = anio

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        if anio > 0:
            self._anio = anio
        else:
            raise ValueError("Año no puede ser negativo")

    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.anio}"

    def __repr__(self):
        return f"Libro({self.titulo}, {self.autor}, {self.anio})"

    def __eq__(self, other):
        return self.titulo == other.titulo and self.autor == other.autor and self.anio == other.anio
    

