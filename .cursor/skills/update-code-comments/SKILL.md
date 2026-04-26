---
name: update-code-comments
description: Reviews and improves code comments for clarity and brevity. Use when the user asks to revise comments, clean comment style, enforce concise one-line comments, or remove redundant parameter/return comments.
---

# Update Code Comments

## Goal

Improve code comments without changing behavior.

## Rules

- Keep comments in English.
- Keep comments brief and descriptive.
- Prefer one-line comments whenever possible.
- Remove comments that only restate obvious code.
- Do not document input/output parameters in comments if already clear in function signatures.
- Keep comments only where they add intent or context.

## Workflow

1. Read the target file(s).
2. Identify noisy, redundant, outdated, or long comments.
3. Replace with concise comments only where needed.
4. Keep existing code logic unchanged.
5. Ensure terminology is consistent.

## Output

- Provide a short change list with updated files.
- Mention if no meaningful comment changes were needed.
