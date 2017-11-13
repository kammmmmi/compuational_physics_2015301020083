from pygame.colordict import THECOLORS

from notification.decorator import deprecated


class Color(object):
    def __init__(self, *args):
        self.r = 0
        self.g = 0
        self.b = 0
        self.a = 255

        if args:
            if isinstance(args[0], tuple):
                self.r, self.g, self.b, self.a = args[0]
            elif isinstance(args[0], str):
                self.r, self.g, self.b, self.a = THECOLORS[args[0]]
            elif len(args) == 4:
                self.r, self.g, self.b, self.a = args


    @deprecated
    def get(self, *args, **kwargs):
        assert isinstance(args[0], str), str(args)
        if len(args) == 1:
            self.r, self.g, self.b, self.a = THECOLORS[args[0]]
            return self.to_tuple()

    def to_tuple(self):
        return self.r, self.g, self.b, self.a
