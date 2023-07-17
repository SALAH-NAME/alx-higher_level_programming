#!/usr/bin/python3
"""
This a test unit for base.py
"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_rectangle_instantiation(self):
        """Test instantiation of the Rectangle class"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(5, 6, 7)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 6)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(8, 9, 10, 11)
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 9)
        self.assertEqual(r3.x, 10)
        self.assertEqual(r3.y, 11)

    def test_rectangle_width(self):
        """Test width property and setter of the Rectangle class"""
        r1 = Rectangle(10, 2)

        # Test width getter
        self.assertEqual(r1.width, 10)

        # Test width setter
        r1.width = 20
        self.assertEqual(r1.width, 20)

    def test_rectangle_height(self):
        """Test height property and setter of the Rectangle class"""
        r1 = Rectangle(10, 2)

        # Test height getter
        self.assertEqual(r1.height, 2)

        # Test height setter
        r1.height = 20
        self.assertEqual(r1.height, 20)

    def test_rectangle_x(self):
        """Test x property and setter of the Rectangle class"""
        r1 = Rectangle(10, 2)

        # Test x getter
        self.assertEqual(r1.x, 0)

        # Test x setter
        r1.x = 20
        self.assertEqual(r1.x, 20)

    def test_rectangle_y(self):
        """Test y property and setter of the Rectangle class"""
        r1 = Rectangle(10, 2)

        # Test y getter
        self.assertEqual(r1.y, 0)

        # Test y setter
        r1.y = 20
        self.assertEqual(r1.y, 20)

    def test_rectangle_area(self):
        """Test area method of the Rectangle class"""
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)

    def test_rectangle_display(self):
        """Test display method of the Rectangle class"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        r1 = Rectangle(4, 6)
        r1.display()
        sys.stdout = sys.__stdout__
        expected_output = '####\n####\n####\n####\n####\n####\n'
        self.assertEqual(capturedOutput.getvalue(), expected_output)

        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        r2 = Rectangle(2, 3, 2, 2)
        r2.display()
        sys.stdout = sys.__stdout__
        expected_output_2 = '\n\n' + ' ' * r2.x + '##\n' + \
                            ' ' * r2.x + '##\n' + ' ' * r2.x + '##\n'
        self.assertEqual(capturedOutput.getvalue(), expected_output_2)

    def test_rectangle_str(self):
        """Test __str__ method of the Rectangle class"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_output_3 = '[Rectangle] (12) {}/{} - {}/{}'.format(
                r1.x, r1.y, r1.width, r1.height)
        self.assertEqual(str(r1), expected_output_3)

    def test_rectangle_update(self):
        """Test update method of the Rectangle class"""
        r1 = Rectangle(10, 10, 10, 10)

        # Update with no-keyword arguments
        r1.update(89)
        expected_output_4 = '[Rectangle] (89) {}/{} - {}/{}'.format(
                r1.x, r1.y, r1.width, r1.height)

        # Update with keyword arguments
        r1.update(x=5, y=6, width=7, height=8, id=99)

        expected_output_5 = '[Rectangle] (99) {}/{} - {}/{}'.format(
                    r1.x, r1.y, r1.width, r1.height)

        self.assertEqual(str(r1), expected_output_5)

    def test_rectangle_to_dictionary(self):
        """Test to_dictionary method of the Rectangle class"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        expected_output_6 = {
                'x': 1, 'y': 9, 'id': r1.id, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, expected_output_6)


if __name__ == '__main__':
    unittest.main()
