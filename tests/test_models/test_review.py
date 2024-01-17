#!/usr/bin/python3
"""Tests for Review"""
import unittest
import os
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """To test Review Class"""

    @classmethod
    def setUpClass(cls):
        """Setup for test"""
        cls.review1 = Review()
        cls.review1.place_id = "Morocco"
        cls.review1.user_id = "Michael"
        cls.review1.text = "I loved it there"

    @classmethod
    def tearDownClass(cls):
        """Teardown for test"""
        del cls.review1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_Review(self):
        """Test for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_pep8_review(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_subclass_Review(self):
        """Test if Review inherited from BaseModel"""
        self.assertTrue(issubclass(self.review1.__class__, BaseModel), True)

    def test_attribute_Review(self):
        """Test for attributes in Review"""
        self.assertTrue('id' in self.review1.__dict__)
        self.assertTrue('created_at' in self.review1.__dict__)
        self.assertTrue('updated_at' in self.review1.__dict__)
        self.assertTrue('place_id' in self.review1.__dict__)
        self.assertTrue('user_id' in self.review1.__dict__)
        self.assertTrue('text' in self.review1.__dict__)

    def test_attributeType_Review(self):
        """Test attribute types in instances"""
        self.assertEqual(type(self.review1.place_id), str)
        self.assertEqual(type(self.review1.user_id), str)
        self.assertEqual(type(self.review1.text), str)

    def test_to_dict(self):
        """Test if serialization works"""
        self.assertEqual('to_dict' in dir(self.review1), True)

    def test_save(self):
        """Test the save function"""
        self.review1.save()
        self.assertNotEqual(self.review1.created_at, self.review1.updated_at)


if __name__ == "__main__":
    unittest.main()
