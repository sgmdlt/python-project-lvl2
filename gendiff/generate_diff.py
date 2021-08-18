from itertools import chain
from operator import itemgetter
import json


def parse_files(first_file, second_file):
    return json.load(open(first_file)), json.load(open(second_file))


def get_diff(old, new):
    diff = set()
    removed = old.keys() - new.keys()
    added = new.keys() - old.keys()
    kept = new.keys() & old.keys()
    
    for key in kept:
        if old.get(key) != new.get(key):
            diff.add((key, 'removed'))
            diff.add((key, 'added'))
        else:
            diff.add((key, 'kept'))
    for key in removed:
        diff.add((key, 'removed'))
    for key in added:
        diff.add((key, 'added'))
    
    return diff


def _sort(diff):
    order = {
    'removed': 1,
    'added': 2,
    'kept': 3,
    }
    diff = sorted(diff, key=lambda pair: order.get(pair[1]))
    diff = sorted(diff, key=lambda pair: pair[0])
    return diff


def format_(diff, old, new, indents=2, sort=_sort):
    result = []
    view = '{ind}{sign} {key}: {value}'.format
    signs = {
    'removed': '-',
    'added': '+',
    'kept': ' ',
    }
    ind = ' ' * indents

    for key, state in sort(diff):
        sign = signs.get(state)
        if state == 'removed':
            value = old.get(key)
        elif state == 'added':
            value = new.get(key)
        elif state == 'kept':
            value = new.get(key)
        result.append(view(ind=ind, sign=sign, key=key, value=value))
    result = chain('{', result, '}')
    
    return '\n'.join(result)


def generate_diff(first_file, second_file):
    first, second = parse_files(first_file, second_file)
    diff = get_diff(first, second)
    return format(diff, first, second)