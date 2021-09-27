import json

import yaml

PARSERS = {  # noqa: WPS407
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
}


def parse_data(data, extension):
    parser = PARSERS.get(extension)
    return parser(data)
