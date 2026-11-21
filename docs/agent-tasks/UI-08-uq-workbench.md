# Uncertainty, sensitivity and identification workbench

**Status:** proposed; not claimed. **Repository:** openMotor_Ivan only.

## Bounded implementation prompt
UI integration for SRM UQ issues #18-23: parameter distribution editor, correlation validation, batch progress, failed-sample diagnostics, sensitivity ranks, confidence/credible interval labeling, identifiability flags, calibration/holdout distinction, per-sample inspection and export. Build on versioned SRM contract; UI must not implement a second statistical engine.

## Execution and acceptance
- First inspect current upstream/fork functionality and related PRs; avoid duplicates and preserve existing UI behavior.
- Before task-specific work, read `docs/agent-tasks/CLAIM_PROTOCOL.md` and acquire a verified **create-only** exclusive claim; do not trust create-or-update branch operations.
- Work in a scoped branch; document dependencies, test fixtures, user-visible acceptance, keyboard accessibility, failure cases, migration behavior and reproducible test commands.
- SRM 1D owns solver/statistics; integrate only via versioned adapter interfaces and pinned fixtures.
- Submit reviewable PR with changelog and evidence. No merge without approval.
