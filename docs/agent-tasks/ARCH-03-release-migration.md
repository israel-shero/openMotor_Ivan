# Reproducible packaging, upgrade and release checklist

**Status:** proposed, not claimed. **Owner repository:** openMotor_Ivan.

## Bounded prompt
Inventory release workflow, pin dependencies, build cross-platform packages, verify old .ric/config/layout migration, reproducible smoke tests and changelog. Reuse M0-0D and QA-02, no duplicate CI framework. Include rollback and signing/permission review.

## Acceptance and safety
Audit current upstream/fork code and existing tasks first; extend rather than duplicate. Follow CLAIM_PROTOCOL.md and obtain a verified create-only exclusive claim before task-specific work. Scoped PR with runnable tests, failure cases, compatibility evidence, changelog and exact source references. No merge without approval; other repos read-only.
