import argparse
import os

from pyautodep import PyAutoDep


def main():
    """Main program entrypoint."""

    # Get command arguments
    parser = argparse.ArgumentParser(
        description="Check every single imported python module(s) on your project and install it automatically"
    )
    parser.add_argument(
        "-f",
        "--file",
        metavar="file",
        type=str,
        help="Search all imported python library on the file"
    )

    parser.add_argument(
        "-d",
        "--dir",
        default=".",
        metavar="dir",
        type=str,
        help="Search all imported python library on the directory and the branchs",
    )
    parser.add_argument(
        "-i",
        "--install",
        action="store_true"
    )

    args = parser.parse_args()

    dir = args.dir
    file = args.file

    module_path = os.getcwd()
    pad = PyAutoDep(module_path)

    if dir:
        # pad.from_dir(dir, args.install)
        pass
    elif file:
        pad.from_file(dir, args.install)
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
