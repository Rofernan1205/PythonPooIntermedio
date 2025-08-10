from ..models.producto import Producto


class ProductoElectronico(Producto):
    def __init__(self, id, nombre, precio, stock, garantia_meses):
        super().__init__(id, nombre, precio, stock)
        self._garantia_meses = garantia_meses

    @property
    def garantia_meses(self):
        return self._garantia_meses

    @garantia_meses.setter
    def garantia_meses(self, meses):
        if meses > 0:
            self._garantia_meses = meses
        else:
            raise ValueError("Número de meses no puede ser negativo")

    def to_dict(self):
        datos = super().to_dict()
        datos["garantia_meses"] = self.garantia_meses
        return datos

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"],
                   data["nombre"],
                   data["precio"],
                   data["stock"],
                   data["fecha_caducidad"])

    def __string__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}. Stock: {self.stock}, Fecha_caducidad: {self.garantia_meses}"

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio}, {self.stock}, {self.garantia_meses})"
