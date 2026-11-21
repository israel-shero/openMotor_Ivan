# Reference drawing and geometry evidence review workflow

**Status:** proposed, not claimed. **Owner repository:** openMotor_Ivan.

## Bounded prompt
Design UI to inspect drawing metadata, dimension evidence, explicit/inferred/unknown fields and uncertainty flags before importing reference .ric geometry. Coordinate SRM #27/#28 and M0-0C. Do not silently invent missing motor data.

## Acceptance and safety
Audit current upstream/fork code and existing tasks first; extend rather than duplicate. Follow CLAIM_PROTOCOL.md and obtain a verified create-only exclusive claim before task-specific work. Scoped PR with runnable tests, failure cases, compatibility evidence, changelog and exact source references. No merge without approval; other repos read-only.
