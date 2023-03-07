import sys
import argparse
import glob
from subprocess import run
from pathlib import Path


def find_input_files(working_directory: str, recursive: bool):
    if recursive:
        return glob.glob(f'{working_directory}/**/*.ui', recursive=True)
    else:
        return glob.glob(f'{working_directory}/*.ui', recursive=True)


def compile(working_dir: Path, recursive: bool):
    input_files = find_input_files(working_dir, recursive)

    for input_file in input_files:
        input_file_path = Path(input_file)
        output_file_path = input_file_path.with_suffix('.py')
        print(f'{input_file_path} -> {output_file_path}')
        run(['pyside6-uic', '-o', output_file_path, input_file_path])


def start():
    parser = argparse.ArgumentParser(description='pyside6-uic-extended')
    parser.add_argument('working_directory', metavar='working_directory', type=str,
                        help='Directory to search for .ui files.')
    parser.add_argument('-r', dest='recursive', action='store_true',
                        help='Search recursively for .ui files')
    args = parser.parse_args(sys.argv[1:])

    print(args.working_directory)
    print(args.recursive)
    compile(args.working_directory, args.recursive)


if __name__ == '__main__':
    start()
