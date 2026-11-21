# Interactive axial geometry editor

**Status:** proposed; not claimed. **Repository:** openMotor_Ivan only.

## Bounded implementation prompt
Visual axial station editor, dimensions and constraints, previews, cross-sections and topology boundaries. Reuse solver geometry contract from SRM #3 and existing grain preview; never imply unsupported end-burning or geometry is supported. Ensure keyboard alternative, undo/redo, invalid input warnings and exact serialized geometry roundtrip.

## Execution and acceptance
- First inspect current upstream/fork functionality and related PRs; avoid duplicates and preserve existing UI behavior.
- Before task-specific work, read `docs/agent-tasks/CLAIM_PROTOCOL.md` and acquire a verified **create-only** exclusive claim; do not trust create-or-update branch operations.
- Work in a scoped branch; document dependencies, test fixtures, user-visible acceptance, keyboard accessibility, failure cases, migration behavior and reproducible test commands.
- SRM 1D owns solver/statistics; integrate only via versioned adapter interfaces and pinned fixtures.
- Submit reviewable PR with changelog and evidence. No merge without approval.
