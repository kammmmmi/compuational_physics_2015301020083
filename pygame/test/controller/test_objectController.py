from unittest import TestCase
import pygame

from controller.object_controller import ObjectController


class TestObjectController(TestCase):
    def setUp(self):
        self.instance = ObjectController()

    def test__init(self):
        self.assertEqual(self.instance.loc, (0,0))
        self.assertIsInstance(self.instance.texture, pygame.SurfaceType)

    def test_generate_texture(self):
        self.assertIsInstance(self.instance.generate_texture(), pygame.SurfaceType)

if __name__ == '__main__':
    import unittest; unittest.main()