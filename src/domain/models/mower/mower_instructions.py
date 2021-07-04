from src.domain.services.move_mower_forward import MoveMowerForward
from src.domain.services.turn_mower_to_left import TurnMowerToLeft
from src.domain.services.turn_mower_to_right import TurnMowerToRight


class MowerInstructions:

    def __init__(self, mower, instructions):
        self._mower = mower
        self._instructions = self._parse_instructions(instructions)

    def _parse_instructions(self, instructions):
        result = []
        for instruction in instructions:
            if instruction == 'R':
                result.append(TurnMowerToRight(self._mower))
            if instruction == 'L':
                result.append(TurnMowerToLeft(self._mower))
            if instruction == 'M':
                result.append(MoveMowerForward(self._mower))
        return result

    @property
    def mower(self):
        return self._mower

    @property
    def instructions(self):
        return self._instructions
