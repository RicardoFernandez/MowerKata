from src.domain.services.mower_movements_parser import MowerMovementsParser
from src.domain.models.mower import Mower
from src.domain.models.plateau import Plateau


class CommandsRunner:
    def execute(self, commands):

        plateau = Plateau(commands[0])
        mowers_movements = MowerMovementsParser(plateau).parse(commands)
        mowers_state = []
        for mower_movements in mowers_movements:
            for movement in mower_movements.movements:
                if movement == 'R':
                    mower_movements.mower.turn_right()
                if movement == 'L':
                    mower_movements.mower.turn_left()
                if movement == 'M':
                    mower_movements.mower.move_forward()

            mowers_state.append(mower_movements.mower.current_state())
        return mowers_state
