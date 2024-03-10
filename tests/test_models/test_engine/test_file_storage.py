#!/usr/bin/python3
"""Unit test for FileStorage class."""
import unittest
from models.base_model import BaseModel
import models
import json
import os


class FileStorageTestCase(unittest.TestCase):
    """Test case for FileStorage class."""

    def test_FileStorage_init(self):
        """Test initialization of FileStorage."""
        # Get file path and objects dictionary from FileStorage
        filepath = models.storage._FileStorage__file_path
        _objs = models.storage._FileStorage__objects

        # Check class attributes
        self.assertEqual(filepath, "file.json")
        self.assertIsInstance(filepath, str)
        self.assertIsInstance(_objs, dict)

        # Create a new BaseModel instance
        new = BaseModel()

        # Check if it has required methods
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        # Test 'all' method
        self.assertIsInstance(models.storage.all(), dict)
        self.assertNotEqual(models.storage.all(), {})

        # Check existence of 'id' attribute
        self.assertTrue(hasattr(new, "id"))
        self.assertIsInstance(new.id, str)

        # Test adding new object to storage
        keyname = "BaseModel." + new.id
        self.assertIsInstance(models.storage.all()[keyname], BaseModel)
        self.assertEqual(models.storage.all()[keyname], new)
        self.assertIn(keyname, models.storage.all())
        self.assertTrue(models.storage.all()[keyname] is new)

        # Test 'save' method
        models.storage.save()
        with open(filepath, 'r') as file:
            saved_data = json.load(file)
        self.assertIn(keyname, saved_data)
        self.assertEqual(saved_data[keyname], new.to_dict())

        # Test 'reload' method
        models.storage.all().clear()
        models.storage.reload()
        with open(filepath, 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data[keyname],
                         models.storage.all()[keyname].to_dict())

        # Test file management
        if os.path.exists(filepath):
            os.remove(filepath)
        self.assertFalse(os.path.exists(filepath))
        models.storage.reload()


if __name__ == '__main__':
    unittest.main()
