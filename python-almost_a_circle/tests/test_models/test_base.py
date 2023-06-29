import unittest
import os
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    def test_save_one_rectangle(self):
        """Test for saving one rectangle."""
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_save_two_rectangles(self):
        """Test for saving two rectangles."""
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_one_square(self):
        """Test for saving one square."""
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_two_squares(self):
        """Test for saving two squares."""
        square1 = Square(10, 7, 2, 8)
        square2 = Square(8, 1, 2, 3)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)

    def test_save_overwrite(self):
        """Test for overwriting."""
        square = Square(8, 5, 9, 2)
        Square.save_to_file([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_empty_list(self):
        """Test for saving an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_no_args(self):
        """Test for no arguments."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_two_arg(self):
        """Test for two arguments."""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase(unittest.TestCase):
    """
    Test cases for Base class.
    """

    def test_creation_id(self):
        """
        Test if value of id has the correct assignment.
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(-5)
        b6 = Base(6.3)
        b7 = Base()
        b8 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, -5)
        self.assertEqual(b6.id, 6.3)
        self.assertEqual(b7.id, 4)
        self.assertEqual(b8.id, 5)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

        json_string = Base.to_json_string([{'id': 1, 'width': 2, 'height': 3}])
        self.assertEqual(json_string, '[{"id": 1, "width": 2, "height": 3}]')

    def test_from_json_string(self):
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])

        json_string = Base.from_json_string("")
        self.assertEqual(json_string, [])

        json_string = Base.from_json_string("[]")
        self.assertEqual(json_string, [])

        json_string = Base.from_json_string('[{"id": 1,\
                                            "width": 2, "height": 3}]')
        self.assertEqual(json_string, [{'id': 1, 'width': 2, 'height': 3}])


class TestPycodestyle(unittest.TestCase):
    """
    Test for Pycodestyle.
    """

    def test_pycodestyle_conformance(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/base.py',
                                    'models/rectangle.py',
                                    'models/square.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
