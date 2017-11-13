from unittest import TestCase

from core.world_engine import World
from models.boll import Boll


class WorldTestCase(TestCase):
    def setUp(self):
        self.instance = World()

    def test_create_object(self):
        self.instance.create(Boll)
        self.assertIsInstance(self.instance.objects[-1], Boll)
