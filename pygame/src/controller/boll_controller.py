from controller.object_controller import ObjectController
from models.boll import Boll
from models.color import Color
import pygame as pg


class BollController(ObjectController):
    def __init__(self):
        self.default_radius = 10
        self.color = Color("red")
        super().__init__()
        dir(self)

    def generate_texture(self, **config):
        boll_surface = pg.Surface((200, 200), pg.SRCALPHA, 32)
        boll_surface.fill(self.background_color.to_tuple())
        rect = pg.draw.circle(boll_surface, self.color.to_tuple(), (100, 100), self.default_radius)
        return boll_surface.subsurface(rect)

    def create(self):
        # fixme : change to mutable loc
        return Boll(id=1, name="A Boll", texture=self.generate_texture(), loc=(200, 200))
        pass



