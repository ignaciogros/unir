"""Unit tests for employee and contract managers."""

from __future__ import annotations

from gestor_contratos import GestorContratos
from gestor_empleados import GestorEmpleados


def crear_gestores(tmp_path):
    ruta = tmp_path / "empleados_test.json"
    gestor_empleados = GestorEmpleados(str(ruta))
    gestor_contratos = GestorContratos(gestor_empleados)
    return gestor_empleados, gestor_contratos


def test_agrega_empleado_correctamente(tmp_path) -> None:
    gestor_empleados, _ = crear_gestores(tmp_path)

    empleado = gestor_empleados.agregar_empleado("Alice Doe", "Developer")

    assert empleado["id"] == 1
    assert empleado["nombre"] == "Alice Doe"
    assert empleado["cargo"] == "Developer"
    assert empleado["contratos"] == []


def test_elimina_empleado_correctamente(tmp_path) -> None:
    gestor_empleados, _ = crear_gestores(tmp_path)
    empleado = gestor_empleados.agregar_empleado("Bob Stone", "Analyst")

    resultado = gestor_empleados.eliminar_empleado(empleado["id"])

    assert resultado is True
    assert gestor_empleados.buscar_empleado(empleado["id"]) == {}


def test_busca_empleado_correctamente(tmp_path) -> None:
    gestor_empleados, _ = crear_gestores(tmp_path)
    empleado = gestor_empleados.agregar_empleado("Carol Smith", "QA")

    encontrado = gestor_empleados.buscar_empleado(empleado["id"])

    assert encontrado["nombre"] == "Carol Smith"
    assert encontrado["cargo"] == "QA"


def test_empleado_tiene_contrato(tmp_path) -> None:
    gestor_empleados, gestor_contratos = crear_gestores(tmp_path)
    empleado = gestor_empleados.agregar_empleado("David Hall", "Support")

    contrato = gestor_contratos.asociar_contrato(
        empleado["id"],
        "2023-01-01",
        "2027-01-01",
        2500.0,
    )
    recargado = gestor_empleados.buscar_empleado(empleado["id"])

    assert contrato["id_contrato"] == 1
    assert len(recargado["contratos"]) == 1
    assert recargado["contratos"][0]["salario"] == 2500.0


def test_lista_contratos_activos(tmp_path) -> None:
    gestor_empleados, gestor_contratos = crear_gestores(tmp_path)
    empleado = gestor_empleados.agregar_empleado("Eva Gray", "Engineering")

    gestor_contratos.asociar_contrato(
        empleado["id"],
        "2024-01-01",
        "2099-01-01",
        3200.0,
    )

    activos = gestor_contratos.listar_contratos_activos()

    assert len(activos) == 1
    assert activos[0]["id_empleado"] == empleado["id"]
    assert activos[0]["contrato"]["salario"] == 3200.0
