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


def jsonify(elem, depth):
    if not isinstance(elem, dict):
        return json.JSONEncoder().encode(elem)
    acc = []
    deep_ind = ' ' * depth
    view = '{ind} {key}: {value}'.format
    for key, value in elem.items():
        acc.append(view(
            ind=' ' * depth,
            key=key,
            value=jsonify(value, depth=depth + 2)
            ))
    result = chain('{', acc, [deep_ind +'}'])       
    return '\n'.join(result)


def format_(diff, depth=2, order=sort_):
    result = []
    view = '{ind}{sign} {key}: {value}'.format
    signs = {
        'removed': '-',
        'added': '+',
        'kept': ' ',
        'nested': ' ',
    }
    
    deep_ind = ' ' * depth
    for key, state in sort_(diff):
        value = diff.get((key, state))
        if state == 'nested':
            value = format_(value, depth=depth+2)
        
        result.append(view(
            ind=' ' * depth,
            sign=signs.get(state),
            key=key,
            value=jsonify(value, depth + 2),
        ))
    result = chain('{', result, [deep_ind +'}'])   
    
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
