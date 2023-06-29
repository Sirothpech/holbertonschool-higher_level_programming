import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_id_assignment(self):
        s1 = Square(5)
        s2 = Square(10)
        s3 = Square(8, 0, 0, 12)

        self.assertNotEqual(s1.id, s2.id)
        self.assertNotEqual(s2.id, s3.id)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Square(10, "2")

        s = Square(10)
        with self.assertRaises(ValueError):
            s.size = -10

        s = Square(10)
        with self.assertRaises(TypeError):
            s.x = {}

        with self.assertRaises(ValueError):
            Square(10, 3, -1)

    def test_area_calculation(self):
        s1 = Square(3)
        s2 = Square(2)
        s3 = Square(8, 0, 0, 12)

        self.assertEqual(s1.area(), 9)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 64)

    def test_display(self):
        s1 = Square(4)
        expected_output = "####\n####\n####\n####\n"
        self.assertEqual(s1.display(), None)

        s2 = Square(2)
        expected_output = "##\n##\n"
        self.assertEqual(s2.display(), None)

    def test_str_representation(self):
        s2 = Square(5, 1, 0, id=3)
        self.assertEqual(str(s2), "[Square] (3) 1/0 - 5")

    def test_display_with_offset(self):
        s1 = Square(2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        self.assertEqual(s1.display(), None)

        s2 = Square(3, 1, 0)
        expected_output = " ###\n ###\n"
        self.assertEqual(s2.display(), None)

    def test_to_dictionary(self):
        s1 = Square(5, 2, 3, 1)
        expected_dict1 = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s1.to_dictionary(), expected_dict1)

        s2 = Square(3, 0, 0, 2)
        expected_dict2 = {'id': 2, 'size': 3, 'x': 0, 'y': 0}
        self.assertEqual(s2.to_dictionary(), expected_dict2)


if __name__ == '__main__':
    unittest.main()
