# Saved-file migration inventory

The current envelope contains `version`, `type`, and `data`. The application
reads current files as stored, rejects future versions, and applies the
registered per-type migration chain to older files. Loading a file does not
rewrite it.

| Source | Next |
| --- | --- |
| 0.1.0 | 0.2.0 |
| 0.2.0 | 0.3.0 |
| 0.3.0 | 0.4.0 |
| 0.4.0 | 0.5.0 |
| 0.5.0 | 0.6.0 |
| 0.6.0 | 0.6.1 |
| 0.6.1 | 0.7.0 |

`test/unit/migrationBaseline.py` checks migration registration and rejection
of missing keys and invalid versions. These checks cover the graph. The graph
does not establish support for every file type at every version. Existing
`test/unit/fileIO.py` covers the current envelope and the historical recent-file
passthrough. Existing igniter tests cover plugin-dependent migration behavior.

Current rejection behavior uses `ValueError` for missing keys or a future
version and `TypeError` for a recognized but mismatched file type. The error
from a malformed version reaching the comparison routine is an implementation
detail. The historical envelope uses Python YAML tags. Fixtures created by
the tests are trusted inputs. Review any change to the parser separately.
