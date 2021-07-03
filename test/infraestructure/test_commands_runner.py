import pytest

from src.infraestructure.commands_runner import CommandsRunner


class TestCommandsRunner:

    @pytest.fixture
    def new_mower_input_command(self):
        return ['5 5', '1 2 N', 'R']

    def test_mower_rotates_to_right(self, new_mower_input_command):
        final_coordinates = CommandsRunner().execute(new_mower_input_command)

        assert final_coordinates == ['1 2 E']
