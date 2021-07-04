import io
from unittest.mock import patch

from src.infraestructure.console_output import ConsoleOutput


class TestConsoleOutput:

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_console_prints_final_mower_state_per_line(self, mock_stdout):
        mowers_final_state = ['1 3 N', '5 1 E']
        ConsoleOutput().print(mowers_final_state)

        assert mock_stdout.getvalue() == '1 3 N\n5 1 E\n'