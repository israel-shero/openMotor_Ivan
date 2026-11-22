# Performance regression benchmarks

**Status:** proposed, not claimed. **Repository:** `israel-shero/openMotor_Ivan` only.

## Scope and implementation prompt
Build reproducible GUI startup, plotting large histories, .ric load/save, plugin run and memory benchmarks; separate Qt startup from solver runtime and warm caches. Pin environments and input fixtures, use repeated runs and noise-aware thresholds. Avoid false regressions from CI variability. Deliver baseline artifacts and an opt-in comparison job.

## Execution gates
1. Read `docs/agent-tasks/CLAIM_PROTOCOL.md`; acquire a verified create-only exclusive claim **before** task-specific work. If unavailable, stop and select another task.
2. Check latest code, open PRs, dependencies and prior implementations; avoid duplicates.
3. Announce owner/run ID, task, branch, base SHA and acceptance gates. Work on scoped branch; preserve existing defaults and compatibility.
4. Include tests, failure injection, reproducible commands, versioned evidence, change summary and cross-repo references. No merge without approval.

**Acceptance:** bounded reviewed PR, executable tests and documented limitations. A prompt alone is not implementation.
