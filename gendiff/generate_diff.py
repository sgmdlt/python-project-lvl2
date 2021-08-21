from gendiff.formaters.stylish import format_
from gendiff.parsers import parse_files


def get_diff(old, new):
    diff = {}
    removed = old.keys() - new.keys()
    added = new.keys() - old.keys()
    kept = new.keys() & old.keys()

    for k_key in kept:
        if isinstance(old[k_key], dict) and isinstance(new[k_key], dict):
            diff[(k_key, 'nested')] = get_diff(old[k_key], new[k_key])
        
        elif old[k_key] == new[k_key]:
            diff[(k_key, 'kept')] = old[k_key]
        
        else:
            diff[(k_key, 'removed')] = old[k_key]
            diff[(k_key, 'added')] = new[k_key]

    for r_key in removed:
        diff[(r_key, 'removed')] = old[r_key]
    for a_key in added:
        diff[(a_key, 'added')] = new[a_key]

    return diff  # { (key, state): value }


def generate_diff(first_file, second_file):
    first, second = parse_files(first_file, second_file)
    return format_(get_diff(first, second))
