STATE = 'state'
ADDED = 'added'
REMOVED = 'removed'
NESTED = 'nested'
CHANGED = 'changed'
UNCHAGED = 'unchanged'
VALUE = 'value'
OLD_VALUE = 'old_value'
NEW_VALUE = 'new_value'


def get_diff(old, new):  # noqa: WPS210
    diff = {}
    removed = old.keys() - new.keys()
    added = new.keys() - old.keys()
    kept = new.keys() & old.keys()

    for k_key in kept:
        old_k_value = old[k_key]
        new_k_value = new[k_key]
        if isinstance(old_k_value, dict) and isinstance(new_k_value, dict):
            diff[k_key] = {
                STATE: NESTED,
                VALUE: get_diff(old_k_value, new_k_value),
            }
        elif old_k_value == new_k_value:
            diff[k_key] = {
                STATE: UNCHAGED,
                VALUE: old_k_value,
            }
        else:
            diff[k_key] = {
                STATE: CHANGED,
                OLD_VALUE: old_k_value,
                NEW_VALUE: new_k_value,
            }

    for r_key in removed:
        diff[r_key] = {
            STATE: REMOVED,
            VALUE: old[r_key],
        }

    for a_key in added:
        diff[a_key] = {
            STATE: ADDED,
            VALUE: new[a_key],
        }
    return diff  # { key: {state, value} }
