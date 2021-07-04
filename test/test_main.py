import io
import sys
from unittest.mock import patch

from main import main


class TestMain:

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mowers_execute_their_rutine_over_plateu(self, mock_stdout, tmpdir):
        fake_dir = tmpdir.mkdir("fake_dir")
        fake_dir.join("testfile.txt").write('5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM')
        path_to_file = str(fake_dir) + '/testfile.txt'
        sys.argv = [path_to_file]

        main(sys.argv[0])

        assert mock_stdout.getvalue() == '1 3 N\n5 1 E\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_error_is_displayed_for_invalid_instruction(self, mock_stdout, tmpdir):
        fake_dir = tmpdir.mkdir("fake_dir")
        fake_dir.join("testfile.txt").write('5 5\n1 2 N\nLMLZ\n3 3 E\nMMRMMRMRRM')
        path_to_file = str(fake_dir) + '/testfile.txt'
        sys.argv = [path_to_file]

        main(sys.argv[0])

        assert mock_stdout.getvalue() == 'Invalid instruction for mower was sent!\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_error_is_displayed_for_out_of_bounds_mower(self, mock_stdout, tmpdir):
        fake_dir = tmpdir.mkdir("fake_dir")
        fake_dir.join("testfile.txt").write('5 5\n6 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM')
        path_to_file = str(fake_dir) + '/testfile.txt'
        sys.argv = [path_to_file]

        main(sys.argv[0])

        assert mock_stdout.getvalue() == 'Invalid initial position was set for a mower, check the size of plateau\n'
