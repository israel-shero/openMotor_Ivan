# Agent task queue — openMotor_Ivan

**Only target:** https://github.com/israel-shero/openMotor_Ivan

This directory is a versioned task queue for Codex and other agents. GitHub Issues were disabled when this queue was created (2026-11-21), so these Markdown files are the source of truth until issues can be enabled. Tasks are proposals, not claims of unimplemented functionality. Check current code, branch and PRs before starting.

## How an agent should pick work
1. Read this file, `CHECKPOINT_2026_11_20.md`, repository agent instructions and the active integration branch.
2. Choose an unclaimed task with satisfied dependencies; inspect code for existing implementation before proceeding.
3. Claim the task by announcing its file and proposed branch; coordinate parallel work to avoid conflicting edits.
4. Execute the task's bounded scope and acceptance gates, then open a PR against `integration/srm1d-packaging` after approval.
5. Update this index/task status in the PR. Never assume this document reflects live GitHub state.

## Queue
| Task | Prompt | Dependencies | Parallel work |
|---|---|---|---|
| M0-0B | [Serialization/config/QA baselines](M0-0B-baselines.md) | None | With 0D, 0F, 0G |
| M0-0C | [.ric contract](M0-0C-ric-contract.md) | 0B final results | Audit now; finalize later |
| M0-0D | [CI and headless GUI tests](M0-0D-ci.md) | Coordinate with 0B | Yes |
| M0-0E | [Plugin integration hardening](M0-0E-plugin.md) | Coordinate 0B/0D | Audit now |
| M0-0F | [Plotting, overlays, dual axes](M0-0F-plots.md) | None | Yes |
| M0-0G | [Validation evidence and gaps](M0-0G-validation.md) | None | Yes |

**Milestone 0 priority:** 0B, then 0C; 0D can begin independently. No new erosive closure, physics-default changes or empirical validation claims are authorized by these prompts.

# Common execution rules
- Sole implementation destination: `israel-shero/openMotor_Ivan`. Never write to `israel-shero/openMotor-srm1d`; historical reference only.
- Check latest branches, open PRs, checkpoint, AGENTS.md, current code and tests first. Skip or narrow work already completed.
- Start from `integration/srm1d-packaging` only after verifying it remains the intended integration branch. Create the named task branch and target the integration branch for review; do not modify upstream-aligned `staging`.
- Keep commits scoped, avoid unrelated refactors, preserve existing solver defaults and numerical physics.
- Test existing and new behavior, document commands, results, limitations, regression checks and upstream compatibility. Maintain changelog or PR change summary.
- Do not merge without approval; report blockers and never invent validation evidence.
