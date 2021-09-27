import argparse

from gendiff.formaters.formaters import DEFAULT_STYLE, FORMATERS


def get_cli_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate diff',
    )
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output (default: {0})'.format(DEFAULT_STYLE),
        choices=FORMATERS,
        default=DEFAULT_STYLE,
    )
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
