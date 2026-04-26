---
name: update-documentation
description: Updates project documentation to match current behavior. Use when the user asks to update README, usage instructions, setup docs, or keep documentation synchronized with code changes.
---

# Update Documentation

## Goal

Keep project documentation accurate, concise, and aligned with the current codebase.

## Scope

- `README.md`
- Project docs under `docs/`
- Inline developer docs explicitly requested by the user

## Rules

- Write in English unless user requests another language.
- Keep text concise and practical.
- Prefer bullet points and short sections.
- Ensure commands and file paths are valid.
- Remove stale instructions and obsolete references.

## Workflow

1. Read relevant code and existing documentation.
2. Detect mismatches between docs and implementation.
3. Update objective, setup, execution, and usage sections as needed.
4. Add/adjust examples when they improve clarity.
5. Keep formatting clean and consistent.

## Output

- List updated documentation files.
- Summarize what was aligned or corrected.
- Mention any open documentation gaps.
