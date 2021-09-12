#!/usr/bin/env python
import argparse

from gendiff.generate_diff import DEFAULT_STYLE, FORMATERS, generate_diff


def main():
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
        choices=list(FORMATERS),
        default=DEFAULT_STYLE,
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
