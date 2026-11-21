# Plugin capability negotiation and schema compatibility

**Status:** proposed, not claimed. **Owner repository:** openMotor_Ivan.

## Bounded prompt
Discover solver version and supported geometry, settings, output channels and feature flags through versioned interface. Render unsupported features as explicit disabled/diagnostic UI, never silent fallback. Coordinate SRM #10/#14/#29 and M0-0E. Test old/new plugin and missing capabilities.

## Acceptance and safety
Audit current upstream/fork code and existing tasks first; extend rather than duplicate. Follow CLAIM_PROTOCOL.md and obtain a verified create-only exclusive claim before task-specific work. Scoped PR with runnable tests, failure cases, compatibility evidence, changelog and exact source references. No merge without approval; other repos read-only.
