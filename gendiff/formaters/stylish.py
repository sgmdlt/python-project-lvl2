from itertools import chain

from gendiff.differ import (
    ADDED,
    CHANGED,
    NESTED,
    NEW_VALUE,
    OLD_VALUE,
    REMOVED,
    STATE,
    UNCHAGED,
    VALUE,
)


def to_str(value):
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
        REMOVED: '-',
        ADDED: '+',
        UNCHAGED: ' ',
        NESTED: ' ',
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
            return to_str(node)

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


def to_format(tree, spaces_count=2):
    step = 4
    inner_step = step // 2
    replacer = ' '

    def _walk(node, count):
        lines = []

        for key in sorted(node):
            data = node[key]
            state = data[STATE]
            value = data.get(VALUE)

            if state == NESTED:
                value = to_format(value, count + step)

            if state == CHANGED:
                old_value = format_value(data[OLD_VALUE], count + inner_step)
                lines.append(make_line(key, old_value, REMOVED, count))
                new_value = format_value(data[NEW_VALUE], count + inner_step)
                lines.append(make_line(key, new_value, ADDED, count))
                continue

            f_value = format_value(value, count + inner_step)
            lines.append(make_line(key, f_value, state, count))

        result = chain('{', lines, [(count - inner_step) * replacer + '}'])
        return '\n'.join(result)
    return _walk(tree, spaces_count)
