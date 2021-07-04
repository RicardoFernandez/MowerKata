from src.domain.services.turn_mower_to_left import TurnMowerToLeft


class TestTurnMowerToLeft:
    def test_mower_turn_to_left(self, mower_facing_north):
        TurnMowerToLeft(mower_facing_north).execute()

        assert mower_facing_north._facing_to == 'W'
