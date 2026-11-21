# Golden-file compatibility and migration corpus

**Status:** proposed, not claimed. **Repository:** `israel-shero/openMotor_Ivan` only.

## Scope and implementation prompt
Assemble versioned, legally distributable .ric fixtures spanning supported grain families, old/unknown fields, malformed inputs, optional solver config and legacy upstream behavior. Verify load/save/load semantics and no silent data loss; document when byte-for-byte equality is not appropriate. Add fixtures to CI and tests for expected failures. Coordinate with M0-0B/M0-0C.

## Execution gates
1. Read `docs/agent-tasks/CLAIM_PROTOCOL.md`; acquire a verified create-only exclusive claim **before** task-specific work. If unavailable, stop and select another task.
2. Check latest code, open PRs, dependencies and prior implementations; avoid duplicates.
3. Announce owner/run ID, task, branch, base SHA and acceptance gates. Work on scoped branch; preserve existing defaults and compatibility.
4. Include tests, failure injection, reproducible commands, versioned evidence, change summary and cross-repo references. No merge without approval.

**Acceptance:** bounded reviewed PR, executable tests and documented limitations. A prompt alone is not implementation.
