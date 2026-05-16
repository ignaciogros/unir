# Chatbot — Azure OpenAI (Act. 2)

> [English version](README.md)

Chatbot de línea de comandos que se conecta a Azure OpenAI (o a un modelo local de
Ollama) y mantiene una conversación multi-turno con parámetros configurables.

## Requisitos previos

```
python --version          # Se necesita Python 3.10 o superior
pip show openai           # Debe estar instalado
pip show python-dotenv    # Debe estar instalado
```

Si algún paquete no está instalado, instálalo tras activar el entorno virtual
(ver sección siguiente).

## Configuración

### 1. Crear y activar un entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar las credenciales

Copia `.env.dist` a `.env` y rellena tus valores de Azure:

```bash
copy .env.dist .env   # Windows
cp .env.dist .env     # macOS / Linux
```

Abre `.env` y establece como mínimo:

```
AZURE_ENDPOINT=https://<tu-recurso>.openai.azure.com/
AZURE_API_KEY=<tu-clave-api>
AZURE_DEPLOYMENT=<nombre-de-tu-despliegue>
```

El resto de parámetros (`TEMPERATURE`, `MAX_TOKENS`, `TOP_P`, `SYSTEM_PROMPT`) tienen
valores por defecto funcionales y pueden dejarse tal cual o ajustarse a tu gusto.

## Ejecutar el chatbot

```bash
python chatbot.py
```

Escribe tu mensaje y pulsa Enter. Escribe `salir` para terminar.

## Cambiar de modelo

Modifica la variable `PROVIDER` en `.env`:

| Valor | Descripción |
|---|---|
| `azure` | Azure OpenAI (por defecto) |
| `ollama` | Servidor Ollama local — establece también `OLLAMA_MODEL` |
| `openai_compat` | Cualquier endpoint compatible con OpenAI — establece `COMPAT_ENDPOINT`, `COMPAT_API_KEY`, `COMPAT_MODEL` |

## Ejecutar los tests

```bash
python -m pytest tests/ -v
```

Los tests son unitarios con mocks: no realizan llamadas reales a la API y no requieren credenciales.
