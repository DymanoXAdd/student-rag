# Decisions — learning

<!-- One entry per decision, newest first. Never edit an old entry; add a new one
     that supersedes it. Changing anything recorded here needs human approval. -->

## D-001 — 2026-11-13 — Initial stack and setup
- Status: accepted
- Decision: A fully local hybrid RAG. Python 3.12 + uv; DuckDB for structured student
  tables, queried through guarded text-to-SQL; Chroma plus sentence-transformers for
  vector retrieval over text notes; Ollama for the LLM; Arize Phoenix for tracing;
  pytest plus a golden eval set; GitHub Actions running ruff, pytest, and gitleaks;
  Dependabot; MIT license. Synthetic, seeded data with planted patterns only.
- Why: Grades, attendance, and discipline are numbers, and vector search over
  stringified rows answers "average" or "how many" questions badly. Text-to-SQL handles
  those, and vectors handle the qualitative notes. Building both teaches the two core
  RAG patterns. Running fully local costs $0 and keeps student-shaped data off third
  parties. Planted patterns give the eval known answers.
- Alternatives considered: pure vector RAG (simpler, but weak on aggregates); the Claude
  API (better answers, but paid and off-box); LangChain or LlamaIndex (faster to
  start, but they hide the mechanics you're here to learn, so plain Python comes first
  and a framework can come later); pgvector (needs a server); Langfuse (Docker, heavier
  than Phoenix).
- Approved by: Luis, 2026-11-13
