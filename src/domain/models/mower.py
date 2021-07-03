from src.domain.models.plateau import Plateau


class Mower:
    def __init__(self, plateau: Plateau, initial_position: str):
        self._plateau = plateau
        self._position_x = initial_position.split(' ')[0]
        self._position_y = initial_position.split(' ')[1]
        self._facing_to = initial_position.split(' ')[2]

    def turn_right(self):
        if self._facing_to == 'N':
            self._facing_to = 'E'
            return
        if self._facing_to == 'E':
            self._facing_to = 'S'
            return
        if self._facing_to == 'S':
            self._facing_to == 'W'
            return
        if self._facing_to == 'W':
            self._facing_to == 'N'
            return

    def current_state(self):
        return self._position_x + ' ' + self._position_y + ' ' + self._facing_to
