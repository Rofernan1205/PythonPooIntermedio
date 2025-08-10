from ..services.gestor import GestorBase
from ..models.productoElectronico import ProductoElectronico


class GestorElectronicos(GestorBase):
    clase_modelo = ProductoElectronico

    def agregar_producto(self, producto):
        if not isinstance(producto, ProductoElectronico):
            raise TypeError("Solo se pueden agregar productos electrónicos")
        self.productos.append(producto)
        self.guardar_en_json()
