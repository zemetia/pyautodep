import argparse
import os
import pypisearch

from pyautodep import PyAutoDep


def main():
    """Main program entrypoint."""

    # Get command arguments
    parser = argparse.ArgumentParser(
        description="Check every single imported python module(s) on your project and install it automatically"
    )
    parser.add_argument(
        "-t",
        "--type",
        metavar="type",
        type=str,
        help="Search all imported python library from file or directory | -f (file | dir)"
    )

    parser.add_argument(
        "-p",
        "--path",
        default=".",
        metavar="path",
        type=str,
        help="The relative path of file / directory",
    )

    parser.add_argument(
        "-i",
        "--install",
        action="store_true",
        help="Install the missing dist"
    )

    args = parser.parse_args()

    type = args.type
    path = args.path

    module_path = os.getcwd()
    pad = PyAutoDep(module_path)

    if type == 'dir' or type == 'folder':
        pad.from_dir(path, args.install)

    elif type == 'file':
        pad.from_file(path, args.install)

    else:
        print('Give the argument..')
        print(
            '~ python -m pyautodep --file [file_name].py \n',
            '~ python -m pyautodep --dir [dir_name] \n')
        print('For example : ')
        print('~ python reqpip.py --file test.py')
        print('~ python reqpip.py --dir .')


if __name__ == "__main__":
    main()
