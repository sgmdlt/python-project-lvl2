import argparse

from gendiff.formaters.formaters import DEFAULT_FORMAT, FORMATERS


def get_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate diff',
    )
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output (default: {0})'.format(DEFAULT_FORMAT),
        choices=FORMATERS,
        default=DEFAULT_FORMAT,
    )
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
