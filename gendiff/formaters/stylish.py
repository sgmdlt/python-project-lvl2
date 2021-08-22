import json

from itertools import chain


def sort_(diff):
    order = {
        'removed': 1,
        'added': 2,
        'kept': 3,
        'nested': 4,
    }
    sorted_diff = {}
    sort_states = sorted(diff, key=lambda pair: order.get(pair[1]))
    sort_names = sorted(sort_states, key=lambda pair: pair[0])
    for key in sort_names:
        sorted_diff[key] = diff[key]
    return sorted_diff


def jsonify(value):
    if value is None:
        return 'none'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return str(value)


def format_value(elem, deep_indent_size, deep_indent):
    if not isinstance(elem, dict):
        return jsonify(elem)
    acc = []
    print('deep_ind_size = ', deep_indent_size)
    current_indent = deep_indent
    deep_indent_size += 4
    deep_indent = deep_indent_size * ' '
    view = '{ind}  {key}: {value}'.format
    for key, value in elem.items():
        acc.append(view(
            ind=deep_indent,
            key=key,
            value=format_value(value, deep_indent_size, deep_indent)
            ))
    result = chain('{', acc, [current_indent +'}'])
    return '\n'.join(result)


def format_(diff, depth = 0, order=sort_):
    result = []
    view = '{ind}{sign} {key}: {value}'.format
    signs = {
        'removed': '-',
        'added': '+',
        'kept': ' ',
        'nested': ' ',
    }
    replacer = ' '
    deep_indent_size = depth + 2
    deep_indent = replacer * deep_indent_size
    current_indent = replacer * depth
    for key, state in order(diff):
        value = diff.get((key, state))
        if state == 'nested':
            deep_indent_size = depth + 4
            value = format_(value, depth=deep_indent_size)
            
        result.append(view(
            ind=deep_indent,
            sign=signs.get(state),
            key=key,
            value=format_value(value, deep_indent_size, deep_indent),
        ))
    result = chain('{', result, [current_indent +'}'])
    
    return '\n'.join(result)


#def format_(diff, spaces_count=1, order=_sort):
#    view = '{ind}{sign} {key}: {value}'.format
#    signs = {
#        'removed': '-',
#        'added': '+',
#        'kept': ' ',
#    }
#
#    def walk(node, depth):
#        if not isinstance(node, dict):
#            return jsonify(node)
#        
#        result = []
#        replacer = ' '
#        depth_size = depth + spaces_count
#        current_ind = depth * replacer
#        deep_ind = depth_size * replacer
#        
#        for key, state in order(node):
#            value = diff.get((key, state))
#
#            result.append(view(
#                ind=deep_ind,
#                sign=signs.get(state),
#                key=key,
#                value=walk(value, depth_size)
#            ))
#        result = chain('{', result, [current_ind + '}'])
#        return '\n'.join(result)
#
#    return walk(diff, 0)
