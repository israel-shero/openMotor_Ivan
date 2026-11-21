# Agent task queue — openMotor_Ivan

## Mandatory before starting any task
Read [CLAIM_PROTOCOL.md](CLAIM_PROTOCOL.md). **Claim the task atomically on GitHub before any task-specific work.** If a lock already exists or create-only behavior cannot be guaranteed, do not start; choose another eligible task. Issue labels/comments alone are not sufficient for concurrency safety.

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

## Reliability and coverage backlog (new)
| Task | Prompt | Dependency |
|---|---|---|
| INF-01 | [Atomic claims and lease recovery](INF-01-atomic-claims.md) | Highest priority; required before autonomous parallel execution |
| INF-02 | [Task registry and scheduler](INF-02-task-registry.md) | INF-01 for live claims; schema can begin independently |
| INF-03 | [Cross-repository contract CI](INF-03-contract-ci.md) | Coordinate SRM 1D #14 and #10 |
| INF-04 | [Independent verification and review](INF-04-independent-verification.md) | Can start now |
| INF-05 | [Performance regression tracking](INF-05-performance.md) | Can start now |
| QA-01 | [Property-based GUI and serialization tests](QA-01-property-tests.md) | Coordinate M0-0F and QA-02 |
| QA-02 | [Golden-file compatibility corpus](QA-02-golden-files.md) | Coordinate M0-0B/M0-0C |

**Recommended parallel starts:** INF-01 design/adversarial tests, INF-03 fixture inventory, INF-04 report schema, QA-02 corpus inventory. Do not dispatch task implementation without a verified exclusive claim.

## UI and usability workstream
| ID | Task | Dependencies |
|---|---|---|
| UI-01 | [UI inventory and workflow audit](UI-01-workflow-audit.md) | First; check upstream before implementing |
| UI-02 | [Plotting and run comparison](UI-02-plot-workspace.md) | M0-0F; preserve dual-axis requirement |
| UI-03 | [Configuration inspector and multi-edit](UI-03-configuration-inspector.md) | UI-01 |
| UI-04 | [Interactive axial geometry editor](UI-04-geometry-editor.md) | SRM #3, UI-01 |
| UI-05 | [Simulation status and diagnostics](UI-05-diagnostics.md) | Solver diagnostics contract |
| UI-06 | [Command palette, presets and recovery](UI-06-productivity.md) | UI-01 |
| UI-07 | [Axial results explorer](UI-07-axial-explorer.md) | SRM #10 result contract |
| UI-08 | [UQ/identification workbench](UI-08-uq-workbench.md) | SRM #18–#23; start UX design separately |
| UI-09 | [GUI QA, accessibility and performance](UI-09-qa-accessibility.md) | M0-0D; can begin now |
| UI-10 | [Reproducible report export](UI-10-report-export.md) | Result schema and UI-02 |

**Parallel preparation:** UI-01 inventory, UI-02 plotting audit, UI-09 test baseline, UI-08 UQ mock interface. Production implementation requires verified exclusive claims and pinned cross-repo contracts.

## Architecture, data and maintenance expansion
| Task | Prompt |
|---|---|
| ARCH-02 | [plugin-capabilities](ARCH-02-plugin-capabilities.md) |
| ARCH-03 | [release-migration](ARCH-03-release-migration.md) |
| AGENT-02 | [merge-checkpoints](AGENT-02-merge-checkpoints.md) |
| RESEARCH-02 | [evidence-links](RESEARCH-02-evidence-links.md) |
| DATA-03 | [drawing-import-review](DATA-03-drawing-import-review.md) |
| DOC-01 | [onboarding](DOC-01-onboarding.md) |

These extend existing M0/INF/UI work; audit for overlap before implementing. Reference drawing workflow is evidence/metadata-oriented, not an assertion of a fully specified motor.
