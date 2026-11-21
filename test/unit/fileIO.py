import tempfile
import unittest
from pathlib import Path

import yaml

from uilib.fileIO import fileTypes, loadFile, saveFile


class TestFileEnvelope(unittest.TestCase):
    def test_current_envelope_preserves_unknown_configuration(self):
        data = {"solver": "unregistered-test-solver", "options": {"custom": [1, 2]}}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.ric"
            saveFile(path, data, fileTypes.MOTOR)
            # FullLoader cannot decode the existing Python-tagged file envelope.
            # This file was produced by saveFile in this test.
            envelope = yaml.load(path.read_text(), Loader=yaml.Loader)
            self.assertEqual(envelope, {
                "version": (0, 7, 0),
                "type": fileTypes.MOTOR,
                "data": data,
            })
            self.assertEqual(loadFile(path, fileTypes.MOTOR), data)
            with self.assertRaises(TypeError):
                loadFile(path, fileTypes.PREFERENCES)

    def test_legacy_recent_files_migrate_without_rewriting_input(self):
        data = ["example.ric"]
        contents = yaml.dump({
            "version": (0, 5, 0),
            "type": fileTypes.RECENT_FILES,
            "data": data,
        })
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "recent.yaml"
            path.write_text(contents, encoding="utf-8")
            self.assertEqual(loadFile(path, fileTypes.RECENT_FILES), data)
            self.assertEqual(path.read_text(encoding="utf-8"), contents)
