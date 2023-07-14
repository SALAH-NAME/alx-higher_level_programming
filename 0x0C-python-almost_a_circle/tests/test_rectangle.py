#!/usr/bin/python3
"""This file a Test unit for Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class"""

    def setUp(self):
        """Resets __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Tests for id attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width(self):
        """Tests for width attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

        r1.width = 20
        self.assertEqual(r1.width, 20)

    def test_height(self):
        """Tests for height attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)

        r1.height = 20
        self.assertEqual(r1.height, 20)

    def test_x(self):
        """Tests for x attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        r1.x = 20
        self.assertEqual(r1.x, 20)

    def test_y(self):
        """Tests for y attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        r1.y = 20
        self.assertEqual(r1.y, 20)


if __name__ == '__main__':
    unittest.main()
