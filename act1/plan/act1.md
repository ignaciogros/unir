# Actividad 1. Sistema de directorio de trabajadores y sus contratos laborales

## Objetivos
Se desarrollará una aplicación en **Python** que administre un directorio de empleados y sus contratos laborales utilizando archivos **JSON** como almacenamiento de datos. La aplicación debe permitir:
*   **Agregar, actualizar y eliminar** empleados.
*   Registrar **contratos laborales** asociados a los empleados.
*   Consultar información de empleados y sus contratos.
*   Generar **reportes básicos** (por ejemplo, empleados con contratos vencidos).
*   Guardar y recuperar información de un archivo JSON.
*   Implementar **pruebas unitarias** sobre las funcionalidades clave.

## Pautas de elaboración

### Módulo `gestor_empleados.py`
*   Maneja la creación, actualización, eliminación y consulta de empleados.
*   Guarda la información en `empleados.json`.
*   **Métodos clave:**
    *   `agregar_empleado(nombre, cargo) → dict`
    *   `eliminar_empleado(id) → bool`
    *   `buscar_empleado(id) → dict`

### Módulo `gestor_contratos.py`
*   Maneja la asociación de contratos laborales a empleados.
*   Permite filtrar contratos **activos y vencidos**.
*   Permite agregar y actualizar contratos de empleados.
*   **Métodos clave:**
    *   `asociar_contrato(id_empleado, fecha_inicio, fecha_fin, salario) → dict`
    *   `listar_contratos_vencidos() → list`

### Módulo `main.py`
*   Ofrece una **interfaz de terminal** para interactuar con el sistema.
*   Ofrece un menú interactivo con opciones para gestionar empleados y contratos.

### Ejemplo de `empleados.json`
```json
{
  "empleados": [
    {
      "id": 1,
      "nombre": "Carlos Pérez",
      "cargo": "Desarrollador",
      "contratos": [
        {
          "id_contrato": 101,
          "fecha_inicio": "2023-02-15",
          "fecha_fin": "2024-02-15",
          "salario": 3500
        }
      ]
    }
  ]
}
```


## Pruebas del proyecto
Implementación de **pruebas unitarias** con la librería `pytest`:
*   Probar que se agrega empleado correctamente.
*   Probar que se elimina un empleado.
*   Probar la búsqueda de un empleado.
*   Probar que un empleado tiene contrato.

## Documentación del proyecto
El **README** incluirá:
*   Objetivo del proyecto.
*   Instrucciones de instalación y ejecución.
*   Ejemplo de uso.

## Extensión y formato
Se entregará en formato **zip** en el campus con el título «`actmod2_nombre_apellido.zip`». Si el proyecto se ha subido a un repositorio de código, se debe incluir el enlace también.

## Rúbrica
| Sistema de directorio de trabajadores y sus contratos laborales | Descripción | Puntuación máxima | Peso |
| :--- | :--- | :--- | :--- |
| **Criterio 1** | Creación del gestor de empleados | 3 | 30 % |
| **Criterio 2** | Creación del gestor de contratos | 3 | 30 % |
| **Criterio 3** | Creación de fichero de entrada e interfaz por terminal | 1 | 10 % |
| **Criterio 4** | Creación de las pruebas solicitados | 2 | 20 % |
| **Criterio 5** | Creación del fichero de documentación Readme.md | 1 | 10 % |
| | **TOTAL** | **10** | **100 %** |
