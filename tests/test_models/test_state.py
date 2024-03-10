#!/usr/bin/python3
"""Unit test for State class."""
import unittest
from models.state import State
from datetime import datetime


class StateTestCase(unittest.TestCase):
    """Test case for State class."""

    def test_state_attributes_existence(self):
        """Test existence of attributes."""
        new_state = State()
        self.assertTrue(hasattr(new_state, "id"))
        self.assertTrue(hasattr(new_state, "created_at"))
        self.assertTrue(hasattr(new_state, "updated_at"))
        self.assertTrue(hasattr(new_state, "name"))

    def test_state_attribute_types(self):
        """Test types of attributes."""
        new_state = State()
        self.assertIsInstance(new_state.id, str)
        self.assertIsInstance(new_state.created_at, datetime)
        self.assertIsInstance(new_state.updated_at, datetime)
        self.assertIsInstance(new_state.name, str)


if __name__ == '__main__':
    unittest.main()
