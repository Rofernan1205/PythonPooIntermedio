class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("Precio no puede ser negativo")

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        if stock > 0:
            self.__stock = stock
        else:
            raise ValueError("Stock no puede ser negativo")

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"],
                   data["nombre"],
                   data["precio"],
                   data["stock"])

    def __string__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}. Stock: {self.stock}"

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio}, {self.stock})"
