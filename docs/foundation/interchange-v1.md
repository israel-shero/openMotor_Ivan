# Inert record interchange v1

This optional JSON format exchanges named records such as catalog labels.
The standalone `interchange.py` module uses only the Python standard library.
Import it from the source checkout. It is outside the packaged application.

```json
{
  "format": "inert-records",
  "version": 1,
  "records": [
    {"id": "item-a", "label": "Archive"}
  ]
}
```

The envelope has exactly the three keys shown. The version is the integer
`1`. Records are an ordered list and may be empty. Each record has exactly
an `id` and a `label`. Both are nonblank Unicode strings without unpaired
surrogates. An ID has no surrounding whitespace and must be unique within
the document. ID comparison is case-sensitive and uses the original
characters without Unicode normalization.

`loads` parses and validates JSON, including rejecting duplicate object keys.
`validate` checks a decoded document without changing it. `dumps` validates
first, preserves record order, sorts object keys, escapes non-ASCII characters,
and emits compact JSON without a trailing newline. Validation errors raise
`InterchangeError`, a subclass of `ValueError`.

Readers reject versions and fields outside this contract. Additions to the
document structure require a new format version. This version is independent
of the existing saved-file version, and the saved-file loader stays separate.
