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
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return str(value)


#def format_value(elem, deep_indent_size, deep_indent):
#    if not isinstance(elem, dict):
#        return jsonify(elem)
#    acc = []
#    print('deep_ind_size = ', deep_indent_size)
#    current_indent_size = deep_indent_size
#    current_indent = current_indent_size * '#'
#    deep_indent_size += 4
#    deep_indent = deep_indent_size * '*'
#    view = '{ind}{key}: {value}'.format
#    for key, value in elem.items():
#        acc.append(view(
#            ind=deep_indent,
#            key=key,
#            value=format_value(value, deep_indent_size, deep_indent)
#            ))
#    result = chain('{', acc, [current_indent +'}'])
#    return '\n'.join(result)
#


def format_value(tree, spaces_count=2, order=sort_):
    view = '{ind}{key}: {value}'.format
    step = spaces_count
    
    def walk(node, count):
        if not isinstance(node, dict):
            return jsonify(node)
         
        line = []
        replacer = ' '
        
        for key, value in node.items():
            line.append(view(
                ind=replacer * (count + 4),
                key=key,
                value=walk(value, count + 4)
            ))
        result = chain('{', line, [(count) * replacer + '}'])
        return '\n'.join(result)
    return walk(tree, spaces_count)


def format_(tree, spaces_count=2, order=sort_):
    view = '{ind}{sign} {key}: {value}'.format
    signs = {
         'removed': '-',
         'added': '+',
         'kept': ' ',
         'nested': ' ',
     }
    step = spaces_count
    
    def walk(node, count):

        line = []
        replacer = ' '
        
        for key, state in order(node):
            value = node.get((key, state))
            if state == 'nested':
                value = format_(value, count + 4)
            
            line.append(view(
                ind=replacer * count,
                sign = signs.get(state),
                key=key,
                value = format_value(value, count + 2)
            ))
        result = chain('{', line, [(count - 2) * replacer + '}'])
        return '\n'.join(result)
    return walk(tree, spaces_count)
 
 
#def format_(diff, depth = 0, order=sort_):
#    result = []
#    view = '{ind}{sign} {key}: {value}'.format
#    signs = {
#        'removed': '-',
#        'added': '+',
#        'kept': ' ',
#        'nested': ' ',
#    }
#    replacer = ' '
#    deep_indent_size = depth + 2
#    deep_indent = replacer * deep_indent_size
#    current_indent = replacer * depth
#    for key, state in order(diff):
#        value = diff.get((key, state))
#        if state == 'nested':
#            deep_indent_size = depth + 4
#            value = format_(value, depth=deep_indent_size)
#            
#        result.append(view(
#            ind=deep_indent,
#            sign=signs.get(state),
#            key=key,
#            value=format_value(value, deep_indent_size + 2),
#        ))
#    result = chain('{', result, [current_indent +'}'])
#    
#    return '\n'.join(result)
