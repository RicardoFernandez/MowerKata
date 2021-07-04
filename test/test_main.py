import io
import sys
from unittest.mock import patch

from main import main


class TestMain:

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mowers_execute_their_rutine_over_plateu(self, mock_stdout):
        sys.argv = ["./instructions.txt"]
        main(sys.argv[0])

        assert mock_stdout.getvalue() == '1 3 N\n5 1 E\n'
