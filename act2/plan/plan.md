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

## ~~Phase 1 — Project structure~~ ✓ DONE

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

## ~~Phase 2 — Provider adapters (`providers/`)~~ ✓ DONE

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

## ~~Phase 3 — `chatbot.py`~~ ✓ DONE

- Load `PROVIDER` from `.env`; instantiate the matching adapter.
- Load `TEMPERATURE`, `MAX_TOKENS`, `TOP_P` from `.env` (with sensible defaults).
- Define a configurable system prompt via `SYSTEM_PROMPT` in `.env`.
- Maintain conversation history (`messages` list with roles: system / user / assistant).
- Interactive loop: read user input → append to history → call adapter → print response.
- Exit cleanly when user types `salir` (case-insensitive).

---

## ~~Phase 4 — `.env` / `.env.dist`~~ ✓ DONE

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

## ~~Phase 5 — Test with Azure (3 use cases, for the report)~~ ✓ DONE

Three use cases documented in the PDF, each run with TEMPERATURE=0 and TEMPERATURE=1:
1. Book recommendations (adult audience / primary-school audience)
2. Tech stack for a clothes-swap app
3. Short poem about a lonely child in winter

---

## ~~Phase 6 — Cost analysis and optimisation~~ ✓ DONE

Documented in `informe.md` (source) and `docs/Informe_act2_Ignacio_Gros.pdf`:
- Model: gpt-5.4-nano ($0,20/1M input · $0,02/1M cached input · $1,25/1M output)
- 8 real test calls: ~$0,00104 total
- Scale projection: ~$12,45/month at 1.000 active users
- 7 optimisation strategies including prompt caching (×10 saving on cached tokens)

---

## ~~Phase 7 — `README.md` and `README_es.md`~~ ✓ DONE

Both files written with: objective, prerequisites check, venv setup, .env config,
model switching, run instructions, test instructions.

---

## ~~Phase 8 — `docs/report.md`~~ ✓ DONE (as PDF)

Report delivered as `docs/Informe_act2_Ignacio_Gros.pdf` directly.
`docs/report.md` skeleton was not used; may be removed.

---

## ~~Phase 9 — ZIP archive~~ ✓ DONE

`actmod2_Ignacio_Gros.zip` (229,8 KB) generated containing:
```
chatbot.py
providers/
tests/
.env.dist
requirements.txt
README.md
README_es.md
docs/Informe_act2_Ignacio_Gros.pdf
```

---

## Extra (optional, post-submission) — Test with alternative models

Not part of the activity. Run at will after delivery:
- `PROVIDER=ollama`, `OLLAMA_MODEL=llama3.1:8b`
- `PROVIDER=ollama`, `OLLAMA_MODEL=tinyllama`
- `PROVIDER=openai_compat` → qwen25coder
- `PROVIDER=openai_compat` → Mistral-Small
