import unittest

from interchange import InterchangeError, dumps, loads, validate


class TestInterchangeV1(unittest.TestCase):
    def setUp(self):
        self.document = {
            "format": "inert-records",
            "version": 1,
            "records": [
                {"label": "Café", "id": "item-b"},
                {"label": "Archive", "id": "item-a"},
            ],
        }

    def test_serialization_is_deterministic_and_preserves_order(self):
        expected = (
            '{"format":"inert-records","records":[{"id":"item-b","label":"Caf\\u00e9"},'
            '{"id":"item-a","label":"Archive"}],"version":1}'
        )
        self.assertEqual(dumps(self.document), expected)
        self.assertEqual(dumps(dict(reversed(list(self.document.items())))), expected)
        self.assertEqual(loads(expected), self.document)
        self.assertEqual(list(self.document["records"][0]), ["label", "id"])

    def test_empty_record_list_is_valid(self):
        self.document["records"] = []
        self.assertEqual(loads(dumps(self.document)), self.document)

    def test_future_and_noninteger_versions_are_rejected(self):
        for version in (2, 1.0, True, "1"):
            with self.subTest(version=version):
                self.document["version"] = version
                with self.assertRaisesRegex(InterchangeError, "unsupported interchange version"):
                    validate(self.document)

    def test_invalid_document_and_records_are_rejected(self):
        cases = [
            ([], "expected a document"),
            (dict(self.document, format="unknown"), "unsupported interchange format"),
            (dict(self.document, extra=None), "expected a document"),
            (dict(self.document, records={}), "records must be a list"),
            (dict(self.document, records=[{"id": "x"}]), r"records\[0\] must contain id and label"),
            (dict(self.document, records=[{"id": " x ", "label": "X"}]), r"records\[0\].id"),
            (dict(self.document, records=[{"id": "x", "label": ""}]), r"records\[0\].label"),
            (dict(self.document, records=[{"id": "x", "label": "\ud800"}]), r"records\[0\].label"),
            (dict(self.document, records=self.document["records"] * 2), r"records\[2\].id duplicates"),
        ]
        for document, diagnostic in cases:
            with self.subTest(diagnostic=diagnostic):
                with self.assertRaisesRegex(InterchangeError, diagnostic):
                    dumps(document)

    def test_malformed_json_and_duplicate_keys_are_rejected(self):
        with self.assertRaisesRegex(InterchangeError, "invalid JSON"):
            loads("{")
        with self.assertRaisesRegex(InterchangeError, "duplicate JSON key"):
            loads('{"format":"inert-records","version":2,"version":1,"records":[]}')
