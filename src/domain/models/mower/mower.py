from src.domain.models.mower.constants import CARDINAL_NOTH, CARDINAL_EAST, CARDINAL_SOUTH, CARDINAL_WEST, \
    INDEX_FOR_X_AXIS, INDEX_FOR_Y_AXIS, INDEX_FOR_FACING, SEPARATOR, MOVEMENT_UNIT
from src.domain.models.mower.exceptions import MowerOutOfBoundsException
from src.domain.models.plateau.plateau import Plateau


class Mower:
    def __init__(self, plateau: Plateau, initial_position: str):
        self._plateau = plateau
        self._position_x = int(initial_position.split(SEPARATOR)[INDEX_FOR_X_AXIS])
        self._position_y = int(initial_position.split(SEPARATOR)[INDEX_FOR_Y_AXIS])
        self._check_mower_out_of_bounds()
        self._facing_to = initial_position.split(' ')[INDEX_FOR_FACING]

    def turn_right(self):
        if self._facing_to == CARDINAL_NOTH:
            self._facing_to = CARDINAL_EAST
            return
        if self._facing_to == CARDINAL_EAST:
            self._facing_to = CARDINAL_SOUTH
            return
        if self._facing_to == CARDINAL_SOUTH:
            self._facing_to = CARDINAL_WEST
            return
        if self._facing_to == CARDINAL_WEST:
            self._facing_to = CARDINAL_NOTH
            return

    def turn_left(self):
        if self._facing_to == CARDINAL_NOTH:
            self._facing_to = CARDINAL_WEST
            return
        if self._facing_to == CARDINAL_WEST:
            self._facing_to = CARDINAL_SOUTH
            return
        if self._facing_to == CARDINAL_SOUTH:
            self._facing_to = CARDINAL_EAST
            return
        if self._facing_to == CARDINAL_EAST:
            self._facing_to = CARDINAL_NOTH
            return

    def move_forward(self):
        if self._facing_to == CARDINAL_NOTH:
            self._position_y += MOVEMENT_UNIT
            return
        if self._facing_to == CARDINAL_EAST:
            self._position_x += MOVEMENT_UNIT
            return
        if self._facing_to == CARDINAL_SOUTH:
            self._position_y -= MOVEMENT_UNIT
            return
        if self._facing_to == CARDINAL_WEST:
            self._position_x -= MOVEMENT_UNIT
            return

    def current_state(self):
        return str(self._position_x) + ' ' + str(self._position_y) + ' ' + self._facing_to

    def _check_mower_out_of_bounds(self):
        mower_is_out_of_bound_in_x_axis = int(self._plateau.bound_x) < int(self._position_x)
        mower_is_out_of_bound_in_y_axis = int(self._plateau.bound_y) < int(self._position_y)
        if mower_is_out_of_bound_in_x_axis or mower_is_out_of_bound_in_y_axis:
            raise MowerOutOfBoundsException
