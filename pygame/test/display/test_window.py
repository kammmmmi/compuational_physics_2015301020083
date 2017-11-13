from unittest import TestCase
import unittest as test

from display.window import Window


class TestWindow(TestCase):
    def setUp(self):
        self.instance = Window()

    def test_observation(self):
        self.instance.set_observation(None)

    def test_draw_none(self):
        self.instance.set_observation(None)
        with self.assertRaises(RuntimeError):
            self.instance.observing()


if __name__ == '__main__':
    test.main()
