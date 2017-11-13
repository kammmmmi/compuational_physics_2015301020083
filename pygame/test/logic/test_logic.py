from unittest import TestCase
import unittest as test


class TestLogic(TestCase):
    def test_check_none(self):
        self.assertTrue(not None, msg="passed")


if __name__ == '__main__':
    test.main()