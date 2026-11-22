# Plot rendering and geometry-preview efficiency

**Status:** proposed, not claimed.

## Scope
Implement evidence-driven throttled redraws, incremental updates, data decimation for display only, cached geometry previews and efficient large-dataset rendering. Preserve original data for export and cursor values; test zoom, dual independent axes, empty/NaN data, resize, high DPI and large runs.

## Execution and acceptance
Read current implementation and upstream before coding. Acquire verified create-only claim per CLAIM_PROTOCOL.md before task-specific implementation. Benchmark reproducible representative workloads and log environment, median timings, variability, peak memory, screenshots where useful, baseline correctness and regression tests. Preserve numerical data, settings and behavior. Scoped PR, independent review, no merge without approval.
