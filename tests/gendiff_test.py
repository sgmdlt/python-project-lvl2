import json
import os

import pytest
from gendiff.differ import get_diff
from gendiff.generate_diff import DEFAULT_FORMAT, generate_diff
from gendiff.io import data_and_format
from gendiff.parsers import parse_data

TEXT_OUTPUTS = {
    'plain_files_default_output': ('file1.json', 'file2.json', 'plain', DEFAULT_FORMAT, 'plain.txt'),
    'nested_files_default_output': ('file1.json', 'file2.yml', 'nested', DEFAULT_FORMAT, 'stylish_diff.txt'),
    'nested_files_plain_output': ('file1.yaml', 'file2.json', 'nested', 'plain', 'plain_diff.txt'),
}


def get_fixture_path(file_name, directory=''):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', directory, file_name)


@pytest.mark.parametrize(
    'first_file, second_file, dir, style, output',
    TEXT_OUTPUTS.values(),
    ids=TEXT_OUTPUTS.keys(),
)
def test_text_output(first_file, second_file, dir, style, output):
    file1 = get_fixture_path(first_file, dir)
    file2 = get_fixture_path(second_file, dir)
    with open(get_fixture_path(output, dir), 'r') as f:
        output_file = f.read()
    assert generate_diff(file1, file2, style) == output_file


@pytest.mark.parametrize(
    'first_file, second_file, dir, style',
    [('file1.json', 'file2.yml', 'nested', 'json')],
)
def test_json_output(first_file, second_file, dir, style):
    path1 = get_fixture_path(first_file, dir)
    path2 = get_fixture_path(second_file, dir)
    file1, extension1 = data_and_format(path1)
    file2, extension2 = data_and_format(path2)
    diff = get_diff(parse_data(file1, extension1), parse_data(file2, extension2))
    json_diff = generate_diff(path1, path2, style)
    assert json.loads(json_diff) == diff


def test_wrong_file_format():
    with pytest.raises(RuntimeError, match=r'format'):
        generate_diff(
            get_fixture_path('file1.doc', 'wrong'),
            get_fixture_path('file2.json', 'plain'),
        )


def test_wrong_output_format():
    with pytest.raises(RuntimeError, match=r'output'):
        generate_diff(
            get_fixture_path('file1.json', 'plain'),
            get_fixture_path('file2.json', 'plain'),
            style='no_style',
        )
