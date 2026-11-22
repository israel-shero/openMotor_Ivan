# Agent development instructions — israel-shero/openMotor_Ivan

## Select and claim your own task

Choose the highest-priority eligible task in **this repository**, respecting live dependencies, claims, existing PRs and actual implemented code. If the user specifically assigns a task (for example INF-01), verify and prioritize that task rather than choosing a different one. Review current staging code and the task queue on docs/agent-task-queue when needed; unmerged planning material is not proof of implementation status.

Read [agent self-assignment](docs/agent-tasks/AGENT_SELF_ASSIGNMENT.md), [supervised pilot policy](docs/agent-tasks/SUPERVISED_PILOT.md) and [claim protocol](docs/agent-tasks/CLAIM_PROTOCOL.md).

**You are responsible for claiming your task.** Using your own authorized **non-admin** GitHub credential with Actions: write, dispatch `claim-request.yml` yourself on `staging` with task ID, agent ID, work branch and scope. Do not ask the human operator to press the Run workflow button. A dispatch is not a claim: verify completed success, the exact `claims/TASK-ID` ref and the matching published owner record before touching task code. If missing permissions, stop and report the one-time access needed.

For an eligible unclaimed task, implement only on `work/TASK-ID/AGENT-ID` (or the exact implementation branch recorded in your successful claim); test it and submit a scoped PR to the correct base. Preserve numerical correctness and compatibility. No task hopping, claim release or reassignment without a fresh authorized process.

**Do not push to the protected integration branch, approve or merge your own PR, use administrator bypass, release/delete claims, or change GitHub rulesets.** Human approval remains mandatory for merges. After opening the PR, report evidence and stop.
