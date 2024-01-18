#!/usr/bin/python3
"""Tests for BaseModel"""
import unittest
import os
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """To test BaseModel Parent Class"""

    @classmethod
    def setUpClass(cls):
        """Setup for test"""
        cls.base1 = BaseModel()
        cls.base1.name = "Peter"
        cls.base1.number = 90

    @classmethod
    def tearDownClass(cls):
        """Teardown for test"""
        del cls.base1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_base1(self):
        """Test for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_pep8_base1(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_init_(self):
        """Test for init"""
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_attribute_base1(self):
        """Test for attributes in BaseModel class"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_attributeType_base1(self):
        """Test attribute types in instances"""
        self.assertEqual(type(self.base1.name), str)

    def test_to_dict(self):
        """Test if serialization works"""
        dictionary = self.base1.to_dict()
        self.assertEqual(self.base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(dictionary['created_at'], str)
        self.assertIsInstance(dictionary['updated_at'], str)

    def test_save(self):
        """Test the save function"""
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)


if __name__ == "__main__":
    unittest.main()
