from itertools import chain


def sort_diff(diff):
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


def format_value(tree, spaces_count=2):
    view = '{ind}{key}: {value}'.format
    step = 4

    def _walk(node, count):
        if not isinstance(node, dict):
            return jsonify(node)

        line = []
        replacer = ' '

        for key, value in node.items():
            line.append(view(
                ind=replacer * (count + step),
                key=key,
                value=_walk(value, count + step),
            ))
        result = chain('{', line, [count * replacer + '}'])
        return '\n'.join(result)
    return _walk(tree, spaces_count)


def format_(tree, spaces_count=2, order=sort_diff):
    view = '{ind}{sign} {key}: {value}'.format
    signs = {
        'removed': '-',
        'added': '+',
        'kept': ' ',
        'nested': ' ',
    }
    step = 4
    inner_step = step // 2
    replacer = ' '

    def _walk(node, count):

        line = []

        for key, state in order(node):
            value = node.get((key, state))

            if state == 'nested':
                value = format_(value, count + step)

            line.append(view(
                ind=replacer * count,
                sign=signs.get(state),
                key=key,
                value=format_value(value, count + inner_step),
            ))
        result = chain('{', line, [(count - inner_step) * replacer + '}'])
        return '\n'.join(result)
    return _walk(tree, spaces_count)
