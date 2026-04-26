[Versión en español](README_es.md)

# Employee Directory and Labor Contracts

## Project Objective

This project implements a Python terminal application to manage an employee directory and their labor contracts using JSON storage.

## Project Structure

- `gestor_empleados.py`: employee CRUD operations and JSON persistence.
- `gestor_contratos.py`: contract association and contract status queries.
- `main.py`: terminal menu interface.
- `empleados.json`: data source file.
- `tests/`: unit tests with `pytest`.

## Installation

1. Use Python 3.10+.
2. Install test dependency:

```bash
pip install pytest
```

## Execution

Run the terminal interface:

```bash
python main.py
```

## Testing

Run tests with:

```bash
pytest
```

## Usage Example

1. Add an employee from menu option `1`.
2. Associate a contract from menu option `4`.
3. List expired contracts from menu option `5`.
