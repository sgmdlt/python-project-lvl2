from gendiff.differ import get_diff
from gendiff.formaters.formaters import DEFAULT_STYLE, format_output
from gendiff.parsers import parse_data
from gendiff.reader import get_file


def generate_diff(first_path, second_path, style=DEFAULT_STYLE):
    first_data, first_format = get_file(first_path)
    second_data, second_format = get_file(second_path)
    diff = get_diff(
        parse_data(first_data, first_format),
        parse_data(second_data, second_format),
    )
    return format_output(diff, style)
