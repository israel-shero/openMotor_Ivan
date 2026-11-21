"""Versioned JSON interchange for inert named records."""

import json

FORMAT = "inert-records"
VERSION = 1


class InterchangeError(ValueError):
    """The document is invalid or uses an unsupported format version."""


def validate(document: object) -> None:
    """Validate a v1 document without modifying it."""
    if not isinstance(document, dict) or set(document) != {"format", "version", "records"}:
        raise InterchangeError("expected a document with format, version, and records")
    if document["format"] != FORMAT:
        raise InterchangeError("unsupported interchange format")
    version = document["version"]
    if type(version) is not int or version != VERSION:
        raise InterchangeError("unsupported interchange version")
    records = document["records"]
    if not isinstance(records, list):
        raise InterchangeError("records must be a list")

    identifiers = set()
    for index, record in enumerate(records):
        location = f"records[{index}]"
        if not isinstance(record, dict) or set(record) != {"id", "label"}:
            raise InterchangeError(f"{location} must contain id and label")
        identifier = record["id"]
        if not _valid_text(identifier) or identifier.strip() != identifier:
            raise InterchangeError(f"{location}.id must be nonempty text without surrounding whitespace")
        if identifier in identifiers:
            raise InterchangeError(f"{location}.id duplicates an earlier record")
        identifiers.add(identifier)
        if not _valid_text(record["label"]):
            raise InterchangeError(f"{location}.label must be nonempty text")


def _valid_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip()) and not any(
        "\ud800" <= character <= "\udfff" for character in value
    )


def _unique_object(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise InterchangeError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def loads(text: str) -> dict:
    """Read a JSON document and reject invalid or unsupported input."""
    try:
        document = json.loads(text, object_pairs_hook=_unique_object)
    except InterchangeError:
        raise
    except (ValueError, TypeError, RecursionError) as exc:
        raise InterchangeError("invalid JSON") from exc
    validate(document)
    return document


def dumps(document: dict) -> str:
    """Write deterministic v1 JSON while preserving the order of records."""
    validate(document)
    return json.dumps(document, ensure_ascii=True, separators=(",", ":"), sort_keys=True)
