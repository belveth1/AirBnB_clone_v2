#!/usr/bin/python3
"""Tests for state"""
import unittest
import os
import pep8
from models.state import State
from models.base_model import BaseModel


class Teststate(unittest.TestCase):
    """To test state Class"""

    @classmethod
    def setUpClass(cls):
        """Setup for test"""
        cls.state1 = State()
        cls.state1.name = "Lagos"

    @classmethod
    def tearDownClass(cls):
        """Teardown for test"""
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_state(self):
        """Test for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_pep8_state(self):
        """checks for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_subclass_state(self):
        """Test if state inherited from BaseModel"""
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_attribute_state(self):
        """Test for attributes in state"""
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)

    def test_attributeType_state(self):
        """Test attribute types in instances"""
        self.assertEqual(type(self.state1.name), str)

    def test_to_dict(self):
        """Test if serialization works"""
        self.assertEqual('to_dict' in dir(self.state1), True)

    def test_save(self):
        """Test the save function"""
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)


if __name__ == "__main__":
    unittest.main()
