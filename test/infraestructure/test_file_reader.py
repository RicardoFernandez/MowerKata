from src.infraestructure.file_reader import FileReader


class TestFileReader:

    def test_file_reader_handles_correctly_txt_info(self, tmpdir):
        fake_dir = tmpdir.mkdir("fake_dir")
        fake_dir.join("testfile.txt").write('5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM')
        path_to_file = str(fake_dir) + '/testfile.txt'
        readed_content = FileReader(path_to_file).read()
        assert readed_content == ['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM']