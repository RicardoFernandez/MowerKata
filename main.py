from src.infraestructure.console_output import ConsoleOutput
from src.application.commands_runner import CommandsRunner
from src.infraestructure.file_reader import FileReader


def main(args):

    data = CommandsRunner(FileReader(args)).execute()
    ConsoleOutput().print(data)


if __name__ == '__main__':
    import sys
    main(sys.argv[1])