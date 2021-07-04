class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        text_file = open(f'{self.path}', 'r')
        lines = text_file.readlines()
        text_file.close()
        clean_lines = []
        for line in lines:
            clean_lines.append(line.rstrip('\n'))
        return clean_lines