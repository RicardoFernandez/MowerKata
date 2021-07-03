import pytest

from src.infraestructure.commands_runner import CommandsRunner


class TestCommandsRunner:

    @pytest.fixture
    def new_mower_input_command(self):
        return ['5 5', '1 2 N', 'LMLMLMLMM']

    def test_mower_reach_desired_state(self, new_mower_input_command):
        final_coordinates = CommandsRunner().execute(new_mower_input_command)

        assert final_coordinates == ['1 3 N']

