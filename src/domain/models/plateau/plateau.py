from src.domain.models.plateau.constants import (INDEX_FOR_X_AXIS, INDEX_FOR_Y_AXIS, SEPARATOR)


class Plateau:
    def __init__(self, size):
        self._bound_x = size.split(SEPARATOR)[INDEX_FOR_X_AXIS]
        self._bound_y = size.split(SEPARATOR)[INDEX_FOR_Y_AXIS]

    @property
    def bound_x(self):
        return self._bound_x

    @property
    def bound_y(self):
        return self._bound_y
