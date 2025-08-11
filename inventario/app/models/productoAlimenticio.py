from ..models.producto import Producto
import datetime

fecha_actual = datetime.datetime.now().date()


class ProductoAlimenticio(Producto):
    def __init__(self, id, nombre, precio, stock, fecha_caducidad):
        super().__init__(id, nombre, precio, stock)
        self.fecha_caducidad = fecha_caducidad

    @property
    def fecha_caducidad(self):
        return self._fecha_caducidad

    @fecha_caducidad.setter
    def fecha_caducidad(self, fecha):
        f_fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")
        if f_fecha.date() > fecha_actual:
            self._fecha_caducidad = f_fecha.date()
        else:
            raise ValueError("Producto vencido")

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "fecha_caducidad": datetime.datetime.strftime(self.fecha_caducidad,"%d/%m/%Y")
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
