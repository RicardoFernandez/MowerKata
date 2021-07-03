from dataclasses import dataclass

from src.domain.models.mower import Mower


@dataclass
class MowerMovements:

    mower: Mower
    movements: str

    def __init__(self, mower, movements):
        self.mower = mower
        self.movements = movements

