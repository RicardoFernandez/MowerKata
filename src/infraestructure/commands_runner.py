from src.domain.models.mower import Mower
from src.domain.models.plateau import Plateau


class CommandsRunner:
    def execute(self, commands):
        plateau = Plateau(commands[0])
        mower = Mower(plateau, commands[1])
        desired_movements = commands[2]
        mowers_state = []

        for movement in desired_movements:
            if movement == 'R':
                mower.turn_right()

        mowers_state.append(mower.current_state())
        return mowers_state