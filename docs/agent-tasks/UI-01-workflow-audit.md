# Existing UI inventory and workflow audit

**Status:** proposed; not claimed. **Repository:** openMotor_Ivan only.

## Bounded implementation prompt
Inventory existing upstream and fork functionality first: Qt widgets, plotting, geometry preview, shortcuts, undo/redo, dark mode, scaling, units, serialization, configuration, plugins. Document user journeys and repetitive steps, supported/partial/missing features, screenshots and baseline timings. Do not duplicate upstream features. Produce prioritized UX backlog and acceptance criteria.

## Execution and acceptance
- First inspect current upstream/fork functionality and related PRs; avoid duplicates and preserve existing UI behavior.
- Before task-specific work, read `docs/agent-tasks/CLAIM_PROTOCOL.md` and acquire a verified **create-only** exclusive claim; do not trust create-or-update branch operations.
- Work in a scoped branch; document dependencies, test fixtures, user-visible acceptance, keyboard accessibility, failure cases, migration behavior and reproducible test commands.
- SRM 1D owns solver/statistics; integrate only via versioned adapter interfaces and pinned fixtures.
- Submit reviewable PR with changelog and evidence. No merge without approval.
