# Nonblocking solver execution and cancellation

**Status:** proposed, not claimed.

## Scope
Ensure long-running simulation, file loading and batch work cannot block Qt event loop; thread/process isolation consistent with Qt ownership, bounded queues, cancellation, progress updates and safe shutdown. Test rapid repeated starts, failed jobs, stale result signals and user interaction during run. Coordinate UI-05 and UQ UI-08.

## Execution and acceptance
Read current implementation and upstream before coding. Acquire verified create-only claim per CLAIM_PROTOCOL.md before task-specific implementation. Benchmark reproducible representative workloads and log environment, median timings, variability, peak memory, screenshots where useful, baseline correctness and regression tests. Preserve numerical data, settings and behavior. Scoped PR, independent review, no merge without approval.
