# Cross-repository contract CI

**Status:** proposed, not claimed. **Repository:** `israel-shero/openMotor_Ivan` only.

## Scope and implementation prompt
Coordinate with SRM 1D #14 and #10. Build pinned fixture matrix for legacy .ric, config precedence, geometry family compatibility, FMM, units, result channels, unknown fields and explicit unsupported cases. Test against pinned SRM 1D SHA and report compatibility; do not silently change solver defaults. PR A fixture inventory, PR B CI matrix. Fail visibly on mismatch and document pin update procedure.

## Execution gates
1. Read `docs/agent-tasks/CLAIM_PROTOCOL.md`; acquire a verified create-only exclusive claim **before** task-specific work. If unavailable, stop and select another task.
2. Check latest code, open PRs, dependencies and prior implementations; avoid duplicates.
3. Announce owner/run ID, task, branch, base SHA and acceptance gates. Work on scoped branch; preserve existing defaults and compatibility.
4. Include tests, failure injection, reproducible commands, versioned evidence, change summary and cross-repo references. No merge without approval.

**Acceptance:** bounded reviewed PR, executable tests and documented limitations. A prompt alone is not implementation.
