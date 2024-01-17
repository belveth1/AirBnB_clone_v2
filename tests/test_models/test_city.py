#!/usr/bin/python3
"""Tests for city"""
import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel


class Testcity(unittest.TestCase):
    """To test city Class"""

    @classmethod
    def setUpClass(cls):
        """Setup for test"""
        cls.city1 = City()
        cls.city1.state_id = "New York"
        cls.city1.name = "Blantyre"

    @classmethod
    def tearDownClass(cls):
        """Teardown for test"""
        del cls.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_city(self):
        """Test for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_pep8_city(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_subclass_city(self):
        """Test if city inherited from BaseModel"""
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_attribute_city(self):
        """Test for attributes in city"""
        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)

    def test_attributeType_city(self):
        """Test attribute types in instances"""
        self.assertEqual(type(self.city1.state_id), str)
        self.assertEqual(type(self.city1.name), str)

    def test_to_dict(self):
        """Test if serialization works"""
        self.assertEqual('to_dict' in dir(self.city1), True)

    def test_save(self):
        """Test the save function"""
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)


if __name__ == "__main__":
    unittest.main()
