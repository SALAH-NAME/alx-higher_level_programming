#!/usr/bin/python3
"""
This a test unit for base.py
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_square_instantiation(self):
        """Test instantiation of the Square class"""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(3, 4)
        self.assertEqual(s2.width, 3)
        self.assertEqual(s2.height, 3)
        self.assertEqual(s2.x, 4)
        self.assertEqual(s2.y, 0)

        s3 = Square(2, 3, 4)
        self.assertEqual(s3.width, 2)
        self.assertEqual(s3.height, 2)
        self.assertEqual(s3.x, 3)
        self.assertEqual(s3.y, 4)

    def test_square_size(self):
        """Test size property and setter of the Square class"""
        s1 = Square(5)

        # Test size getter
        self.assertEqual(s1.size, 5)

        # Test size setter
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_square_update(self):
        """Test update method of the Square class"""
        s1 = Square(10, 10, 10)

        # Update with no-keyword arguments
        s1.update(89)
        expected_output_4 = '[Square] (89) {}/{} - {}'.format(
                s1.x, s1.y, s1.size)

        # Update with keyword arguments
        s1.update(x=5, y=6, size=7, id=99)

        expected_output_5 = '[Square] (99) {}/{} - {}'.format(
                s1.x, s1.y, s1.size)

        self.assertEqual(str(s1), expected_output_5)

    def test_square_to_dictionary(self):
        """Test to_dictionary method of the Square class"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        expected_output_6 = {'x': 2, 'y': 1, 'id': s1.id, 'size': 10}
        self.assertEqual(s1_dictionary, expected_output_6)


if __name__ == '__main__':
    unittest.main()
