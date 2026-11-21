# Solver configuration selection

The global active-solver preference selects the solver name. Per-motor settings
override parameters for the selected name. A nonempty motor configuration
wins over the global configuration. Empty or missing entries fall through to
the global configuration, then to `None`.

An unregistered selected name falls back to the quasi-steady name. If the
fallback solver is unavailable, the manager calls the motor's legacy simulation
entry point. Unknown saved configuration entries are retained on reload and
remain dormant until a matching solver is registered.

`test/unit/solverConfigBaseline.py` checks dispatch with a stub backend and
a stub legacy entry point. It also checks persistence of an unknown option
and handling of absent motor settings with an empty motor record.
Existing tests cover the registered plugin's stale-default upgrades.
