# Reproducible simulation report and comparison export

**Status:** proposed; not claimed. **Repository:** openMotor_Ivan only.

## Bounded implementation prompt
Export configuration and solver version/commit, units, plots, numerical settings, warnings, input evidence, comparison metrics, uncertainty methodology and failed samples. Offer machine-readable manifest alongside human-readable report; no ungrounded accuracy/validation claims.

## Execution and acceptance
- First inspect current upstream/fork functionality and related PRs; avoid duplicates and preserve existing UI behavior.
- Before task-specific work, read `docs/agent-tasks/CLAIM_PROTOCOL.md` and acquire a verified **create-only** exclusive claim; do not trust create-or-update branch operations.
- Work in a scoped branch; document dependencies, test fixtures, user-visible acceptance, keyboard accessibility, failure cases, migration behavior and reproducible test commands.
- SRM 1D owns solver/statistics; integrate only via versioned adapter interfaces and pinned fixtures.
- Submit reviewable PR with changelog and evidence. No merge without approval.
