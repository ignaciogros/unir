"""Employee management module for the activity project."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class GestorEmpleados:
    """Manages employee CRUD operations over a JSON file."""

    def __init__(self, ruta_archivo: str = "empleados.json") -> None:
        self.ruta_archivo = Path(ruta_archivo)
        self._inicializar_archivo()

    def _inicializar_archivo(self) -> None:
        if not self.ruta_archivo.exists():
            self._guardar_datos({"empleados": []})

    def _cargar_datos(self) -> dict[str, list[dict[str, Any]]]:
        with self.ruta_archivo.open("r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def _guardar_datos(self, datos: dict[str, list[dict[str, Any]]]) -> None:
        with self.ruta_archivo.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

    def _siguiente_id(self, empleados: list[dict[str, Any]]) -> int:
        if not empleados:
            return 1
        return max(int(empleado["id"]) for empleado in empleados) + 1

    def agregar_empleado(self, nombre: str, cargo: str) -> dict[str, Any]:
        if not nombre.strip() or not cargo.strip():
            raise ValueError("Nombre y cargo son obligatorios.")

        datos = self._cargar_datos()
        empleados = datos["empleados"]
        empleado = {
            "id": self._siguiente_id(empleados),
            "nombre": nombre.strip(),
            "cargo": cargo.strip(),
            "contratos": [],
        }
        empleados.append(empleado)
        self._guardar_datos(datos)
        return empleado

    def eliminar_empleado(self, id_empleado: int) -> bool:
        datos = self._cargar_datos()
        empleados = datos["empleados"]
        cantidad_inicial = len(empleados)
        datos["empleados"] = [
            empleado for empleado in empleados if int(empleado["id"]) != id_empleado
        ]
        if len(datos["empleados"]) == cantidad_inicial:
            return False
        self._guardar_datos(datos)
        return True

    def buscar_empleado(self, id_empleado: int) -> dict[str, Any]:
        datos = self._cargar_datos()
        for empleado in datos["empleados"]:
            if int(empleado["id"]) == id_empleado:
                return empleado
        return {}
