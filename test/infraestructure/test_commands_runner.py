import pytest

from src.infraestructure.commands_runner import CommandsRunner


class TestCommandsRunner:

    def test_one_mower_reach_desired_state(self):
        mower_input_command = ['5 5', '1 2 N', 'LMLMLMLMM']

        final_coordinates = CommandsRunner().execute(mower_input_command)

        assert final_coordinates == ['1 3 N']

    def test_two_mower_reach_desired_state(self):
        mower_input_command = ['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM']

        final_coordinates = CommandsRunner().execute(mower_input_command)

        assert final_coordinates == ['1 3 N', '5 1 E']
