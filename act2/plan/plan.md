# Plan for `act2`

## Deliverables
- `chatbot.py` — main loop, provider selection
- `providers/` — one adapter per model family
- `.env` / `.env.dist` — all credentials and config
- `requirements.txt`
- `tests/` — smoke tests per provider
- `README.md` / `README_es.md`
- `docs/report.md` — skeleton for the PDF report
- `actmod2_Ignacio_Gros.zip` — code-only archive

---

## Phase 1 — Project structure

Create the following layout inside `act2/`:

```
act2/
├── chatbot.py
├── providers/
│   ├── __init__.py
│   ├── azure.py
│   ├── ollama.py
│   └── openai_compat.py
├── tests/
│   └── test_chatbot.py
├── docs/
│   └── report.md
├── .env              ← not committed
├── .env.dist
├── requirements.txt
├── README.md
└── README_es.md
```

---

## Phase 2 — Provider adapters (`providers/`)

### `providers/__init__.py`
- Export `get_provider(name: str) -> BaseProvider`.
- Read `PROVIDER` from env; default to `azure`.

### `providers/azure.py`
- Uses `openai.AzureOpenAI`.
- Reads from `.env`: `AZURE_ENDPOINT`, `AZURE_API_KEY`, `AZURE_DEPLOYMENT`, `AZURE_API_VERSION`.

### `providers/ollama.py`
- Uses `openai.OpenAI` pointed at `http://localhost:11434/v1` (Ollama's OpenAI-compatible layer).
- Reads from `.env`: `OLLAMA_MODEL` (e.g. `llama3.1:8b`, `tinyllama`).

### `providers/openai_compat.py`
- Reusable for any OpenAI-compatible endpoint (qwen25coder, Mistral-Small, others).
- Reads from `.env`: `COMPAT_ENDPOINT`, `COMPAT_API_KEY`, `COMPAT_MODEL`.

All adapters expose the same interface:
```python
def chat(messages: list[dict], temperature, max_tokens, top_p) -> str
```

---

## Phase 3 — `chatbot.py`

- Load `PROVIDER` from `.env`; instantiate the matching adapter.
- Load `TEMPERATURE`, `MAX_TOKENS`, `TOP_P` from `.env` (with sensible defaults).
- Define a configurable system prompt via `SYSTEM_PROMPT` in `.env`.
- Maintain conversation history (`messages` list with roles: system / user / assistant).
- Interactive loop: read user input → append to history → call adapter → print response.
- Exit cleanly when user types `salir` (case-insensitive).

---

## Phase 4 — `.env` / `.env.dist`

`.env.dist` (committed):
```
PROVIDER=azure          # azure | ollama | openai_compat

# Azure
AZURE_ENDPOINT=
AZURE_API_KEY=
AZURE_DEPLOYMENT=
AZURE_API_VERSION=2024-02-01

# Ollama (local)
OLLAMA_MODEL=llama3.1:8b

# OpenAI-compatible (qwen25coder, Mistral-Small, …)
COMPAT_ENDPOINT=
COMPAT_API_KEY=
COMPAT_MODEL=

# Chatbot behaviour
SYSTEM_PROMPT=Eres un asistente útil y conciso.
TEMPERATURE=0.7
MAX_TOKENS=512
TOP_P=1.0
```

`.env` (not committed, holds real secrets).

---

## Phase 5 — Test with Azure (3 use cases, for the report)

Run `chatbot.py` with `PROVIDER=azure` and document:

| # | Scenario | Key parameters to vary |
|---|----------|------------------------|
| 1 | [placeholder — e.g. book recommendations] | temperature ↑ |
| 2 | [placeholder — e.g. technical Q&A] | max_tokens ↓ |
| 3 | [placeholder — e.g. creative writing] | top_p variation |

Capture terminal screenshots for the PDF report.

---

## Phase 6 — Cost analysis and optimisation

- Use Azure Pricing Calculator to estimate cost for each use case.
- Count tokens per request (response includes `usage` in API reply).
- Document at least three optimisation strategies (e.g. shorter system prompt, lower max_tokens, caching repeated queries).

---

## Phase 7 — `README.md` and `README_es.md`

Follow the same structure as `act1/README.md`. Include:
- Project objective.
- Prerequisites check (e.g. `pip show openai`, `python --version`).
- Virtual environment setup (`python -m venv venv` + activation).
- `.env` configuration guide.
- How to switch models.
- Run instructions.

---

## Phase 8 — `docs/report.md`

Skeleton (sections only, to be filled before PDF export):
1. Introducción y objetivos
2. Configuración del entorno Azure
3. Arquitectura del chatbot
4. Casos de uso y pruebas (3 × subsección con capturas)
5. Análisis de costes y optimización
6. Conclusiones

---

## Phase 9 — ZIP archive

Generate `actmod2_Ignacio_Gros.zip` containing:
```
chatbot.py
providers/
tests/
.env.dist
requirements.txt
README.md
README_es.md
```

Exclude: `.env`, `__pycache__`, `.pytest_cache`, `docs/`, `plan/`.

---

## Extra (optional, post-submission) — Test with alternative models

Not part of the activity. Run at will after delivery:
- `PROVIDER=ollama`, `OLLAMA_MODEL=llama3.1:8b`
- `PROVIDER=ollama`, `OLLAMA_MODEL=tinyllama`
- `PROVIDER=openai_compat` → qwen25coder
- `PROVIDER=openai_compat` → Mistral-Small
