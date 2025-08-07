from app.services.gestorEmpleado import GestorEmpledos
from app.models.desarrollador import Desarrollador
from app.models.empleado import Empleado
from app.models.gerente import Gerente

gestorEmpleados = GestorEmpledos()

empleados = [
    Desarrollador("Rodrigo", 3700),
    Desarrollador("Sandro", 3700),
    Desarrollador("Lheyla", 3700),
    Empleado("Juan", 2000),
    Empleado("Flor", 2000),
    Gerente("Pedro", 5000),
]
for empleado in empleados:
    gestorEmpleados.crear_empleado(empleado)


gestorEmpleados.mostrar_empleados()

# resultado = gestorEmpleados.buscar_tipo("Desarrollador")
# print(resultado)

gestorEmpleados.editar_empleados("Rodrigo", "Rodrigou", 3900)

gestorEmpleados.mostrar_empleados()

gestorEmpleados.eliminar_empleado("Flor")

gestorEmpleados.mostrar_empleados()