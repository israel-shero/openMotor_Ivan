# M0-0E — Plugin discovery, packaging, configuration and cancellation
**Suggested branch:** `milestone0/plugin-contract`. **Dependencies:** coordinate with 0B and 0D. **Parallel:** initial audit.

## Instructions
1. Audit existing plugin discovery, packaging paths, optional dependencies, stale configuration migration, progress/cancel behavior and error reporting. Identify already completed GUI fixes.
2. Compare integration points with upstream `reilleya/openMotor` and check related PRs.
3. Add focused tests for missing plugin, stale settings, discovery, progress, cancellation and exceptions. Make minimal production fixes only for confirmed defects; otherwise file a separate proposed task.
4. Verify headless and GUI import behavior and record supported packaging smoke checks.

## Acceptance
- Testable integration contract, observed defects and minimal justified changes.
- No new closures, numerical retuning, solver default change or broad GUI redesign.
- Regression test results and changelog provided.

# Common execution rules
- Sole implementation destination: `israel-shero/openMotor_Ivan`. Never write to `israel-shero/openMotor-srm1d`; historical reference only.
- Check latest branches, open PRs, checkpoint, AGENTS.md, current code and tests first. Skip or narrow work already completed.
- Start from `integration/srm1d-packaging` only after verifying it remains the intended integration branch. Create the named task branch and target the integration branch for review; do not modify upstream-aligned `staging`.
- Keep commits scoped, avoid unrelated refactors, preserve existing solver defaults and numerical physics.
- Test existing and new behavior, document commands, results, limitations, regression checks and upstream compatibility. Maintain changelog or PR change summary.
- Do not merge without approval; report blockers and never invent validation evidence.
