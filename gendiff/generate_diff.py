from gendiff.formaters.plain import plain
from gendiff.formaters.stylish import stylish
from gendiff.parsers import parse_files

FORMATERS = {  # noqa: WPS407
    'stylish': stylish,
    'plain': plain,
}

DEFAULT_STYLE = 'stylish'


def get_diff(old, new):  # noqa: WPS210
    diff = {}
    removed = old.keys() - new.keys()
    added = new.keys() - old.keys()
    kept = new.keys() & old.keys()

    for k_key in kept:
        old_k_value = old[k_key]
        new_k_value = new[k_key]
        if isinstance(old_k_value, dict) and isinstance(new_k_value, dict):
            diff[(k_key, 'nested')] = get_diff(old_k_value, new_k_value)

        elif old_k_value == new_k_value:
            diff[(k_key, 'unchanged')] = old_k_value

        else:
            diff[(k_key, 'changed')] = {
                'old_value': old_k_value,
                'new_value': new_k_value,
            }

    for r_key in removed:
        diff[(r_key, 'removed')] = old[r_key]
    for a_key in added:
        diff[(a_key, 'added')] = new[a_key]

    return diff  # { (key, state): value }


def generate_diff(first_file, second_file, style=DEFAULT_STYLE):
    first, second = parse_files(first_file, second_file)
    diff = get_diff(first, second)
    style = FORMATERS.get(style)
    return style(diff)
