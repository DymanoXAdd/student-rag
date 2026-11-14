---
paths:
  - "src/**"
  - "notebooks/**"
  - "eval/**"
---

# Security rules

- Synthetic data only. Never load, read, or embed real student records; that needs a new D-entry first.
- LLM-generated SQL runs only on a DuckDB connection opened `read_only=True`, after a guard that accepts exactly one SELECT statement, and with a row limit.
- Values from the user go into SQL as parameters, never as concatenated strings. (The LLM-generated SQL is the one exception, and the guard above covers it.)
- Never `eval`/`exec` model output or build shell commands from it.
- Data files (`*.duckdb`, Chroma dir, Phoenix traces, `data/`) are never committed.
- A new dependency needs Luis's approval; prefer what is already installed.
