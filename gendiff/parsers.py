import json

import yaml

PARSERS = (
    ('.json', lambda file: json.load(open(file))),
    ('.yaml', lambda file: yaml.safe_load(open(file))),
    ('.yml', lambda file: yaml.safe_load(open(file))),
)


def select_parser(filename):
    for extension, parser in PARSERS:
        if filename.endswith(extension):
            return parser


def parse_files(path_to_first_file, path_to_second_file):
    first_parser = select_parser(path_to_first_file)
    second_parser = select_parser(path_to_second_file)
    return (
        first_parser(path_to_first_file),
        second_parser(path_to_second_file),
    )
