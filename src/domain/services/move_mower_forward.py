class MoveMowerForward:
    def __init__(self, mower):
        self._mower = mower

    def execute(self):
        self._mower.move_forward()