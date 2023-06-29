import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_id_assignment(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertNotEqual(r1.id, r2.id)
        self.assertNotEqual(r2.id, r3.id)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10

        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.x = {}

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area_calculation(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        r1 = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(r1.display(), None)

        r2 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        self.assertEqual(r2.display(), None)

    def test_str_representation(self):
        r2 = Rectangle(5, 5, 1, 0, id=3)
        self.assertEqual(str(r2), "[Rectangle] (3) 1/0 - 5/5")

    def test_display_with_offset(self):
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(r1.display(), None)

        r2 = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        self.assertEqual(r2.display(), None)

    def test_to_dictionary(self):
        r = Rectangle(3, 3, 1, 1, 1)
        expected_dict = {'id': 1, 'width': 3, 'height': 3, 'x': 1, 'y': 1}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
