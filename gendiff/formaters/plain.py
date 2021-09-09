#def sort_diff(diff):
#    order = {
#        'removed': 1,
#        'added': 2,
#        'unchanged': 3,
#        'changed': 4,
#        'nested': 5,
#    }
#    sorted_diff = {}
#    sort_states = sorted(diff, key=lambda pair: order.get(pair[1]))
#    sort_names = sorted(sort_states, key=lambda pair: pair[0])
#    for key in sort_names:
#        sorted_diff[key] = diff[key]
#    return sorted_diff


def make_line(state, path, old=None, new=None, value=None):
    path = '.'.join(path)
    if state == 'removed':
        line = 'Property {0} was removed'.format(path)
    elif state == 'changed':
        line = 'Propetry {0} was updated. From {1} to {2}'.format(path, old, new)  # noqa: E501
    elif state == 'added':
        line = 'Propetry {0} was added with value: {1}'.format(path, value)
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
            old_value = value['old_value']
            new_value = value['new_value']
            line = make_line(state, path, old_value, new_value)
        else:
            line = make_line(state, path, value=value)
        path.pop()
        result.append(line)
    return '\n'.join(line for line in result if line)
