#!/usr/bin/python3
"""Unit test for Amenity class."""
import unittest
from models.amenity import Amenity
from datetime import datetime


class AmenityTestCase(unittest.TestCase):
    """Test case for Amenity class."""

    def test_amenity_attributes_existence(self):
        """Test existence of attributes."""
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, "id"))
        self.assertTrue(hasattr(new_amenity, "created_at"))
        self.assertTrue(hasattr(new_amenity, "updated_at"))
        self.assertTrue(hasattr(new_amenity, "name"))

    def test_amenity_attribute_types(self):
        """Test types of attributes."""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity.id, str)
        self.assertIsInstance(new_amenity.created_at, datetime)
        self.assertIsInstance(new_amenity.updated_at, datetime)
        self.assertIsInstance(new_amenity.name, str)


if __name__ == '__main__':
    unittest.main()
