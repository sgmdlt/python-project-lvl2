from itertools import chain


def sort_diff(diff):
    order = {
        'removed': 1,
        'added': 2,
        'changed': 3,
        'unchanged': 4,
        'nested': 5,
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


def make_line(key, value, state, indent):
    view = '{ind}{sign} {key}: {value}'.format
    signs = {
        'removed': '-',
        'added': '+',
        'unchanged': ' ',
        'nested': ' ',
    }
    replacer = ' '
    return view(
        ind=replacer * indent,
        sign=signs.get(state),
        key=key,
        value=value,
    )


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


def format_stylish(tree, spaces_count=2, order=sort_diff):
    step = 4
    inner_step = step // 2
    replacer = ' '

    def _walk(node, count):
        lines = []

        for key, state in order(node):
            value = node.get((key, state))

            if state == 'nested':
                value = format_stylish(value, count + step)

            if state == 'changed':
                old_value = format_value(value['old_value'], count + inner_step)
                lines.append(make_line(key, old_value, 'removed', count))
                new_value = format_value(value['new_value'], count + inner_step)
                lines.append(make_line(key, new_value, 'added', count))
                continue

            value = format_value(value, count + inner_step)
            lines.append(make_line(key, value, state, count))

        result = chain('{', lines, [(count - inner_step) * replacer + '}'])
        return '\n'.join(result)
    return _walk(tree, spaces_count)
