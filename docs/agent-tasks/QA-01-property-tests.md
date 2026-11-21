# Property-based GUI and serialization tests

**Status:** proposed, not claimed. **Repository:** `israel-shero/openMotor_Ivan` only.

## Scope and implementation prompt
Use bounded property-based generators for valid/invalid motor configurations, serialization fields and plotting arrays. Assert round-trip semantic equivalence, deterministic error behavior, dimensional units, monotone timestamps, independent left/right axis scale behavior, and cancellation invariants. Preserve minimized failure fixtures. Coordinate with M0-0F and QA-02.

## Execution gates
1. Read `docs/agent-tasks/CLAIM_PROTOCOL.md`; acquire a verified create-only exclusive claim **before** task-specific work. If unavailable, stop and select another task.
2. Check latest code, open PRs, dependencies and prior implementations; avoid duplicates.
3. Announce owner/run ID, task, branch, base SHA and acceptance gates. Work on scoped branch; preserve existing defaults and compatibility.
4. Include tests, failure injection, reproducible commands, versioned evidence, change summary and cross-repo references. No merge without approval.

**Acceptance:** bounded reviewed PR, executable tests and documented limitations. A prompt alone is not implementation.
