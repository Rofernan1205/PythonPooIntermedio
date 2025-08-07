from ..models.empleado import Empleado
from ..models.gerente import Gerente
from ..models.desarrollador import Desarrollador

class GestorEmpledos():
    def __init__(self):
        self.empleados = []

    def crear_empleado(self, objeto):
        self.empleados.append(objeto)

    def buscar_nombre(self, nombre):
        for empleado in self.empleados:
            if empleado.nombre== nombre:
                return empleado
        return False

    def buscar_tipo(self, tipo):
        desarrollador = []
        for empleado in self.empleados:
            if empleado.tipo == tipo:
                desarrollador.append(empleado)
        return desarrollador

    def editar_empleados(self,nombre, nuevo_nombre=None, nuevo_sueldo=None ):
        empleado = self.buscar_nombre(nombre)
        if empleado:
            if nuevo_nombre:
                empleado.nombre = nuevo_nombre
            if nuevo_sueldo:
                empleado.sueldo = nuevo_sueldo
        else:
            print("Empleado no encontrado")

    def eliminar_empleado(self,nombre):
        empleado = self.buscar_nombre(nombre)
        if empleado:
            self.empleados.remove(empleado)
        else:
            print("Empleado no encontrado")




    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado.to_dict())


