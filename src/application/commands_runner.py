from src.domain.services.mower_instructions_parser import MowerInstructionsParser
from src.domain.models.plateau.plateau import Plateau


class CommandsRunner:
    def __init__(self, file_reader):
        self._file_reader = file_reader

    def execute(self):
        commands = self._file_reader.read()
        plateau = Plateau(commands[0])
        mowers_instructions = MowerInstructionsParser(plateau).parse(commands)
        mowers_state = []
        for mower_instructions in mowers_instructions:
            for instruction in mower_instructions.instructions:
                instruction.execute()

            mowers_state.append(mower_instructions.mower.current_state())
        return mowers_state