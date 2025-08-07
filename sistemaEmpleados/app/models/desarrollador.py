from ..models.empleado import Empleado

class Desarrollador(Empleado):

    def calcular_bono(self):
        return self.sueldo * 0.15

    def __str__(self):
        return f"{self.nombre}, S/.{self.sueldo}, S/.{self.bono} , {self.tipo}"

    def __repr__(self):
        return f"Desarrollador({self.nombre} , {self.sueldo}, {self.bono}, {self.tipo})"