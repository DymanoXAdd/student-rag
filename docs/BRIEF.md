# Brief — learning

Created 2026-11-13 by `/new-project`. This is the record of the intake answers.
Anything marked **default** or **open** was not answered and has a matching task in `TASKS.md`.

## 1. Identity and scope
- Goal: Learn RAG and related AI subjects in depth, on the way to becoming an AI engineer,
  by building a RAG system of my own over student data. Then test whether it has a real
  use: improving student performance, reading metrics, or insight into student demographics.
- Users: Luis (the learner and builder)
- Type: CLI/library + Jupyter notebooks first; a UI may come later
- Core job: ask questions about student data (grades, courses, attendance, discipline,
  other factors) and get grounded answers that show where students struggle and
  which demographics are affected. A research assistant, not a decision maker.
- Data: synthetic or public data first. Real data only after privacy controls exist.
- Success looks like: a working RAG system that answers grounded, cited questions over
  the student data, measured against a small eval set
- Out of scope for v1: real student data, web UI, deployment/hosting, predictions or
  risk scores about individual students (aggregate research questions only)
- Deadline or milestones: first working RAG + eval within 1 month (by about 2026-12-13)
- Starting point: new build
- Intake depth: full

## 2. Architecture specifications
- Approach: hybrid RAG. Text-to-SQL over the structured tables (grades, courses,
  attendance, discipline, demographics), plus vector retrieval over the text (notes,
  reading passages, docs). Claude proposes the stack in D-001 for approval.
- Stack (proposed): Python + uv, DuckDB (tables), Chroma (vectors), Jupyter notebooks,
  a small CLI
- LLM: local via Ollama
- Embeddings: local sentence-transformers
- External services: none. Fully local, so no data leaves the machine.
- Hosting: none (runs locally)
- Hardware: Ryzen 7 9800X3D, 32 GB RAM, AMD Radeon RX 9070 XT 16 GB. Targets 7–14B
  quantized models. Ollama GPU support for AMD on Windows (ROCm, RDNA4) must be checked.
- Scale: one user, synthetic data of thousands to tens of thousands of rows
- Existing architecture doc: none

## 3. Current documentation
- Existing docs: none, start fresh (**default**)
- Keep current: README, `docs/`, and a learning log in `docs/learning/` (one note per
  concept: chunking, embeddings, retrieval, text-to-SQL, eval), linked from each notebook
- Versions: pin the latest at setup with `uv lock`; record them in ARCHITECTURE.md
- Changelog: from v1 (**default**)

## 4. Design
- Not applicable for v1 (no UI). Notebook charts use matplotlib defaults.
## 5. Human approval gates
- **Learning rule:** Luis types the Python code himself. Claude helps by explaining,
  writing the context notes (what the code does and how it works), giving hints and
  small snippets when asked, and reviewing what Luis wrote. Claude does not write
  application code unless Luis asks for it explicitly.
- Plan first: before every new concept or milestone (chunking, retrieval, text-to-SQL,
  eval), Claude explains the approach and the why before any code is written.
- Gates: new dependency, any paid service, any secret, anything touching real student
  data, starting a new milestone. Push and merge follow Luis's usual autonomy, with
  Claude allowed to commit docs and notes (**default**, not answered directly).
- Approver: Luis

## 6. Automated tests
- Levels: pytest unit tests (data generator, SQL safety guard, chunking, retrieval
  helpers) plus a golden Q&A eval set (retrieval hit rate, answer accuracy, citation
  correctness)
- Runs: pytest on every PR in GitHub Actions; the eval runs locally (it needs Ollama)
- Coverage: all risky logic, meaning the SQL guard and the data generator (**default**)
- Test data: seeded synthetic generator with a fixed seed, so runs are repeatable
- Luis writes the tests too; Claude explains what to test and why
## 7. Error monitoring and observability
- Error tracking, alerts, uptime: not applicable (local, single user)
- Tracing: Arize Phoenix running locally (OpenTelemetry/OpenInference) records each
  query's retrieved chunks, generated SQL, prompt, answer, and latency
- Logging: Python `logging`; never log real student records (synthetic data only in v1)

## 8. Security and secrets
- Auth and roles: not applicable (local, single user)
- Sensitive data: none in v1 (synthetic). Real student data would be FERPA-covered,
  is out of scope, and would need a new decision before use.
- Text-to-SQL guard: DuckDB opened `read_only=True`, plus rejection of anything that
  is not a single SELECT statement
- Secrets: none expected (fully local). Any future one goes in `.env`, which is git-ignored.
- Scanning: gitleaks and Dependabot in CI. Dependabot PRs must not add co-author trailers,
  and no Claude or Dependabot attribution goes into commits or merges.
- Data files (`*.duckdb`, `data/raw/`, Chroma dir, Phoenix traces) are git-ignored
## 9. Pull requests and git workflow
- GitHub, trunk-based, branches `task/T-###-short-name`, Conventional Commits,
  about 400 changed lines per PR, one task per PR (**default**)
- Luis commits his code and opens PRs. Claude reviews the diff (`/ponytail-review`)
  and explains the findings. Luis merges.
- Required checks: ruff lint, pytest, gitleaks
- No Claude or Dependabot co-author or attribution trailers

## 10. Database
- Engine: DuckDB, a local file at `data/students.duckdb` (git-ignored); Chroma
  persistent dir for vectors
- Migrations: none. The schema is rebuilt from the seeded generator script.
- Entities (draft): students (with demographics), courses, enrollments/grades,
  attendance, discipline incidents, reading assessments, teacher notes (text, for vectors)
- Size: about 2k students at one school, roughly 20k grade rows and 100k attendance rows
- Planted patterns: known correlations (for example chronic absence and lower reading
  scores in one grade) give the eval ground truth
- Public dataset: later (open decision)
- Backups: not needed. Data is regenerable from seed.
## 11. CI/CD, environments, rollback
- Environments: local only; no deploy, so no rollback is needed
- CI: GitHub Actions on every PR runs ruff, pytest, and gitleaks. Dependabot runs weekly.
- Eval runs locally (`uv run python -m eval`), not in CI

## 12. Performance, accessibility, SEO
- Latency: under 10 s per question on the RX 9070 XT
- Accessibility and SEO: not applicable (no UI)

## 13. Privacy and compliance
- Synthetic data only in v1. Real student data is FERPA-covered and needs a new
  decision, de-identification, and local-only processing before use.
- License: MIT

## 14. Cost and context budget
- Ponytail: `lite`
- Graphify: soft nudges, code and docs
- Budget: $0/month (fully local). Any paid service needs approval.
- MCP servers: none

## 15. Definition of done and release criteria
- Task done: tests pass, ruff is clean, Claude has reviewed it, the learning note in
  `docs/learning/` is written, Luis can explain how it works in his own words, and
  `docs/TASKS.md` plus the registry are updated
- v1 done: 30+ golden eval questions, at least 80% retrieval hit rate, at least 70%
  correct answers, every planted pattern found, a results write-up, and p50 latency
  under 10 s
- Owner after v1: Luis; next steps are a public dataset, a UI, or real-data planning
