from core.world_engine import World
from display.window import Window
from models.boll import Boll

if __name__ == '__main__':
    window = Window()
    world = World()
    world.create(Boll)
    window.set_observation(world)
    window.observing()
