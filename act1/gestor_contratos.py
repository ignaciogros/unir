"""Contract management module for the activity project."""

from __future__ import annotations

from datetime import date, datetime
from typing import Any

from gestor_empleados import GestorEmpleados


class GestorContratos:
    """Manages employee contracts using the shared JSON data file."""

    def __init__(self, gestor_empleados: GestorEmpleados) -> None:
        self.gestor_empleados = gestor_empleados

    @staticmethod
    def _parsear_fecha(fecha_iso: str) -> date:
        return datetime.strptime(fecha_iso, "%Y-%m-%d").date()

    @staticmethod
    def _siguiente_id_contrato(contratos: list[dict[str, Any]]) -> int:
        if not contratos:
            return 1
        return max(int(contrato["id_contrato"]) for contrato in contratos) + 1

    def asociar_contrato(
        self,
        id_empleado: int,
        fecha_inicio: str,
        fecha_fin: str,
        salario: float,
    ) -> dict[str, Any]:
        if salario <= 0:
            raise ValueError("El salario debe ser mayor a cero.")

        inicio = self._parsear_fecha(fecha_inicio)
        fin = self._parsear_fecha(fecha_fin)
        if inicio > fin:
            raise ValueError("La fecha de inicio no puede ser posterior a la fecha fin.")

        datos = self.gestor_empleados._cargar_datos()
        for empleado in datos["empleados"]:
            if int(empleado["id"]) == id_empleado:
                contratos = empleado["contratos"]
                contrato = {
                    "id_contrato": self._siguiente_id_contrato(contratos),
                    "fecha_inicio": fecha_inicio,
                    "fecha_fin": fecha_fin,
                    "salario": salario,
                }
                contratos.append(contrato)
                self.gestor_empleados._guardar_datos(datos)
                return contrato
        raise ValueError("Empleado no encontrado.")

    def actualizar_contrato(
        self,
        id_empleado: int,
        id_contrato: int,
        fecha_inicio: str,
        fecha_fin: str,
        salario: float,
    ) -> bool:
        if salario <= 0:
            raise ValueError("El salario debe ser mayor a cero.")

        inicio = self._parsear_fecha(fecha_inicio)
        fin = self._parsear_fecha(fecha_fin)
        if inicio > fin:
            raise ValueError("La fecha de inicio no puede ser posterior a la fecha fin.")

        datos = self.gestor_empleados._cargar_datos()
        for empleado in datos["empleados"]:
            if int(empleado["id"]) != id_empleado:
                continue
            for contrato in empleado["contratos"]:
                if int(contrato["id_contrato"]) == id_contrato:
                    contrato["fecha_inicio"] = fecha_inicio
                    contrato["fecha_fin"] = fecha_fin
                    contrato["salario"] = salario
                    self.gestor_empleados._guardar_datos(datos)
                    return True
            return False
        return False

    def listar_contratos_vencidos(self) -> list[dict[str, Any]]:
        hoy = date.today()
        vencidos: list[dict[str, Any]] = []
        datos = self.gestor_empleados._cargar_datos()

        for empleado in datos["empleados"]:
            for contrato in empleado["contratos"]:
                fin = self._parsear_fecha(contrato["fecha_fin"])
                if fin < hoy:
                    vencidos.append(
                        {
                            "id_empleado": empleado["id"],
                            "nombre": empleado["nombre"],
                            "contrato": contrato,
                        }
                    )
        return vencidos

    def listar_contratos_activos(self) -> list[dict[str, Any]]:
        hoy = date.today()
        activos: list[dict[str, Any]] = []
        datos = self.gestor_empleados._cargar_datos()

        for empleado in datos["empleados"]:
            for contrato in empleado["contratos"]:
                inicio = self._parsear_fecha(contrato["fecha_inicio"])
                fin = self._parsear_fecha(contrato["fecha_fin"])
                if inicio <= hoy <= fin:
                    activos.append(
                        {
                            "id_empleado": empleado["id"],
                            "nombre": empleado["nombre"],
                            "contrato": contrato,
                        }
                    )
        return activos
