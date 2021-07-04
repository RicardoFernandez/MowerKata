from src.domain.models.mower.constants import INSTRUCTION_RIGHT, INSTRUCTION_LEFT, INSTRUCTION_FORWARD
from src.domain.models.mower.exceptions import \
    InvalidInstructionForMowerException
from src.domain.services.move_mower_forward import MoveMowerForward
from src.domain.services.turn_mower_to_left import TurnMowerToLeft
from src.domain.services.turn_mower_to_right import TurnMowerToRight


class MowerInstructions:

    def __init__(self, mower, instructions):
        self._check_valid_instructions(instructions)
        self._mower = mower
        self._instructions = self._parse_instructions(instructions)

    def _parse_instructions(self, instructions):
        result = []
        for instruction in instructions:
            if instruction == INSTRUCTION_RIGHT:
                result.append(TurnMowerToRight(self._mower))
            if instruction == INSTRUCTION_LEFT:
                result.append(TurnMowerToLeft(self._mower))
            if instruction == INSTRUCTION_FORWARD:
                result.append(MoveMowerForward(self._mower))

        return result

    def _check_valid_instructions(self, introduced_instructions):
        valid_instruction = 'RLM'
        contains_valid_instructions = all(instruction in valid_instruction for instruction in introduced_instructions)
        if not contains_valid_instructions:
            raise InvalidInstructionForMowerException

    @property
    def mower(self):
        return self._mower

    @property
    def instructions(self):
        return self._instructions
