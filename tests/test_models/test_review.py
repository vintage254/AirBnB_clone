#!/usr/bin/python3
"""Unit test for Review class."""
import unittest
from models.review import Review
from datetime import datetime


class ReviewTestCase(unittest.TestCase):
    """Test case for Review class."""

    def test_review_attributes_existence(self):
        """Test existence of attributes."""
        new_review = Review()
        self.assertTrue(hasattr(new_review, "id"))
        self.assertTrue(hasattr(new_review, "created_at"))
        self.assertTrue(hasattr(new_review, "updated_at"))
        self.assertTrue(hasattr(new_review, "place_id"))
        self.assertTrue(hasattr(new_review, "user_id"))
        self.assertTrue(hasattr(new_review, "text"))

    def test_review_attribute_types(self):
        """Test types of attributes."""
        new_review = Review()
        self.assertIsInstance(new_review.id, str)
        self.assertIsInstance(new_review.created_at, datetime)
        self.assertIsInstance(new_review.updated_at, datetime)
        self.assertIsInstance(new_review.place_id, str)
        self.assertIsInstance(new_review.user_id, str)
        self.assertIsInstance(new_review.text, str)


if __name__ == '__main__':
    unittest.main()

