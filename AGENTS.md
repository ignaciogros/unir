# AGENTS.md

## Purpose

This document defines the roles, responsibilities, and operational guidelines for agents interacting with this Python project. Agents may include human contributors, automated scripts, CI/CD systems, or AI-based tools.

---

## Project Overview

- **Language:** Python 3.x

---

## Agent Types

### 1. Developer Agents

Responsible for implementing features and fixing bugs.

**Responsibilities:**
- Follow PEP8 style guidelines
- Write unit tests for all new functionality
- Maintain backward compatibility unless explicitly stated
- Use type hints where applicable

---

## Code Standards

- Follow **PEP8**
- Use **type hints** (`typing` module)
- Prefer **dataclasses** for structured data
- Keep functions small and single-purpose
- Avoid global state unless strictly necessary

---

## Testing Guidelines

- Framework: `pytest`
- Minimum coverage: **100%**

Tests must be:
- Deterministic  
- Isolated  
- Fast  

**Test structure:**

    tests/
        test_<module>.py

## Configuration Management

- Use `.env` files for local development
- Never commit secrets
- Provide `.env.example`

---

## Logging

- Use Python `logging` module

Levels:
- DEBUG  
- INFO  
- WARNING  
- ERROR  
- CRITICAL  

---

## Error Handling

- Do not suppress exceptions silently
- Use custom exception classes where needed
- Provide actionable error messages

---

## Security Guidelines

- Validate all external inputs
- Avoid executing arbitrary code
- Keep dependencies updated

---

## Automation Rules for AI Agents

- Do not modify files outside the scope of the task
- Prefer minimal diffs
- Preserve existing code style
- Add tests when adding logic
- Avoid introducing new dependencies unless necessary

---

## Documentation

- All public modules must include docstrings
- Use Google or NumPy docstring format
- Keep README.md updated