from gendiff.formaters.json import json_format
from gendiff.formaters.plain import plain_format
from gendiff.formaters.stylish import stylish_format

FORMATERS = {  # noqa: WPS407
    'stylish': stylish_format,
    'plain': plain_format,
    'json': json_format,
}

DEFAULT_FORMAT = 'stylish'


def format_output(diff, style=DEFAULT_FORMAT):
    style = FORMATERS.get(style) or FORMATERS.get(DEFAULT_FORMAT)
    return style(diff)
