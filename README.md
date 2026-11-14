# student-rag

A local hybrid RAG research assistant over **synthetic** student data: grades, courses,
attendance, discipline, demographics, and reading scores. You ask questions in plain
English and get grounded answers with citations about where students struggle and
which groups are affected.

Built as a learning project. Every concept gets a note in [`docs/learning/`](docs/learning/README.md).

- **Hybrid retrieval:** text-to-SQL (DuckDB) for numbers, vector search (Chroma) for notes
- **Fully local:** Ollama LLM, sentence-transformers embeddings, Arize Phoenix tracing
- **Measured:** a golden eval set scored on retrieval hit rate and answer accuracy

> All data is synthetic and generated from a fixed seed. No real student records are used.

Status: in progress. See [`docs/TASKS.md`](docs/TASKS.md).

License: MIT
