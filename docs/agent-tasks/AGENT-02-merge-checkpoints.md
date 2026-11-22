# Cross-repository merge queue and resumable agent checkpoints

**Status:** proposed, not claimed. **Owner repository:** openMotor_Ivan.

## Bounded prompt
Implement GUI-repo-specific change conflict preflight, checkpoint handoff, safe resumption, and integration test ordering. Coordinate SRM #30 and INF-01/02/04. Do not auto-merge or delete refs; protect integration branch.

## Acceptance and safety
Audit current upstream/fork code and existing tasks first; extend rather than duplicate. Follow CLAIM_PROTOCOL.md and obtain a verified create-only exclusive claim before task-specific work. Scoped PR with runnable tests, failure cases, compatibility evidence, changelog and exact source references. No merge without approval; other repos read-only.
