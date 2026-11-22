# UI regression, accessibility and performance acceptance

**Status:** proposed; not claimed. **Repository:** openMotor_Ivan only.

## Bounded implementation prompt
Establish automated Qt/headless tests, resize/high-DPI, themes, keyboard traversal, focus order, screen-reader labels where supported, large plot datasets, cancellation and recovery, localization-ready strings and platform matrix. Establish measurable baseline rather than arbitrary targets; coordinate M0-0D.

## Execution and acceptance
- First inspect current upstream/fork functionality and related PRs; avoid duplicates and preserve existing UI behavior.
- Before task-specific work, read `docs/agent-tasks/CLAIM_PROTOCOL.md` and acquire a verified **create-only** exclusive claim; do not trust create-or-update branch operations.
- Work in a scoped branch; document dependencies, test fixtures, user-visible acceptance, keyboard accessibility, failure cases, migration behavior and reproducible test commands.
- SRM 1D owns solver/statistics; integrate only via versioned adapter interfaces and pinned fixtures.
- Submit reviewable PR with changelog and evidence. No merge without approval.
