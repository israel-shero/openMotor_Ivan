# M0-0D — CI and headless GUI regression gates
**Suggested branch:** `milestone0/ci-regressions`. **Dependencies:** coordinate test runner/fixtures with M0-0B. **Parallel:** yes.

## Instructions
1. Audit existing workflows, dependency versions, supported Python/platform matrix, native extensions, Qt headless setup and test commands.
2. Add minimal GitHub Actions coverage for a supported Linux/Python configuration, native build, unit tests and headless GUI smoke tests. Do not invent support for Apple Silicon runners.
3. Ensure failures are visible rather than masked by broad skips. Separate environmental limitations from regressions.
4. Document exact local/CI reproduction commands, artifact handling and upstream conflicts. Avoid unrelated dependency upgrades.

## Acceptance
- Workflow file and reproducible instructions; actual green GitHub run required before claiming CI success.
- Existing tests preserved and new baseline tests included when available.
- No solver behavior change.

# Common execution rules
- Sole implementation destination: `israel-shero/openMotor_Ivan`. Never write to `israel-shero/openMotor-srm1d`; historical reference only.
- Check latest branches, open PRs, checkpoint, AGENTS.md, current code and tests first. Skip or narrow work already completed.
- Start from `integration/srm1d-packaging` only after verifying it remains the intended integration branch. Create the named task branch and target the integration branch for review; do not modify upstream-aligned `staging`.
- Keep commits scoped, avoid unrelated refactors, preserve existing solver defaults and numerical physics.
- Test existing and new behavior, document commands, results, limitations, regression checks and upstream compatibility. Maintain changelog or PR change summary.
- Do not merge without approval; report blockers and never invent validation evidence.
