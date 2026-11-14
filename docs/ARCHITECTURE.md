# Architecture — learning

<!-- Describe what cannot be read from the code: intent, boundaries, constraints.
     Graphify covers structure; do not hand-maintain file listings here. -->

## Context
A local research assistant for one user (Luis). You ask a question in plain English
("Which demographic groups in grade 7 have the lowest reading scores, and how does
attendance relate?"). It answers from synthetic student data and cites the rows or
notes it used. Everything runs on the local machine: no hosted services, and no data
leaves the box.

## Stack
| Layer | Choice | Why |
|---|---|---|
| Language / tooling | Python 3.12 + uv | The standard for AI work; uv handles fast, locked installs |
| Structured data | DuckDB (file) | Analytical SQL over tables in one local file; no server needed |
| Vector store | Chroma (persistent, local) | The simplest local vector DB, with metadata filters |
| Embeddings | sentence-transformers (e.g. `BAAI/bge-small-en-v1.5`) on CPU | Free and local; CPU is fast enough at this size |
| LLM | Ollama, 7–14B model (e.g. Qwen 2.5 / Qwen 2.5-Coder 14B for SQL) | Local and free; 16 GB VRAM fits 14B at Q4 |
| Tracing | Arize Phoenix (local) + OpenInference | Shows retrieved chunks, SQL, prompts, and latency per query |
| Interface | CLI (`student-rag`) + Jupyter notebooks | Notebooks teach each concept; the CLI is the end-to-end tool |
| Tests | pytest + golden eval set | Unit tests for risky logic; the eval measures RAG quality |
| Hosting | none | Local only in v1 |

Versions are pinned by `uv lock` at setup; the table below is filled then.

| Package | Version |
|---|---|
| (filled in at T-004) | |

## Components and boundaries
1. **Data generator** (`src/student_rag/data/`): a seeded script that builds the
   DuckDB tables and teacher-note text, with planted patterns. It is the only writer to
   the database.
2. **Indexer**: chunks the text documents (teacher notes, course descriptions, data
   dictionary), embeds them, and stores them in Chroma with metadata (student_id, grade,
   course).
3. **Router**: decides whether a question needs SQL (counts, averages, comparisons),
   vector search (qualitative notes), or both.
4. **Text-to-SQL**: the LLM writes SQL from the schema plus the data dictionary. A guard
   allows only a single SELECT, and the query runs on a `read_only=True` connection
   with a row limit. It must never write.
5. **Retriever**: top-k vector search, with metadata filters taken from the question.
6. **Answerer**: the LLM combines SQL results and retrieved chunks into an answer that
   cites its sources (the SQL plus chunk IDs).
7. **Eval**: golden Q&A set, scored for retrieval hit rate, answer accuracy, and
   whether each planted pattern was found.

The system answers aggregate research questions only. It produces no per-student
predictions or risk scores.

## Data model
Draft, to be finalized in the data-generator task. All data is synthetic.
- `students` (student_id, grade_level, gender, race_ethnicity, ell_status, iep_status,
  frl_status): demographics. This would be sensitive if the data were real.
- `courses` (course_id, name, subject, grade_level)
- `enrollments` (student_id, course_id, term, grade_pct, letter_grade)
- `attendance` (student_id, date, status)
- `discipline` (incident_id, student_id, date, category, action)
- `reading_assessments` (student_id, term, score, lexile, benchmark_level)
- `teacher_notes` (note_id, student_id, course_id, date, text), which is embedded into Chroma

Planted patterns (ground truth for the eval) are listed in the generator's docstring
and in `eval/`.

## External services and API contracts
| Service | Used for | Failure plan |
|---|---|---|
| Ollama (localhost:11434) | LLM generation | CLI shows a clear "start Ollama" error |
| Hugging Face (first run only) | Downloading the embedding model | Cached after the first download; works offline after |

## Non-functional targets
- Performance: p50 under 10 s per question on the RX 9070 XT
- Availability: not applicable (local)
- Scale: about 2k students, 20k grade rows, 100k attendance rows

## Constraints and known risks
- Ollama GPU support for AMD RX 9070 XT (RDNA4) on Windows must be verified (T-003). The
  fallbacks are the Vulkan backend or CPU, which are slower.
- Text-to-SQL accuracy from local models is the weakest link. A good data dictionary
  and few-shot examples matter more than model size.
- sentence-transformers pulls in PyTorch (CPU build, about 1 GB). Ollama's
  `nomic-embed-text` would avoid it if the install becomes a problem.
- Synthetic data can make results look cleaner than reality. Findings say nothing
  about real schools.
