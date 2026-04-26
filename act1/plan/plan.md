# Plan for `act1`

1. Create the required project structure in `act1/`:
    - `gestor_empleados.py`
    - `gestor_contratos.py`
    - `main.py`
    - `empleados.json`
    - `tests/`
    - `README.md`

2. Implement `gestor_empleados.py`:
    - Load and persist data in `empleados.json`.
    - Implement required methods:
        - `agregar_empleado(nombre, cargo) -> dict`
        - `eliminar_empleado(id) -> bool`
        - `buscar_empleado(id) -> dict`
    - Add input validation and clear error handling.

3. Implement `gestor_contratos.py`:
    - Associate contracts to employees.
    - Support contract updates.
    - Implement required methods:
        - `asociar_contrato(id_empleado, fecha_inicio, fecha_fin, salario) -> dict`
        - `listar_contratos_vencidos() -> list`
    - Include active/expired contract filtering.

4. Implement `main.py`:
    - Build an interactive terminal menu.
    - Add options to manage employees and contracts.
    - Show concise and clear user feedback.

5. Add tests using `pytest`:
    - Add employee successfully.
    - Remove employee successfully.
    - Find employee by id.
    - Verify an employee has a contract.
    - Target minimum 80% coverage.

6. Write `README.md`:
    - Project objective.
    - Installation and execution steps.
    - Usage example.

7. Final verification before delivery:
    - Run test suite.
    - Confirm required files and methods exist.
    - Validate alignment with `act1.docx` rubric requirements.
