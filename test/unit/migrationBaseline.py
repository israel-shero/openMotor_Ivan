"""Regression coverage for saved-file validation and the migration graph."""
import tempfile
import unittest
from pathlib import Path

import yaml

from uilib import fileIO


class TestMigrationBaseline(unittest.TestCase):
    def test_known_versions_reach_current_version_in_order(self):
        self.assertEqual(
            {version: entry["to"] for version, entry in fileIO.migrations.items()},
            {
                (0, 1, 0): (0, 2, 0),
                (0, 2, 0): (0, 3, 0),
                (0, 3, 0): (0, 4, 0),
                (0, 4, 0): (0, 5, 0),
                (0, 5, 0): (0, 6, 0),
                (0, 6, 0): (0, 6, 1),
                (0, 6, 1): (0, 7, 0),
            },
        )

    def test_invalid_envelopes_are_rejected(self):
        envelope = {
            "version": fileIO.appVersion,
            "type": fileIO.fileTypes.MOTOR,
            "data": {},
        }
        cases = [
            ("missing " + key, ValueError, {
                name: value for name, value in envelope.items() if name != key
            })
            for key in envelope
        ]
        cases.extend([
            ("future version", ValueError, dict(envelope, version=(1, 0, 0))),
            ("malformed version", TypeError, dict(envelope, version="invalid")),
        ])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.ric"
            for label, error, data in cases:
                with self.subTest(label=label):
                    path.write_text(yaml.dump(data), encoding="utf-8")
                    with self.assertRaises(error):
                        fileIO.loadFile(path, fileIO.fileTypes.MOTOR)
