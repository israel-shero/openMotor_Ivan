# Supervised parallel-agent pilot (minimum safe coordination)

Status: **agent-selected and agent-claimed tasks with human-reviewed merges**. No unattended merging, automatic reassignment, automatic claim release, or privileged administration. Agents may choose, acquire and implement their own eligible tasks after credential setup.

## Permissions and responsibility

- An agent with its own authorized, **non-admin** GitHub identity dispatches `Request exclusive task claim` on the **trusted default branch** (openMotor: `staging`; SRM1D: `main`). **Human intervention is not required for task selection or claim dispatch.** The agent identity must have Actions: write to trigger the workflow; see [self-assignment instructions](AGENT_SELF_ASSIGNMENT.md).
- Agents use distinct labels, e.g. `codex-A`, `codex-B`, and branches `work/TASK-ID/codex-A` and `work/TASK-ID/codex-B`. Agent labels are **self-declared**, not authenticated identities; the GitHub workflow's `github.actor` identifies the dispatch credential.
- Do **not** give agents a personal administrator token, repository Rulesets bypass, or the ability to modify `staging`/`main` directly. Agents operate on their own work branches and submit PRs.
- GitHub ruleset `Pilot integration — pull requests only` protects the shared integration branch. A non-admin PR author cannot merge without **one independent approving review**. Administrator bypass is reserved for the human operator, never an AI agent. No unattended merge. If the owner authored the PR and GitHub disallows self-approval, the owner can explicitly authorize a documented manual admin-bypass merge only after reviewing CI and the changes.
- Claim refs are immutable to non-bypassing actors: they are created once and remain until manually authorized reconciliation. A stale clock does not transfer ownership.

## Claim and assignment procedure

1. Inspect live task backlog, current PRs, and existing `claims/TASK-ID`. Pick a narrow, dependency-ready task not already being developed.
2. **The agent itself** dispatches the claim workflow with **task_id**, **agent_id**, **work_branch**, and a short **scope** using its non-admin GitHub credential. Use the trusted default branch, not a feature branch. The user does not need to press Run workflow.
3. The trusted workflow performs GitHub create-only `POST /git/refs`. Exactly one claimant succeeds. A definite conflict means select another eligible task; an **ambiguous** result means STOP and reconcile before selecting another.
4. After acquiring the ref, workflow posts a ledger comment to the central record. SRM1D: [coordination issue #12](https://github.com/israel-shero/srm_1d_Ivans_vibes/issues/12). openMotor: a GitHub commit comment on the pinned base SHA (Contents permission; the repository has Issues disabled). The comment includes the verified GitHub dispatch actor and workflow URL, the agent label, base SHA, task, scope, and work branch.
5. **Do not start coding** until both the claim ref and ledger comment are visible and correspond to the same run. If publishing the comment fails, the lock remains held. Stop and reconcile; do not retry the claim or reassign it.
6. The agent creates only its named work branch, reads the exact task criteria, commits in small slices, runs tests, and opens a PR. It does not make direct writes to shared integration branches.

## Human PR checkpoint

- Review scope and whether the PR maps to an authorized claim and ledger record.
- Check base commit/ref, work branch, changed-file overlap and dependencies on other active tasks.
- Require CI passing at the candidate PR head. Read the actual test logs, not a claimed success in the PR description. Required branch checks are a future enhancement: initially the operator manually verifies test status.
- Confirm no regressions to numerical outputs, expected behavior, .ric/config compatibility, model validation, or GUI data integrity as applicable.
- Re-run CI if the base has changed or dependencies landed; do not merge stale/conflicting output.
- Merge only after the operator **explicitly authorizes that specific PR**. Do not enable automatic merging.
- Publish status on the task/ledger: `READY FOR REVIEW`, `MERGED`, `BLOCKED`, or `ABANDONED`, with PR link and reason. Claims are not automatically deleted.

## Pilot size and stop conditions

Start with at most **2 agents across low-overlap, independently verifiable tasks**; expand to 3–4 only after a clean initial integration cycle. For one session, give each agent one task and one branch; do not allow task switching, cross-repo claims or self-directed reassignment.

**Stop the pilot immediately** if:
- A task has competing claim records or an unknown ref owner.
- An agent attempts a direct shared-branch push, merge, administrative operation, or claim manipulation.
- A claim was created but not recorded, or claim/PR fields disagree.
- PR checks fail, regressions appear, or an independent review cannot attribute the changes.
- An agent becomes unreachable; retain its lock and use the manual recovery procedure.

## Not required for supervised pilot

No heartbeat daemon, lease timeout, fencing tokens, distributed scheduler, automatic recovery, or required PR-ownership status check. All become relevant **before unattended reassignment or unattended merges**. An operator must never reassign a claimed task merely because the owner has gone quiet.

## Evidence checklist for initial launch

- [ ] Exact integration branch protected via active targeted ruleset; GitHub API-read verified (not only UI).
- [ ] Administrator bypass limited to trusted human maintainers; AI tokens have no bypass powers.
- [ ] CI passing for claim-notice helper + coordinator.
- [ ] One fresh TEST-CLAIM-* acquisition using updated workflow, successful ledger comment, verified actor/run/branch/scope, and one rejected duplicate.
- [ ] Agent-selected eligible task and agent-dispatched workflow were verified against the live task queue and durable ownership record. The operator did not need to approve selection/claim.
- [ ] Human-reviewed PR with recorded CI/acceptance evidence.
- [ ] User-approved merge only.

If GitHub Actions cannot post to the ledger (notably a merged PR in a repository with Issues disabled), the claim remains reserved and **the pilot must not proceed** until the log destination is fixed and verified in a PR. Do not silently substitute workflow output as the durable ownership record.

## Ownership record correction, 2026-11-22

openMotor's initial ownership test created a `TEST-CLAIM-OWNER-20261121-C` ref but `GITHUB_TOKEN` failed with HTTP 403 when posting to the merged PR #6 issue-comment endpoint. The workflow correctly failed closed. [Failed run](https://github.com/israel-shero/openMotor_Ivan/actions/runs/44984841566); [manual incident record](https://github.com/israel-shero/openMotor_Ivan/pull/6#issuecomment-7074162968).

The openMotor workflow uses a **commit comment on its verified base SHA** as its ledger instead. Commit-comment creation is supported with GitHub Contents repository permission; the response must confirm HTTP 201 and an auditable `html_url`. This was verified end to end with a fresh test claim and an independently fetched commit comment. See [successful live run](https://github.com/israel-shero/openMotor_Ivan/actions/runs/44985235118) and [owner record](https://github.com/israel-shero/openMotor_Ivan/commit/250fea6865d6bf536667613edd04c8edf915e78f#commitcomment-211256498). The original `-C` test ref remains blocked until separately authorized cleanup.
