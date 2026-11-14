# Runbook — learning

## Environments
| Name | URL | Branch | Who can deploy |
|---|---|---|---|
| local | localhost (Ollama :11434, Phoenix :6006) | any | n/a |

No staging or production environments in v1.

## Deploy
Not applicable. Runs locally.

## Rollback
Not applicable. To undo, check out the previous commit and regenerate the data.

## Monitoring
- Errors: Python `logging` to the console
- Tracing: Arize Phoenix at http://localhost:6006. Start it before running the CLI or
  notebooks; traces are kept locally (git-ignored).
- Uptime and alerts: not applicable

## Database
- Rebuild from scratch: run the data generator (command filled in at T-006). It's
  seeded, so the output is identical every run.
- Rebuild vectors: run the indexer (command filled in at T-008)
- Migrations: none; change the generator and rebuild
- Backups: none needed (regenerable)

## Secrets
None expected. If one appears, put it in `.env` (git-ignored) and record a D-entry.

## Incidents
<!-- Newest first: date, what broke, cause, fix, follow-up task ID. -->

## v1 readiness checklist
- [ ] Tests pass in CI on the release commit
- [ ] `/ponytail-audit` run, findings fixed or logged as tasks
- [ ] 30+ golden questions; retrieval hit rate ≥ 80%; answer accuracy ≥ 70%
- [ ] Every planted pattern found by the system
- [ ] p50 latency under 10 s
- [ ] gitleaks and the dependency scan are clean; no data files committed
- [ ] Results write-up in `docs/learning/`
- [ ] Luis signed off
