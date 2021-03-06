import pytest

from src.domain.models.mower.exceptions import (
    InvalidInstructionForMowerException, MowerOutOfBoundsException)
from src.domain.services.move_mower_forward import MoveMowerForward
from src.domain.services.mower_instructions_parser import \
    MowerInstructionsParser
from src.domain.services.turn_mower_to_right import TurnMowerToRight


class TestMowerInstructionsParser:
    def test_mower_instructions_parser_return_correct_mowers_and_related_movements(self, plateau):
        commands = ['5 5', '1 2 N', 'RM']

        instructions_for_mower = MowerInstructionsParser(plateau).parse(commands)

        assert instructions_for_mower[0].mower.current_state() == '1 2 N'
        assert len(instructions_for_mower[0].instructions) == 2
        assert isinstance(instructions_for_mower[0].instructions[0], TurnMowerToRight)
        assert isinstance(instructions_for_mower[0].instructions[1], MoveMowerForward)

    def test_exception_is_raised_for_invalid_movement(self, plateau):
        with pytest.raises(InvalidInstructionForMowerException):
            commands = ['5 5', '1 2 N', 'RXM']
            MowerInstructionsParser(plateau).parse(commands)

    def test_exception_is_raised_for_out_of_bounds_mower(self, plateau):
        with pytest.raises(MowerOutOfBoundsException):
            commands = ['5 5', '6 6 N', 'RXM']
            MowerInstructionsParser(plateau).parse(commands)