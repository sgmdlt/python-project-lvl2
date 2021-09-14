from gendiff.differ import get_diff
from gendiff.formaters.formaters import DEFAULT_STYLE, format_output
from gendiff.parsers import parse_files


def generate_diff(first_file, second_file, style=DEFAULT_STYLE):
    first, second = parse_files(first_file, second_file)
    diff = get_diff(first, second)
    return format_output(diff, style)
