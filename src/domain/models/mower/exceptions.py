class InvalidInstructionForMowerException(Exception):
    def __init__(self):
        self.message = 'Invalid instruction for mower was sent!'


class MowerOutOfBoundsException(Exception):
    def __init__(self):
        self.message = 'Invalid initial position was set for a mower, check the size of plateau'
