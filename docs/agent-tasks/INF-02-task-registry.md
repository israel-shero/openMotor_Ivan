# Machine-readable task registry and scheduler

**Status:** proposed, not claimed. **Repository:** `israel-shero/openMotor_Ivan` only.

## Scope and implementation prompt
Create versioned schema for task ID, repo, source Markdown path, dependencies, priority, risk, file conflict set, readiness, required checks and claimed status. Keep Markdown tasks as source until GitHub Issues enabled; registry is derived/indexed and cannot overwrite live claim state. Validate cycles and cross-repo dependencies. Dry-run scheduler first; claim via INF-01 before any task-specific audit or execution. Tests: stale registry, blocked dependencies, concurrent selection, task already in PR.

## Execution gates
1. Read `docs/agent-tasks/CLAIM_PROTOCOL.md`; acquire a verified create-only exclusive claim **before** task-specific work. If unavailable, stop and select another task.
2. Check latest code, open PRs, dependencies and prior implementations; avoid duplicates.
3. Announce owner/run ID, task, branch, base SHA and acceptance gates. Work on scoped branch; preserve existing defaults and compatibility.
4. Include tests, failure injection, reproducible commands, versioned evidence, change summary and cross-repo references. No merge without approval.

**Acceptance:** bounded reviewed PR, executable tests and documented limitations. A prompt alone is not implementation.
