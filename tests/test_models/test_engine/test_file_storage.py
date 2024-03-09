#!/usr/bin/python3
import os
import json
import unittest
from ..models.base_model import BaseModel
from ..models.engine.file_storage import FileStorage
class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""
    def setup(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage().all(None)
    def test_all_storage_returns_dictionary(self):
        self.assertEqual(dict, type(FileStorage().all()))
    def test_new(self):
        obj = BaseModel()
        FileStorage().new(obj)
        self.assertIn(obj, FileStorage().all().values())
if __name__ == "__main__":
    unittest.main()
