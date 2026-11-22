# GUI performance baseline and event-loop responsiveness

**Status:** proposed, not claimed.

## Scope
Profile load/edit/simulate/plot/export workflows with real fixture sizes; measure UI thread stalls, event-loop latency, time to first plot, peak memory and redraw count. Identify existing async behavior and upstream performance fixes first. Coordinate INF-05, UI-09 and M0-0F; no claims of speedups without measurement.

## Execution and acceptance
Read current implementation and upstream before coding. Acquire verified create-only claim per CLAIM_PROTOCOL.md before task-specific implementation. Benchmark reproducible representative workloads and log environment, median timings, variability, peak memory, screenshots where useful, baseline correctness and regression tests. Preserve numerical data, settings and behavior. Scoped PR, independent review, no merge without approval.
