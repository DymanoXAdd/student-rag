---
paths:
  - "tests/**"
  - "eval/**"
  - "**/test_*.py"
---

# Testing rules

- Luis writes the tests. Claude explains what to test and why, and reviews.
- Cover risky logic first: the SQL guard (it must reject INSERT/UPDATE/DELETE/DROP, multiple statements, and comments hiding writes), the data generator (same seed gives the same output, and planted patterns are present), and chunking.
- Unit tests never call Ollama or the network. Use a fixed seed and small fixtures.
- The eval (`eval/`) calls the real local model and is not part of `pytest` or CI.
- Never delete, skip, or weaken a failing test to get a green run. Report it and ask.
- Run `uv run pytest` before calling a task done, and paste the summary line.
