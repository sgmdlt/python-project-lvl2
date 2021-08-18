from itertools import chain
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


def format_(diff, old, new, indents=2):
    result = []
    view = '{ind}{sign} {key}: {value}'.format
    signs = {
    'removed': '-',
    'added': '+',
    'kept': ' ',
    }
    ind = ' ' * indents

    for key, state in sorted(diff, key = lambda x: x[0]):
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