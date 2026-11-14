# learning

Learn RAG end to end by building a local hybrid RAG research assistant over synthetic
student data (grades, courses, attendance, discipline, demographics, reading scores).
It should answer grounded, cited questions about where students struggle and which
groups are affected.

- Type: Python library + CLI + Jupyter notebooks · Stage: building · Ponytail level: lite
- Stack: Python + uv, DuckDB, Chroma, sentence-transformers, Ollama (local LLM), Arize Phoenix (tracing)

## Commands

- Install: `uv sync`
- Dev: `uv run jupyter lab` · CLI: `uv run student-rag ask "<question>"`
- Test: `uv run pytest`
- Lint / typecheck: `uv run ruff check .`
- Eval (local only, needs Ollama): `uv run python -m eval`

## Where things are

- Tasks and status: `docs/TASKS.md` (read first)
- Intake answers and scope: `docs/BRIEF.md`
- Architecture and data model: `docs/ARCHITECTURE.md`
- Decisions and their reasons: `docs/DECISIONS.md`
- Running locally, tracing, data regeneration: `docs/RUNBOOK.md`
- Concept notes: `docs/learning/` (one note per concept)
- Code map: `graphify-out/GRAPH_REPORT.md` (query with `graphify query`)

## Rules for this project

- **Luis types the Python code.** Claude explains, writes the context notes, gives
  hints or short snippets when asked, and reviews. Claude does not write application
  or test code unless Luis explicitly asks for it in that turn.
- **Teach before code.** Before each new concept or milestone, explain the approach,
  why it works, and the trade-offs. Then write or update its note in `docs/learning/`
  (what it does, how it works, the key terms, and what to watch for).
- **Notes are read in Obsidian.** Follow `docs/learning/_template.md`: YAML
  frontmatter (tags, task, status), `[[wikilinks]]` between notes, callouts
  (`> [!tip]`, `> [!warning]`, `> [!question]-`), short sections, and Mermaid diagrams
  for flows. Use no HTML and no relative markdown links between notes.
- Synthetic data only. Real student data is out of scope and needs a new D-entry.
- LLM-generated SQL runs only on a DuckDB connection opened `read_only=True`, after a
  check that rejects anything other than a single SELECT.
- Branch per task: `task/T-###-short-name`. Conventional Commits. One task per PR,
  under about 400 changed lines. Luis commits, opens PRs, and merges; Claude reviews with `/ponytail-review`.
- No Claude or Dependabot co-author or attribution trailers in commits or merges.
- A task is done when: tests pass, ruff is clean, Claude has reviewed it, the learning
  note is written, Luis can explain it in his own words, and `docs/TASKS.md` plus the
  registry are updated.

## Approval gates for this project

Ask for an explicit yes before: starting a new milestone, adding a dependency,
any paid service, any secret, anything that touches real student data, pushing or
merging, and changing anything in `docs/DECISIONS.md`.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- When graphify-out/graph.json exists, run `graphify query "<question>"` before your first grep, search or source-file read for a codebase question, and put this rule in every subagent prompt that explores code. Read raw files only for lines the graph or an earlier read already located. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
- A committed graphify-out/graph.json is rewritten whole on every build, so a large diff to it in a pull request is expected. Do not flag it as churn or suggest skipping the graph rebuild or its hooks.
