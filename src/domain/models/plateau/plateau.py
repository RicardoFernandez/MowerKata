class Plateau:
    def __init__(self, size):
        self._bound_x = size.split(' ')[0]
        self._bound_y = size.split(' ')[1]

    @property
    def bound_x(self):
        return self._bound_x

    @property
    def bound_y(self):
        return self._bound_y
