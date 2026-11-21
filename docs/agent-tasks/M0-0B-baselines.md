# M0-0B — .ric, solver config and quasi-steady regression baselines
**Suggested branch:** `milestone0/ric-qs-baselines`. **Priority:** first. **Dependencies:** none.

## Instructions
1. Audit `uilib/fileIO.py`, `motorlib/motor.py`, `motorlib/properties.py`, `motorlib/solvers.py`, preferences/simulation managers, current tests and fixtures. Do not assume paths remain unchanged.
2. Characterize existing historical `.ric` migrations, malformed/missing/future versions, grain ordering, optional fields and round-trip behavior using small fixtures. Separate observed from desired behavior.
3. Test solver selection/precedence across motor override, global preference, defaults, stale/unknown IDs and reload. Confirm actual precedence from code rather than assuming it.
4. Commit deterministic quasi-steady reference fixtures for supported BATES, noncircular/FMM and tapered geometry (skip unsupported variants explicitly). Record time, pressure, thrust, impulse, burn duration, warnings, units, versions, generating commit and justified tolerances. Tests must never silently regenerate golden data.
5. Register tests in existing test runner and document reproducibility, source provenance and limitations. Do not change production physics, serialization or defaults.

## Acceptance
- Existing unit suite and new characterization tests pass, or failures are accurately reported.
- Three supported reference cases with provenance, documented precision and no automatic fixture rewrite.
- Migration and config-precedence behavior covered; no false experimental validation claim.
- Diff, upstream alignment and changelog reviewed.

# Common execution rules
- Sole implementation destination: `israel-shero/openMotor_Ivan`. Never write to `israel-shero/openMotor-srm1d`; historical reference only.
- Check latest branches, open PRs, checkpoint, AGENTS.md, current code and tests first. Skip or narrow work already completed.
- Start from `integration/srm1d-packaging` only after verifying it remains the intended integration branch. Create the named task branch and target the integration branch for review; do not modify upstream-aligned `staging`.
- Keep commits scoped, avoid unrelated refactors, preserve existing solver defaults and numerical physics.
- Test existing and new behavior, document commands, results, limitations, regression checks and upstream compatibility. Maintain changelog or PR change summary.
- Do not merge without approval; report blockers and never invent validation evidence.
