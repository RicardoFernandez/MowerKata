import pytest

from src.domain.models.mower.mower import Mower
from src.domain.models.plateau.plateau import Plateau


@pytest.fixture
def plateau():
    return Plateau('5 5')


@pytest.fixture
def mower_facing_north(plateau):
    return Mower(plateau, '1 1 N')
