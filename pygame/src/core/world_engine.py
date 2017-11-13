from models.color import Color
import pygame


class World(object):
    def __init__(self):
        self.background = Color().get('green')

        self.objects = []

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown()
        pass

    def create(self, cls: type):
        module = getattr(__import__("controller."+cls.__name__.lower()+"_controller")
                         , cls.__name__.lower()+"_controller"
                         )
        assert hasattr(module, cls.__name__+"Controller"), dir(module)

        clscc = getattr(module, cls.__name__+"Controller")()
        self.objects.append(clscc.create())

    def handle_keydown(self):
        pass
