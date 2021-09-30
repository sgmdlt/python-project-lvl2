from gendiff.differ import CHANGED, NESTED, NEW_VALUE, OLD_VALUE, STATE, VALUE


def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return "'{0}'".format(value)
    if value is None:
        return 'null'
    return '{0}'.format(value)


def make_line(state, path, old=None, new=None, value=None):
    path = '.'.join(path)
    if state == 'removed':
        line = "Property '{0}' was removed".format(path)
    elif state == 'changed':
        line = "Property '{0}' was updated. From {1} to {2}".format(path, old, new)  # noqa: E501
    elif state == 'added':
        line = "Property '{0}' was added with value: {1}".format(path, value)
    else:
        line = ''
    return line


def to_format(diff, path=None):
    if path is None:
        path = []
    result = []
    for key in sorted(diff):
        path.append(key)
        data = diff[key]
        state = data[STATE]

        if state == NESTED:
            result.append(to_format(data[VALUE], path))

        if state == CHANGED:
            old_value = to_str(data[OLD_VALUE])
            new_value = to_str(data[NEW_VALUE])
            line = make_line(state, path, old_value, new_value)
        else:
            value = to_str(data[VALUE])
            line = make_line(state, path, value=value)

        path.pop()
        result.append(line)
    return '\n'.join(line for line in result if line)
