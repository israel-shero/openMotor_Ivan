# Atomic claims and lease recovery

**Status:** proposed, not claimed. **Repository:** `israel-shero/openMotor_Ivan` only.

## Scope and implementation prompt
Design and implement a create-only, fail-closed claim client for openMotor task IDs. Coordinate protocol with SRM 1D #12; same semantics, separate namespace/repo. Never treat GitHub create-or-update branch as atomic. Include owner/run ID, nonce, fencing token, lease/heartbeat, verified release and conflict reconciliation. Tests: two concurrent contenders exactly one winner, timeout, stale owner, crash recovery, duplicate selection and unauthorized release. Deliver CLI and CI test report in scoped PR.

## Execution gates
1. Read `docs/agent-tasks/CLAIM_PROTOCOL.md`; acquire a verified create-only exclusive claim **before** task-specific work. If unavailable, stop and select another task.
2. Check latest code, open PRs, dependencies and prior implementations; avoid duplicates.
3. Announce owner/run ID, task, branch, base SHA and acceptance gates. Work on scoped branch; preserve existing defaults and compatibility.
4. Include tests, failure injection, reproducible commands, versioned evidence, change summary and cross-repo references. No merge without approval.

**Acceptance:** bounded reviewed PR, executable tests and documented limitations. A prompt alone is not implementation.
