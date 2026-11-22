# Claim coordinator live-test evidence (2026-11-22 UTC)

**Repository:** israel-shero/openMotor_Ivan  
**Deployed branch:** `staging`  
**Merge PR:** https://github.com/israel-shero/openMotor_Ivan/pull/6  
**Merge commit:** `745757b44c15b8768780cd77fb98696478f6f9cb`  
**Active immutable-claim ruleset:** https://github.com/israel-shero/openMotor_Ivan/rules/27825165

## Results
| Test | GitHub Actions evidence | Observed output | Result |
|---|---|---|---|
| Two simultaneous attempts (0 s stagger) | https://github.com/israel-shero/openMotor_Ivan/actions/runs/44983137091 | Exactly one `ACQUIRED`, one `CONFLICT`; resulting test ref SHA matches merge commit | PASS |
| Two competing attempts (5 s stagger) | https://github.com/israel-shero/openMotor_Ivan/actions/runs/44983246621 | Exactly one `ACQUIRED`, one `CONFLICT`; resulting test ref SHA matches merge commit | PASS |

The tests used two competing threads within the **same Actions process and credential**, calling GitHub's actual create-only `POST /git/refs` API. These tests **did not** exercise independent users, different tokens, permission boundaries, process failures, interrupted network responses or lease recovery. Offline mocked coordinator tests passed in GitHub Actions. Python 3.9 and 3.10 general unit test CI passed after pinning ubuntu-24.04.

## Durable test refs
- `refs/heads/claims/TEST-CLAIM-PILOT-20261121-A`
- `refs/heads/claims/TEST-CLAIM-PILOT-20261121-B`

Both were independently fetched via GitHub REST after the workflows completed, and both resolve to `745757b44c15b8768780cd77fb98696478f6f9cb`. These are **testing-only** references. Do not reuse them as production claims, steal them, or delete them automatically. Any cleanup requires authorized administrator action and explicit approval.

## Remaining rollout gates
- [ ] Design verified task owner identity, unique generation/fencing token, heartbeat and recovery with safe stale-claim reconciliation.
- [ ] Implement mandatory PR check that confirms the actor and generation owns the exact task claim, not merely that the ref exists.
- [ ] Run independent-process / independently authenticated concurrent acquisition tests.
- [ ] Run deliberate network failure, expired-owner and recovery simulations.
- [ ] Enable appropriate default-branch required checks and limited bypass policies for PR acceptance.
- [ ] Validate cross-repository dependencies, task status reconciliation and abort/cancellation behavior.

**Current readiness:** Atomic create-ref acquisition is **verified for the two controlled race cases above**. Protected claim refs are configured. Full unattended parallel task ownership and safe recovery are **NOT VERIFIED**. Do not treat this as permission to run autonomous agents without supervision.
