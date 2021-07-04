from src.domain.services.turn_mower_to_right import TurnMowerToRight


class TestTurnMowerToRight:
    def test_mower_turn_to_right(self, mower_facing_north):
        TurnMowerToRight(mower_facing_north).execute()

        assert mower_facing_north._facing_to == 'E'
