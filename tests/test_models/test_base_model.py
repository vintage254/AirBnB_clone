#!/usr/bin/python3
"""
unittest for the base model class 
"""
import unittest
from models.base_model import BaseModel
class TestBasemodel(unittest.TestCase):
    def test_init(self):
        test_model = BaseModel()

        self.assertIsNotNone(test_model.id)
        self.assertIsNotNone(test_model.created_at)
        self.assertIsNotNone(test_model.updated_at)

    def test_save(self):

        test_model = BaseModel()

        first_updated_t = test_model.updated_at
        second_updated_t = test_model.save()

        self.assertNotEqual(first_updated_t, second_updated_t)

    def test_to_dict(self):
        
        test_model = BaseModel()

        test_dict = test_model.to_dict()

        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict["__class__" ] , 'BaseModel' )
        self.assertEqual(test_dict['id'] , test_model.id)
        self.assertEqual(test_dict['created_at'] ,test_model.created_at.isoformat())
        self.assertEqual(test_dict['updated_at'] ,test_model.updated_at.isoformat())

    def test_str(self):

        test_model = BaseModel()

        self.assertTrue(str(test_model).startswith('[BaseModel]'))
        self.assertIn(test_model.id , str(test_model))
        self.assertIn(str(test_model.__dict__ ) ,str(test_model))

if __name__ == "__main__":
    unittest.main()
