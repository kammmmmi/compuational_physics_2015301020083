from pygame.locals import *
import pygame

from core import world_engine
from core.world_engine import World


class Window(object):
    def __init__(self):
        self.__observation = None
        pygame.init()
        self.size = (720, 640)
        self.__display = None
        self.is_observing = False
        self.last_observation_time = 0

    def set_observation(self, world: world_engine):
        self.__observation = world
        self.__display = pygame.display.set_mode(self.size, pygame.SRCALPHA, 32)

    def observing(self):
        # try to start observe
        self.is_observing = True
        if self.__observation:
            while self.is_observing:
                if pygame.time.get_ticks() - self.last_observation_time > 50:
                    self.__display.fill(self.__observation.background)
                    for obj in self.__observation.objects:
                        self.__display.blit(obj.texture, (0,0))
                    pygame.display.update()
                    self.last_observation_time = pygame.time.get_ticks()
                self.send_event(self.__observation, pygame.event.get())
        else:
            # reset to False , if raise error
            self.is_observing = False
            raise RuntimeError("No observing instance!")

    def send_event(self, world: World, events):
        world.handle_events(events)
        pass




