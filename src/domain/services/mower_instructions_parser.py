from src.domain.models.mower.mower import Mower
from src.domain.models.mower.mower_instructions import MowerInstructions


class MowerInstructionsParser:
    def __init__(self, plateau):
        self._plateau = plateau

    def parse(self, commands):
        initial_positions_with_movements = commands[:0] + commands[0+1:]
        mowers_with_movements = (
            [
                MowerInstructions(Mower(self._plateau, initial_positions_with_movements[element]), initial_positions_with_movements[element + 1])
                for element in range(0, len(initial_positions_with_movements), 2)
            ]
        )
        return mowers_with_movements


