from src.domain.models.mower_movements import MowerMovements
from src.domain.models.mower import Mower


class MowerMovementsParser:
    def __init__(self, plateau):
        self._plateau = plateau

    def parse(self, commands):
        initial_positions_with_movements = commands[:0] + commands[0+1:]
        breakpoint()
        mowers_with_movements = (
            [
                MowerMovements(Mower(self._plateau, initial_positions_with_movements[element]), initial_positions_with_movements[element + 1])
                for element in range(0, len(initial_positions_with_movements), 2)
            ]
        )
        return mowers_with_movements

