from gendiff.differ import get_diff
from gendiff.formaters.formaters import format_output
from gendiff.io import data_and_format
from gendiff.parsers import parse_data

DEFAULT_FORMAT = 'stylish'


def generate_diff(first_path, second_path, style=DEFAULT_FORMAT):
    first_data, first_format = data_and_format(first_path)
    second_data, second_format = data_and_format(second_path)
    diff = get_diff(
        parse_data(first_data, first_format),
        parse_data(second_data, second_format),
    )
    return format_output(diff, style)
