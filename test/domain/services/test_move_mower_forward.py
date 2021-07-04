from src.domain.services.move_mower_forward import MoveMowerForward


class TestMoveMowerForward:
    def test_move_mower_forward(self, mower_facing_north):
        MoveMowerForward(mower_facing_north).execute()

        assert mower_facing_north.current_state() == '1 2 N'
