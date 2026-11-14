# Tasks — learning

Stage: building · Updated: 2026-11-13 · Milestone: v1 by about 2026-12-13

<!-- IDs never get reused. "Now" holds at most 3 tasks. When a task changes state,
     update the registry row in the workspace CLAUDE.md in the same turn.
     Luis writes the code for every task; Claude teaches, writes the note, and reviews. -->

## Now
- [ ] T-002 Create the GitHub repo, push the scaffold, and add an MIT LICENSE

## Next
Setup
- [ ] T-003 Install Ollama; check GPU acceleration on the RX 9070 XT (ROCm or Vulkan); pull a 7B and a 14B model and time them
- [ ] T-004 `uv init` the package (`src/student_rag/`), add deps (needs approval), pin versions in ARCHITECTURE.md
- [ ] T-005 CI: GitHub Actions running ruff, pytest, and gitleaks; Dependabot weekly; check that no co-author trailers are added

Milestone 1 — data (week 1)
- [ ] T-006 Seeded synthetic data generator into DuckDB, with planted patterns, plus tests · note: `docs/learning/01-synthetic-data.md`
- [ ] T-007 Data dictionary (table and column meanings), used by text-to-SQL · note: `02-schema-as-context.md`

Milestone 2 — vector RAG (week 2)
- [ ] T-008 Chunk and embed the teacher notes into Chroma, with metadata · note: `03-chunking-and-embeddings.md`
- [ ] T-009 Retrieval plus a grounded answer with citations via Ollama; Phoenix tracing on · note: `04-retrieval-and-grounding.md`

Milestone 3 — text-to-SQL and hybrid (week 3)
- [ ] T-010 Text-to-SQL with a read-only connection and a SELECT-only guard, plus tests · note: `05-text-to-sql.md`
- [ ] T-011 Router: SQL, vector, or both; CLI `student-rag ask` · note: `06-hybrid-routing.md`

Milestone 4 — eval (week 4)
- [ ] T-012 Golden eval set (30+ questions) and scorer (hit rate, accuracy, patterns found) · note: `07-evaluating-rag.md`
- [ ] T-013 Tune (chunk size, top-k, prompts, model) against the eval; write up the results
- [ ] T-014 Build the code graph after the first feature lands (`/graphify .`)

## Blocked or waiting on a human

## Open decisions from intake
- Public dataset to add after v1 (UCI Student Performance, NCES, state report cards)
- Push/merge autonomy was not answered directly; defaulted to Luis commits, opens PRs, and merges
- Coverage rule defaulted to "all risky logic" (the SQL guard and the data generator)
- Git workflow details (branch naming, 400-line PRs) were defaults
- Changelog from v1 was a default

## Debt (from `/ponytail-debt`)

## Done
<!-- Keep the last 10. Move older lines to docs/archive/TASKS-<year>.md. -->
- [x] T-001 Luis approved the brief, architecture, and D-001 (2026-11-13)
