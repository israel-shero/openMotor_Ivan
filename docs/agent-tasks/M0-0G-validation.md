# M0-0G — Evidence eligibility and remaining verification gates
**Suggested branch:** `milestone0/validation-evidence`. **Dependencies:** none for audit. **Parallel:** documentation-only.

## Instructions
1. Verify checkpoint assertions against evidence actually present in openMotor_Ivan; companion repositories are historical/read-only reference and their artifacts may not be present.
2. Record completed source reconciliation, common-state and coupled closure comparisons separately from incomplete full-burn convergence, case quality reviews, fit/holdout assignment and experimental validation.
3. Create a traceability matrix for each available case: source, time anchor, calibration, eligibility, numerical screen, known uncertainties and missing data. Never fabricate measured traces or performance claims.
4. Document future bounded evidence-gathering tasks; do not implement new closures, tune physics, or change defaults.

## Acceptance
- Source-linked, auditable gap inventory; blockers and next gates explicit.
- Completed work not repeated; no unverified empirical validation claim.

# Common execution rules
- Sole implementation destination: `israel-shero/openMotor_Ivan`. Never write to `israel-shero/openMotor-srm1d`; historical reference only.
- Check latest branches, open PRs, checkpoint, AGENTS.md, current code and tests first. Skip or narrow work already completed.
- Start from `integration/srm1d-packaging` only after verifying it remains the intended integration branch. Create the named task branch and target the integration branch for review; do not modify upstream-aligned `staging`.
- Keep commits scoped, avoid unrelated refactors, preserve existing solver defaults and numerical physics.
- Test existing and new behavior, document commands, results, limitations, regression checks and upstream compatibility. Maintain changelog or PR change summary.
- Do not merge without approval; report blockers and never invent validation evidence.
