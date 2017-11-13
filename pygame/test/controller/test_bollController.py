from unittest import TestCase

from controller.boll_controller import BollController
from models.boll import Boll


class TestBollController(TestCase):
    def setUp(self):
        self.instance = BollController()

    def test_init(self):
        self.instance.generate_texture()

    def test_create(self):
        a = self.instance.create()
        self.assertIsInstance(a, Boll)
    pass
