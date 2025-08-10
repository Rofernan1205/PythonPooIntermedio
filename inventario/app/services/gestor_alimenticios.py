from ..services.gestor import GestorBase
from ..models.productoAlimenticio import ProductoAlimenticio


class GestorAlimenticios(GestorBase):
    clase_modelo = ProductoAlimenticio

    def agregar_producto(self, producto):
        if not isinstance(producto, ProductoAlimenticio):
            raise TypeError("Solo se pueden agregar productos alimenticios")
        self.productos.append(producto)
        self.guardar_en_json()