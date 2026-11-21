# Independent verification and review

**Status:** proposed, not claimed. **Repository:** `israel-shero/openMotor_Ivan` only.

## Scope and implementation prompt
Implement reviewer/verifier evidence checklist and reproducible CI report independent of implementer self-report. Cover GUI headless tests, serialization regression, plugin discovery/cancellation, compatibility, numerical baseline provenance, failure injection and changes to defaults. Document branch protection requirements but do not claim they are configured. PR A report schema and verification workflow.

## Execution gates
1. Read `docs/agent-tasks/CLAIM_PROTOCOL.md`; acquire a verified create-only exclusive claim **before** task-specific work. If unavailable, stop and select another task.
2. Check latest code, open PRs, dependencies and prior implementations; avoid duplicates.
3. Announce owner/run ID, task, branch, base SHA and acceptance gates. Work on scoped branch; preserve existing defaults and compatibility.
4. Include tests, failure injection, reproducible commands, versioned evidence, change summary and cross-repo references. No merge without approval.

**Acceptance:** bounded reviewed PR, executable tests and documented limitations. A prompt alone is not implementation.
