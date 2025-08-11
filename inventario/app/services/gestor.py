import json
from abc import ABC, abstractmethod


class GestorBase(ABC):
    def __init__(self, archivo):
        self.archivo = archivo
        self.productos = []


    @abstractmethod
    def agregar_producto(self, producto):
        pass

    def guardar_en_json(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.productos], f, indent=4, ensure_ascii=False)

    def cargar_desde_json(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.productos = [self.clase_modelo.from_dict(d) for d in data]
        except FileNotFoundError:
            self.productos = []

    def listar_productos(self):
        for producto in self.productos:
            print(producto)

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.id != id]
        self.guardar_en_json()
