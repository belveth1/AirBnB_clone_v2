#!/usr/bin/python3
"""Tests for Amenity"""
import unittest
import os
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """To test Amenity Class"""

    @classmethod
    def setUpClass(cls):
        """Setup for test"""
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Towels"

    @classmethod
    def tearDownClass(cls):
        """Teardown for test"""
        del cls.amenity1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_Amenity(self):
        """Test for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_pep8_Amenity(self):
        """Tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attribute_Amenity(self):
        """Test for attributes in Amenity"""
        self.assertTrue('id' in self.amenity1.__dict__)
        self.assertTrue('created_at' in self.amenity1.__dict__)
        self.assertTrue('updated_at' in self.amenity1.__dict__)
        self.assertTrue('name' in self.amenity1.__dict__)

    def test_attributeType_Amenity(self):
        """Test attribute types in instances"""
        self.assertEqual(type(self.amenity1.name), str)

    def test_inheritance_Amenity(self):
        """Test if Amenity inherited from BaseModel"""
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_to_dict(self):
        """Test if serialization works"""
        self.assertEqual('to_dict' in dir(self.amenity1), True)

    def test_save(self):
        """Test the save function"""
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)


if __name__ == "__main__":
    unittest.main()
