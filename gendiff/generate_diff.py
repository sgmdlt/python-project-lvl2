from itertools import chain
import json


def parse_files(path_to_first_file, path_to_second_file):
    first = json.load(open(path_to_first_file)) 
    second = json.load(open(path_to_second_file))
    return (first, second)


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


def sort_(diff):
    order = {
    'removed': 1,
    'added': 2,
    'kept': 3,
    }
    diff = sorted(diff, key=lambda pair: order.get(pair[1]))
    diff = sorted(diff, key=lambda pair: pair[0])
    return diff


def format_(diff, old, new, indents=2, order=sort_):
    result = []
    view = '{ind}{sign} {key}: {value}'.format
    signs = {
    'removed': '-',
    'added': '+',
    'kept': ' ',
    }
    ind = ' ' * indents

    for key, state in order(diff):
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
    return format_(get_diff(first, second), first, second)