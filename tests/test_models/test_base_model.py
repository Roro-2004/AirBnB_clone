#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

"""
A unittest class for base model
"""


class test_base_model(unittest.TestCase):
    def test_init(self):
        """
        tests the constructor
        """
        test_model = BaseModel()

        self.assertIsNotNone(test_model.id)
        self.assertIsNotNone(test_model.created_at)
        self.assertIsNotNone(test_model.updated_at)

    def test_str(self):
        """
        tests str method
        """
        test_model = BaseModel()

        self.assertTrue(str(test_model).startswith('[BaseModel]'))
        self.assertIn(test_model.id, str(test_model))
        self.assertIn(str(test_model.__dict__), str(test_model))

    def test_save(self):
        """
        tests save method
        """

        test_model = BaseModel()

        initial = test_model.updated_at
        test_model.save()
        current = test_model.updated_at
        self.assertNotEqual(current, initial)

    def test_to_dict(self):
        """
        test to_dict method
        """

        test_model = BaseModel()

        test = test_model.to_dict()
        self.assertIsInstance(test, dict)
        self.assertEqual(test['__class__'], 'BaseModel')
        self.assertEqual(test['id'], test_model.id)
        self.assertEqual(test['created_at'], test_model.created_at.isoformat())
        self.assertEqual(test['updated_at'], test_model.updated_at.isoformat())
