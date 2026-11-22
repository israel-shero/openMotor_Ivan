# Command palette, presets and workspace recovery

**Status:** proposed; not claimed. **Repository:** openMotor_Ivan only.

## Bounded implementation prompt
Command search, discoverable shortcuts, recently used configs, saved layouts, autosave and crash recovery, plot and solver presets, reset to default. Preserve existing upstream capabilities, ensure migration, undo semantics and recovery from corrupted autosave. Test keyboard-only workflows, high DPI and cross-platform persistence.

## Execution and acceptance
- First inspect current upstream/fork functionality and related PRs; avoid duplicates and preserve existing UI behavior.
- Before task-specific work, read `docs/agent-tasks/CLAIM_PROTOCOL.md` and acquire a verified **create-only** exclusive claim; do not trust create-or-update branch operations.
- Work in a scoped branch; document dependencies, test fixtures, user-visible acceptance, keyboard accessibility, failure cases, migration behavior and reproducible test commands.
- SRM 1D owns solver/statistics; integrate only via versioned adapter interfaces and pinned fixtures.
- Submit reviewable PR with changelog and evidence. No merge without approval.
