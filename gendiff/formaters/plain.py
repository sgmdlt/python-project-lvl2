def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    translation = {
        None: 'null',
        False: 'false',
        True: 'true',
    }
    return translation.get(value, "'{0}'".format(value))


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


def plain(diff, path=None):
    if path is None:
        path = []

    result = []
    for key, state in sorted(diff):
        path.append(key)
        if state == 'nested':
            result.append(plain(diff.get((key, state)), path))

        value = diff.get((key, state))
        if state == 'changed':
            old_value = format_value(value['old_value'])
            new_value = format_value(value['new_value'])
            line = make_line(state, path, old_value, new_value)
        else:
            value = format_value(value)
            line = make_line(state, path, value=value)
        path.pop()
        result.append(line)
    return '\n'.join(line for line in result if line)
