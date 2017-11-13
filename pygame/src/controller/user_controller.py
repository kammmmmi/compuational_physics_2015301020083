from controller.boll_controller import BollController
from controller.object_controller import ObjectController
from models.color import Color


class UserController(BollController):
    def __init__(self):
        super().__init__()
        self.color = Color('blue')