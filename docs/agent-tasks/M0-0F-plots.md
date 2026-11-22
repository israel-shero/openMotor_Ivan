# M0-0F — Result channels, CSV overlays and independent axis scaling
**Suggested branch:** `milestone0/results-plot-contract`. **Dependencies:** none for audit; coordinate GUI tests with 0D. **Parallel:** yes.

## Instructions
1. Audit existing result channels, units, plotting widgets, CSV overlay support, saved settings and tests; avoid duplicating completed features.
2. Specify independently selectable left/right y-axis ranges and autoscale, channel-axis association, legend behavior, overlay time alignment, missing data and export semantics.
3. Add tests for existing plotting/overlay behavior. If independent-axis implementation is small and isolated, implement with focused tests and screenshots; otherwise create a follow-up implementation task.
4. Preserve single-axis defaults and prevent silent unit mixing; numerical solver outputs must remain unchanged.

## Acceptance
- Clear axis/overlay behavior specification and regression tests.
- Any implementation is bounded, tested and documented; no unrequested plot redesign.

# Common execution rules
- Sole implementation destination: `israel-shero/openMotor_Ivan`. Never write to `israel-shero/openMotor-srm1d`; historical reference only.
- Check latest branches, open PRs, checkpoint, AGENTS.md, current code and tests first. Skip or narrow work already completed.
- Start from `integration/srm1d-packaging` only after verifying it remains the intended integration branch. Create the named task branch and target the integration branch for review; do not modify upstream-aligned `staging`.
- Keep commits scoped, avoid unrelated refactors, preserve existing solver defaults and numerical physics.
- Test existing and new behavior, document commands, results, limitations, regression checks and upstream compatibility. Maintain changelog or PR change summary.
- Do not merge without approval; report blockers and never invent validation evidence.
