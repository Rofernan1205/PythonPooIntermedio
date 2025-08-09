from ..models.producto import Producto


class ProductoElectronico(Producto):
    def __init__(self, id, nombre, precio, stock, fecha_caducidad):
        super().__init__(id, nombre, precio, stock)
        self.__fecha_caducidad = fecha_caducidad



    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "fecha_caducidad": self.fecha_caducidad
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"],
                   data["nombre"],
                   data["precio"],
                   data["stock"],
                   data["fecha_caducidad"])

    def __string__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}. Stock: {self.stock}, Fecha_caducidad: {self.fecha_caducidad}"

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio}, {self.stock}, {self.fecha_caducidad})"
