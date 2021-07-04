from unittest.mock import patch

from src.application.commands_runner import CommandsRunner
from src.infraestructure.file_reader import FileReader


class TestCommandsRunner:

    def test_mowers_reach_desired_state(self):
        with patch.object(FileReader, 'read') as reader_mock:
            reader_mock.return_value = ['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM']
            final_coordinates = CommandsRunner(FileReader('fake_path')).execute()

        assert final_coordinates == ['1 3 N', '5 1 E']

    def test_invalid_instruction_message_is_returned_for_invalid_instructions(self):
        with patch.object(FileReader, 'read') as reader_mock:
            reader_mock.return_value = ['5 5', '1 2 N', 'LXX']
            result = CommandsRunner(FileReader('fake_path')).execute()

        assert result == ['Invalid instruction for mower was sent!']

    def test_mower_out_of_bounds_is_returned_for_invalid_initial_position(self):
        with patch.object(FileReader, 'read') as reader_mock:
            reader_mock.return_value = ['5 5', '6 6 N', 'LRR']
            result = CommandsRunner(FileReader('fake_path')).execute()

        assert result == ['Invalid initial position was set for a mower, check the size of plateau']
