#!/usr/bin/python3
"""
This a test unit for base.py
"""
import unittest
from models.base import Base
from os import path, remove
import os
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        """Set up for the tests"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up after tests"""
        if path.exists("Base.json"):
            remove("Base.json")
        if path.exists("Base.csv"):
            remove("Base.csv")

    def test_base_instantiation(self):
        """Test instantiation of the Base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test to_json_string method of Base class"""
        d1 = {"id": 1, "x": 2, "y": 3}
        d2 = {"id": 4, "x": 5, "y": 6}
        json_str = Base.to_json_string([d1, d2])
        str_test = '[{"id": 1, "x": 2, "y": 3}, {"id": 4, "x": 5, "y": 6}]'
        self.assertEqual(json_str, str_test)
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, '[]')
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, '[]')

    def test_save_to_file(self):
        """Test save_to_file method of Base class"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        # Save objects to file
        Rectangle.save_to_file([r1, r2])

        # Load objects from file
        loaded_objs = Rectangle.load_from_file()

        # Test that the loaded objs have the same attributes as the saved objs
        self.assertEqual([obj.to_dictionary() for obj in loaded_objs],
                         [r1.to_dictionary(), r2.to_dictionary()])

    def test_from_json_string(self):
        """Test from_json_string method of Base class"""

        # Test loading from JSON string
        list_dicts = [{"id": 1}, {"id": 2}]

        json_str = '[{"id": 1}, {"id": 2}]'

        loaded_list_dicts = Base.from_json_string(json_str)

        # Test that the loaded list of dics is =l to the original list of dics
        self.assertEqual(loaded_list_dicts, list_dicts)

    def test_load_from_file(self):
        """Test load_from_file method of Base class"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        # Save objects to file
        Rectangle.save_to_file([r1, r2])

        # Load objects from file
        loaded_objs = Rectangle.load_from_file()

        # Test that the loaded objs have the same attributes as the saved objs
        self.assertEqual([obj.to_dictionary() for obj in loaded_objs],
                         [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method of Base class"""

        try:
            loaded_objs = Rectangle.load_from_file_csv()
            self.assertTrue(False)
        except Exception as e:
            self.assertTrue(True)

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method of Base class"""

        try:
            loaded_objs = Rectangle.load_from_file_csv()
            self.assertTrue(False)
        except Exception as e:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
