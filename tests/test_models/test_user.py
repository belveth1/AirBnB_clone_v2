#!/usr/bin/python3
"""Tests for user"""
import unittest
import os
import pep8
from models.user import User
from models.base_model import BaseModel


class Testuser(unittest.TestCase):
    """To test user Class"""

    @classmethod
    def setUpClass(cls):
        """Setup for test"""
        cls.user1 = User()
        cls.user1.email = "michaelkazembe@gmail.com"
        cls.user1.password = "atat"
        cls.user1.first_name = "Michael"
        cls.user1.last_name = "Kazembe"

    @classmethod
    def tearDownClass(cls):
        """Teardown for test"""
        del cls.user1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_user(self):
        """Test for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_pep8_user(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_subclass_user(self):
        """Test if user inherited from BaseModel"""
        self.assertTrue(issubclass(self.user1.__class__, BaseModel), True)

    def test_attribute_user(self):
        """Test for attributes in user"""
        self.assertTrue('id' in self.user1.__dict__)
        self.assertTrue('created_at' in self.user1.__dict__)
        self.assertTrue('email' in self.user1.__dict__)
        self.assertTrue('password' in self.user1.__dict__)
        self.assertTrue('first_name' in self.user1.__dict__)
        self.assertTrue('last_name' in self.user1.__dict__)

    def test_attributeType_user(self):
        """Test attribute types in instances"""
        self.assertEqual(type(self.user1.email), str)
        self.assertEqual(type(self.user1.password), str)
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.last_name), str)

    def test_to_dict(self):
        """Test if serialization works"""
        self.assertEqual('to_dict' in dir(self.user1), True)

    def test_save(self):
        """Test the save function"""
        self.user1.save()
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)


if __name__ == "__main__":
    unittest.main()
