[English version](README.md)

# Directorio de Empleados y Contratos Laborales

## Objetivo del Proyecto

Este proyecto implementa una aplicación de terminal en Python para gestionar un directorio de empleados y sus contratos laborales usando almacenamiento en JSON.

## Estructura del Proyecto

- `gestor_empleados.py`: operaciones CRUD de empleados y persistencia en JSON.
- `gestor_contratos.py`: asociación de contratos y consultas por estado del contrato.
- `main.py`: interfaz de menú por terminal.
- `empleados.json`: archivo de datos.
- `tests/`: pruebas unitarias con `pytest`.

## Instalación

1. Usar Python 3.10+.
2. Instalar dependencia de pruebas:

```bash
pip install pytest
```

## Ejecución

Ejecutar la interfaz de terminal:

```bash
python main.py
```

## Pruebas

Ejecutar pruebas con:

```bash
py -m pytest
```

## Ejemplo de Uso

1. Añadir un empleado desde la opción `1` del menú.
2. Asociar un contrato desde la opción `4`.
3. Listar contratos vencidos desde la opción `5`.
4. Listar contratos activos desde la opción `6`.
5. Salir desde la opción `7`.
