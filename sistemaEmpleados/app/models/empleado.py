class Empleado:
    def __init__(selfl, nombre, sueldo):
        selfl.nombre = nombre
        selfl.__sueldo = sueldo
        selfl.tipo = selfl.__class__.__name__
        selfl.bono = selfl.calcular_bono()

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self,sueldo):
        if sueldo >= 0:
            self.__sueldo = sueldo
        else:
            raise ValueError("Sueldo no puede ser negativo")

    def __str__(self):
        return f"{self.nombre} , S/.{self.sueldo}, S/.{self.bono} , {self.tipo}"

    def __dir__(self):
        return f"Empleado({self.nombre} , {self.sueldo}, {self.bono}, {self.tipo})"

    def __eq__(self, other):
        return self.nombre == other.nombre and self.sueldo == other.sueldo

    def calcular_bono(self):
        return self.sueldo * 0.1

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "sueldo": self.sueldo,
            "bono": self.bono,
            "tipo": self.tipo
        }

