# Chatbot — Azure OpenAI (Act. 2)

> [Versión en español](README_es.md)

Command-line chatbot that connects to Azure OpenAI (or a local Ollama model) and
maintains a multi-turn conversation with configurable parameters.

## Prerequisites

```
python --version          # 3.10 or later required
pip show openai           # must be installed
pip show python-dotenv    # must be installed
```

If either package is missing, install them after activating the virtual environment
(see next section).

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure credentials

Copy `.env.dist` to `.env` and fill in your Azure values:

```bash
cp .env.dist .env   # macOS / Linux
copy .env.dist .env # Windows
```

Open `.env` and set at minimum:

```
AZURE_ENDPOINT=https://<your-resource>.openai.azure.com/
AZURE_API_KEY=<your-api-key>
AZURE_DEPLOYMENT=<your-deployment-name>
```

All other parameters (`TEMPERATURE`, `MAX_TOKENS`, `TOP_P`, `SYSTEM_PROMPT`) have
working defaults and can be left as-is or adjusted to taste.

## Running the chatbot

```bash
python chatbot.py
```

Type your message and press Enter. Type `salir` to exit.

## Switching models

Change the `PROVIDER` variable in `.env`:

| Value | Description |
|---|---|
| `azure` | Azure OpenAI (default) |
| `ollama` | Local Ollama server — also set `OLLAMA_MODEL` |
| `openai_compat` | Any OpenAI-compatible endpoint — set `COMPAT_ENDPOINT`, `COMPAT_API_KEY`, `COMPAT_MODEL` |

## Running tests

```bash
python -m pytest tests/ -v
```

Tests are unit tests with mocks — no real API calls are made and no credentials are required.
