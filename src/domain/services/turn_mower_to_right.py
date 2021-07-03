class TurnMowerToRight:
    def __init__(self, mower):
        self._mower = mower

    def execute(self):
        self._mower.turn_right()
