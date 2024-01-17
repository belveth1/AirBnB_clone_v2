#!/usr/bin/python3
"""Tests for place"""
import unittest
import os
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """To test Place Class"""

    @classmethod
    def setUpClass(cls):
        """Setup for test"""
        cls.place1 = Place()
        cls.place1.city_id = "Lilongwe"
        cls.place1.user_id = "Ahmad"
        cls.place1.name = "BICC"
        cls.place1.description = "Presidential Hotel"
        cls.place1.number_rooms = 2
        cls.place1.number_bathrooms = 1
        cls.place1.max_guest = 4
        cls.place1.price_by_night = 200
        cls.place1.latitude = 44.4
        cls.place1.longitude = 23.4
        cls.place1.amenity_ids = ["Wifi", "Jacuzzi", "Toiletries"]

    @classmethod
    def tearDownClass(cls):
        """Teardown for test"""
        del cls.place1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_place(self):
        """Test for docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_pep8_place(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_subclass_place(self):
        """Test if Place inherited from BaseModel"""
        self.assertTrue(issubclass(self.place1.__class__, BaseModel), True)

    def test_attribute_place(self):
        """Test for attributes in Place"""
        self.assertTrue('id' in self.place1.__dict__)
        self.assertTrue('created_at' in self.place1.__dict__)
        self.assertTrue('updated_at' in self.place1.__dict__)
        self.assertTrue('city_id' in self.place1.__dict__)
        self.assertTrue('user_id' in self.place1.__dict__)
        self.assertTrue('name' in self.place1.__dict__)
        self.assertTrue('description' in self.place1.__dict__)
        self.assertTrue('number_rooms' in self.place1.__dict__)
        self.assertTrue('max_guest' in self.place1.__dict__)
        self.assertTrue('price_by_night' in self.place1.__dict__)
        self.assertTrue('latitude' in self.place1.__dict__)
        self.assertTrue('longitude' in self.place1.__dict__)
        self.assertTrue('amenity_ids' in self.place1.__dict__)

    def test_attributeType_place(self):
        """Test attribute types in instances"""
        self.assertEqual(type(self.place1.city_id), str)
        self.assertEqual(type(self.place1.user_id), str)
        self.assertEqual(type(self.place1.name), str)
        self.assertEqual(type(self.place1.description), str)
        self.assertEqual(type(self.place1.number_rooms), int)
        self.assertEqual(type(self.place1.number_bathrooms), int)
        self.assertEqual(type(self.place1.max_guest), int)
        self.assertEqual(type(self.place1.price_by_night), int)
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(type(self.place1.longitude), float)
        self.assertEqual(type(self.place1.amenity_ids), list)

    def test_to_dict(self):
        """Test if serialization works"""
        self.assertEqual('to_dict' in dir(self.place1), True)

    def test_save(self):
        """Test the save function"""
        self.place1.save()
        self.assertNotEqual(self.place1.created_at, self.place1.updated_at)


if __name__ == "__main__":
    unittest.main()
