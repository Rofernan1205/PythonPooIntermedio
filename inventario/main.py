from app.services.gestor_electronicos import GestorElectronicos
from app.services.gestor_alimenticios import GestorAlimenticios
from app.models.productoAlimenticio import ProductoAlimenticio
from app.models.productoElectronico import ProductoElectronico

gestorElectronicos = GestorElectronicos("productoElectronicos.json")
gestorAlimenticios = GestorAlimenticios("productoAlimenticio.json")

productos = [
    ProductoAlimenticio(1, "Arroz", 23, 12, "12/12/25"),
    ProductoElectronico(2, "Televisión", 400, 5, 12),
    ProductoAlimenticio(3, "Azúcar", 55, 5, "12/12/25"),
    ProductoAlimenticio(4, "Lenteja", 13, 10, "12/12/25"),
    ProductoElectronico(5, "Celular", 800, 12, 10),
]

for producto in productos:
    if isinstance(producto, ProductoAlimenticio):
        gestorAlimenticios.agregar_producto(producto)
    elif isinstance(producto, ProductoElectronico):
        gestorElectronicos.agregar_producto(producto)

print("\n📦 Productos Electrónicos:")
gestorElectronicos.listar_productos()

print("\n🥦 Productos Alimenticios:")
gestorAlimenticios.listar_productos()
