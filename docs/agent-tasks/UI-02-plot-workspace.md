# Plotting and run-comparison workspace

**Status:** proposed; not claimed. **Repository:** openMotor_Ivan only.

## Bounded implementation prompt
Extend M0-0F rather than duplicate. Independent left/right y-axis ranges and units; multiple run/CSV overlays, synchronized cursors, zoom/pan, aligned times, difference/residual plots, plot presets, annotations, export and config diff. Tests: axis independence, invalid units, NaN/gaps, large datasets, persisted settings and accessibility.

## Execution and acceptance
- First inspect current upstream/fork functionality and related PRs; avoid duplicates and preserve existing UI behavior.
- Before task-specific work, read `docs/agent-tasks/CLAIM_PROTOCOL.md` and acquire a verified **create-only** exclusive claim; do not trust create-or-update branch operations.
- Work in a scoped branch; document dependencies, test fixtures, user-visible acceptance, keyboard accessibility, failure cases, migration behavior and reproducible test commands.
- SRM 1D owns solver/statistics; integrate only via versioned adapter interfaces and pinned fixtures.
- Submit reviewable PR with changelog and evidence. No merge without approval.
