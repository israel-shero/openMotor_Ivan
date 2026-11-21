# Configuration inspector and efficient editing

**Status:** proposed; not claimed. **Repository:** openMotor_Ivan only.

## Bounded implementation prompt
Searchable grouped property inspector with advanced-setting disclosure, inline unit conversion and validation, default reset, contextual documentation, multi-select edits, duplicate/copy-paste grains, undo/redo preservation and keyboard navigation. Start with UX inventory, small scoped PR, no silent unit conversions or destructive edits.

## Execution and acceptance
- First inspect current upstream/fork functionality and related PRs; avoid duplicates and preserve existing UI behavior.
- Before task-specific work, read `docs/agent-tasks/CLAIM_PROTOCOL.md` and acquire a verified **create-only** exclusive claim; do not trust create-or-update branch operations.
- Work in a scoped branch; document dependencies, test fixtures, user-visible acceptance, keyboard accessibility, failure cases, migration behavior and reproducible test commands.
- SRM 1D owns solver/statistics; integrate only via versioned adapter interfaces and pinned fixtures.
- Submit reviewable PR with changelog and evidence. No merge without approval.
