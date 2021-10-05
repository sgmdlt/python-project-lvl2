from gendiff.formaters.json import json_format
from gendiff.formaters.plain import to_format as plain_format
from gendiff.formaters.stylish import to_format as stylish_format

FORMATERS = {  # noqa: WPS407
    'stylish': stylish_format,
    'plain': plain_format,
    'json': json_format,
}


def format_output(diff, style):
    message = 'Wrong output format: {f}. Supported formats: {sup}'.format  # noqa: E501
    try:
        style = FORMATERS[style]
    except KeyError:
        raise RuntimeError(message(f=style, sup=FORMATERS))
    return style(diff)
