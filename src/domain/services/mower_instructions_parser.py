from src.domain.models.mower.mower import Mower
from src.domain.models.mower.mower_instructions import MowerInstructions


class MowerInstructionsParser:
    def __init__(self, plateau):
        self._plateau = plateau

    def parse(self, commands):
        commands_without_plateau = commands[:0] + commands[0+1:]
        mowers_with_movements = (
            [
                MowerInstructions(Mower(self._plateau, commands_without_plateau[element]), commands_without_plateau[element + 1])
                for element in range(0, len(commands_without_plateau), 2)
            ]
        )
        return mowers_with_movements


