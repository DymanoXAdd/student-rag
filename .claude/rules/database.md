---
paths:
  - "src/student_rag/data/**"
  - "src/student_rag/sql/**"
  - "**/*.sql"
---

# Database rules

- Only the seeded generator writes to DuckDB. Everything else opens it `read_only=True`.
- There are no migrations: schema changes go in the generator, and the database is rebuilt from scratch.
- Keep the data dictionary in step with the schema; text-to-SQL depends on it.
- Every query the LLM generates gets a row limit (for example `LIMIT 200`) before it runs.
- Demographic columns are synthetic; they would be sensitive if real, so answers report aggregates, never single students.
