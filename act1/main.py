"""Terminal interface for employee and contract management."""

from __future__ import annotations

from datetime import datetime

from gestor_contratos import GestorContratos
from gestor_empleados import GestorEmpleados

try:
    from colorama import init as colorama_init
except ImportError:  # pragma: no cover
    colorama_init = None

COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_BLUE = "\033[94m"

if colorama_init is not None:
    colorama_init()


def mostrar_exito(mensaje: str) -> None:
    """Print a success message with icon and green color."""
    print(f"{COLOR_GREEN}[SUCCESS] ✅ {mensaje}{COLOR_RESET}")


def mostrar_error(mensaje: str) -> None:
    """Print an error message with icon and red color."""
    print(f"{COLOR_RED}[ERROR] ❌ {mensaje}{COLOR_RESET}")


def mostrar_info(mensaje: str) -> None:
    """Print an informational message with icon and blue color."""
    print(f"{COLOR_BLUE}[INFO] ℹ️ {mensaje}{COLOR_RESET}")


def mostrar_menu() -> None:
    """Print available options for the terminal interface."""
    print("\n=== Directorio de trabajadores ===")
    print("1. Agregar empleado")
    print("2. Eliminar empleado")
    print("3. Buscar empleado")
    print("4. Asociar contrato")
    print("5. Listar contratos vencidos")
    print("6. Listar contratos activos")
    print("7. Salir")


def validar_fechas_contrato(fecha_inicio: str, fecha_fin: str) -> None:
    """Validate date format and logical order for contract dates."""
    try:
        inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    except ValueError as error:
        raise ValueError(
            "Formato de fecha inválido. Use YYYY-MM-DD."
        ) from error

    if inicio > fin:
        raise ValueError("La fecha de inicio no puede ser posterior a la fecha fin.")


def ejecutar() -> None:
    """Run the terminal menu loop."""
    gestor_empleados = GestorEmpleados()
    gestor_contratos = GestorContratos(gestor_empleados)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                cargo = input("Cargo: ")
                empleado = gestor_empleados.agregar_empleado(nombre, cargo)
                mostrar_exito(f"Empleado creado con id {empleado['id']}.")
            elif opcion == "2":
                id_empleado = int(input("ID del empleado: "))
                eliminado = gestor_empleados.eliminar_empleado(id_empleado)
                if eliminado:
                    mostrar_exito("Empleado eliminado.")
                else:
                    mostrar_error("Empleado no encontrado.")
            elif opcion == "3":
                id_empleado = int(input("ID del empleado: "))
                empleado = gestor_empleados.buscar_empleado(id_empleado)
                if empleado:
                    mostrar_info(str(empleado))
                else:
                    mostrar_error("Empleado no encontrado.")
            elif opcion == "4":
                id_empleado = int(input("ID del empleado: "))
                empleado = gestor_empleados.buscar_empleado(id_empleado)
                if not empleado:
                    mostrar_error("Empleado no encontrado.")
                    continue
                fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
                fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
                validar_fechas_contrato(fecha_inicio, fecha_fin)
                salario = float(input("Salario: "))
                contrato = gestor_contratos.asociar_contrato(
                    id_empleado,
                    fecha_inicio,
                    fecha_fin,
                    salario,
                )
                mostrar_exito(f"Contrato creado con id {contrato['id_contrato']}.")
            elif opcion == "5":
                vencidos = gestor_contratos.listar_contratos_vencidos()
                if not vencidos:
                    mostrar_info("No hay contratos vencidos.")
                else:
                    for item in vencidos:
                        mostrar_info(str(item))
            elif opcion == "6":
                activos = gestor_contratos.listar_contratos_activos()
                if not activos:
                    mostrar_info("No hay contratos activos.")
                else:
                    for item in activos:
                        mostrar_info(str(item))
            elif opcion == "7":
                mostrar_info("Saliendo...")
                break
            else:
                mostrar_error("Opción no válida.")
        except ValueError as error:
            mostrar_error(str(error))


if __name__ == "__main__":
    ejecutar()
