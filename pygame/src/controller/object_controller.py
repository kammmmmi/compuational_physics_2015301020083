import pygame
from models.color import Color

from models.point import Point

"""
:author Alan WANG
:contract alan1995wang@outlook.com
"""


class ObjectController(object):
    def __init__(self):
        self.background_color = Color(0, 0, 0, 0)
        self.loc = Point(0, 0)
        self.texture = self.generate_texture()

    def generate_texture(self):
        return pygame.Surface([0, 0])

    def create(self):
        # todo: add default instance init code
        pass
