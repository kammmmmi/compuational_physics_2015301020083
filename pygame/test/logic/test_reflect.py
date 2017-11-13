from unittest import TestCase

from models.color import Color


class ReflectTest(TestCase):
    def test_reflect(self):
        instance = Color
        self.assertIsInstance(instance(), Color)

if __name__ == '__main__':
    import unittest
    unittest.main()