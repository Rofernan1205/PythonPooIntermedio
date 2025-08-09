import json
from abc import  ABC, abstractmethod
# @abstractmethod metodo que se repite entre clases hijas , pero comportamiento
# diferente. En caso de que el metodo es lo mismo para las clases hijas mejor
# implementar en la clase padre

class Gestor(ABC):
    def __init__(self, archivo):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_json()

    @abstractmethod
    def agregar_producto(self, producto):
        pass

    def guardar_en_json(self):
        with open(self.archivo, 'w', encoding="utf-8") as file:
            json.dump()









