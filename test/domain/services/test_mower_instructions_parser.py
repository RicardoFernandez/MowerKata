from src.domain.services.move_mower_forward import MoveMowerForward
from src.domain.services.turn_mower_to_right import TurnMowerToRight
from src.domain.services.mower_instructions_parser import MowerInstructionsParser


class TestMowerInstructionsParser:
    def test_mower_instructions_parser_return_correct_mowers_and_related_movements(self, plateau):
        commands = ['5 5', '1 2 N', 'RM']

        instructions_for_mower = MowerInstructionsParser(plateau).parse(commands)

        assert instructions_for_mower[0].mower.current_state() == '1 2 N'
        assert len(instructions_for_mower[0].instructions) == 2
        assert isinstance(instructions_for_mower[0].instructions[0], TurnMowerToRight)
        assert isinstance(instructions_for_mower[0].instructions[1], MoveMowerForward)