# Graph Report - learning  (2026-11-13)

## Corpus Check
- 16 files · ~4,683 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 5 file(s) not represented in the graph (top: (none) 5)

## Summary
- 79 nodes · 67 edges · 13 communities (7 shown, 6 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3fcde79a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Architecture — learning
- Tasks — learning
- Brief — learning
- Runbook — learning
- 00 · Concept name
- learning
- pull_request_template.md
- Decisions — learning
- database.md
- security.md
- testing.md
- student-rag

## God Nodes (most connected - your core abstractions)
1. `Brief — learning` - 16 edges
2. `Runbook — learning` - 9 edges
3. `Architecture — learning` - 8 edges
4. `Tasks — learning` - 7 edges
5. `learning` - 6 edges
6. `00 · Concept name` - 6 edges
7. `Decisions — learning` - 2 edges
8. `Database rules` - 1 edges
9. `Security rules` - 1 edges
10. `Testing rules` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (13 total, 6 thin omitted)

### Community 0 - "Architecture — learning"
Cohesion: 0.22
Nodes (8): Architecture — learning, Components and boundaries, Constraints and known risks, Context, Data model, External services and API contracts, Non-functional targets, Stack

### Community 1 - "Tasks — learning"
Cohesion: 0.20
Nodes (8): Blocked or waiting on a human, Debt (from `/ponytail-debt`), Done, Next, Now, Open decisions from intake, Tasks — learning, student-rag

### Community 2 - "Brief — learning"
Cohesion: 0.12
Nodes (16): 10. Database, 11. CI/CD, environments, rollback, 12. Performance, accessibility, SEO, 13. Privacy and compliance, 14. Cost and context budget, 15. Definition of done and release criteria, 1. Identity and scope, 2. Architecture specifications (+8 more)

### Community 3 - "Runbook — learning"
Cohesion: 0.20
Nodes (9): Database, Deploy, Environments, Incidents, Monitoring, Rollback, Runbook — learning, Secrets (+1 more)

### Community 4 - "00 · Concept name"
Cohesion: 0.22
Nodes (7): Learning log, 00 · Concept name, Check yourself, How it works, In this project, Key terms, Links

### Community 5 - "learning"
Cohesion: 0.29
Nodes (6): Approval gates for this project, Commands, graphify, learning, Rules for this project, Where things are

### Community 6 - "pull_request_template.md"
Cohesion: 0.40
Nodes (4): Checklist, How to check it, Risks and follow-ups, What and why

## Knowledge Gaps
- **1 isolated node(s):** `student-rag`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 67 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `student-rag` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Brief — learning` be split into smaller, more focused modules?**
  _Cohesion score 0.11764705882352941 - nodes in this community are weakly interconnected._