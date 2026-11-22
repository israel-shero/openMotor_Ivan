# M0-0C — Versioned .ric interchange contract
**Suggested branch:** `milestone0/ric-contract`. **Dependency:** use completed M0-0B baselines before final contract approval; audit may start earlier.

## Instructions
1. Inspect current `.ric` reader/writer and migrations, property ownership, units, references, plugin settings, unknown keys and failure handling.
2. Compare with current `reilleya/openMotor` upstream; identify extension conflicts, backwards compatibility risks and existing related PRs.
3. Write an explicit versioned schema proposal with sample documents, compatibility matrix, migration behavior, unknown-field handling, solver config ownership and fallback rules. Label proposed fields as proposed, never as implemented.
4. Add tests for existing behavior only. Split implementation of new schema into a separate reviewed task rather than silently changing saved files.

## Acceptance
- Auditable contract, examples and compatibility matrix; clear compatibility/failure guarantees.
- No breaking writer changes, default changes or physics modifications.
- Results of M0-0B incorporated.

# Common execution rules
- Sole implementation destination: `israel-shero/openMotor_Ivan`. Never write to `israel-shero/openMotor-srm1d`; historical reference only.
- Check latest branches, open PRs, checkpoint, AGENTS.md, current code and tests first. Skip or narrow work already completed.
- Start from `integration/srm1d-packaging` only after verifying it remains the intended integration branch. Create the named task branch and target the integration branch for review; do not modify upstream-aligned `staging`.
- Keep commits scoped, avoid unrelated refactors, preserve existing solver defaults and numerical physics.
- Test existing and new behavior, document commands, results, limitations, regression checks and upstream compatibility. Maintain changelog or PR change summary.
- Do not merge without approval; report blockers and never invent validation evidence.
