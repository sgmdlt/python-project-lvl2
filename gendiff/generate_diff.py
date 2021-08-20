import json
from itertools import chain


def parse_files(path_to_first_file, path_to_second_file):
    with open(path_to_first_file) as first:
        first = json.load(first)
        with open(path_to_second_file) as second:
            second = json.load(second)
            return (first, second)


def get_diff(old, new):  # noqa:WPS210, WPS440
    diff = {}
    removed = old.keys() - new.keys()
    added = new.keys() - old.keys()
    kept = new.keys() & old.keys()

    for k_key in kept:
        if old[k_key] == new[k_key]:
            diff[(k_key, 'kept')] = old[k_key]
        else:
            diff[(k_key, 'removed')] = old[k_key]
            diff[(k_key, 'added')] = new[k_key]

    for r_key in removed:
        diff[(r_key, 'removed')] = old[r_key]
    for a_key in added:
        diff[(a_key, 'added')] = new[a_key]

    return diff  # { (key, state): value }


def _sort(diff):
    order = {
        'removed': 1,
        'added': 2,
        'kept': 3,
    }
    state_sorted = sorted(diff, key=lambda pair: order.get(pair[1]))
    return sorted(state_sorted, key=lambda pair: pair[0])


def jsonify(value):
    if not isinstance(value, str):
        value = json.JSONEncoder().encode(value)
    return value


def format_(diff, indents=2, order=_sort):  # noqa: WPS210
    result = []
    view = '{ind}{sign} {key}: {value}'.format
    signs = {
        'removed': '-',
        'added': '+',
        'kept': ' ',
    }

    for key, state in order(diff):
        value = jsonify(diff.get((key, state)))
        result.append(view(
            ind=' ' * indents,
            sign=signs.get(state),
            key=key,
            value=value,
        ))
    result = chain('{', result, '}')

    return '\n'.join(result)


def generate_diff(first_file, second_file):
    first, second = parse_files(first_file, second_file)
    return format_(get_diff(first, second))
