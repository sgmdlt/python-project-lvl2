import pytest
import os
from gendiff.generate_diff import generate_diff

PLAIN_EXPECTED = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


PLAIN_FILES = {
    'plain_files_default_output': ('file1.json', 'file2.json', '', None, PLAIN_EXPECTED),
}


NESTED_FILES = {
    'nested_files_default_output': ('file1.json', 'file2.yml', 'nested', None, 'stylish_diff.txt'),
    'nested_files_plain_output': ('file1.yaml', 'file2.json', 'nested', 'plain', 'plain_diff.txt'),
    'nested_files_json_output': ('file1.json', 'file2.yml', 'nested', 'json', 'json_diff.txt'),
}


def get_fixture_path(file_name, directory=''):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', directory, file_name)


@pytest.mark.parametrize(
    "first_file, second_file, dir, style, output",
    PLAIN_FILES.values(),
    ids=PLAIN_FILES.keys(),
)
def test_plain_files(first_file, second_file, dir, style, output):
    file1 = get_fixture_path(first_file, dir)
    file2 = get_fixture_path(second_file, dir)
    assert generate_diff(file1, file2, style) == output


@pytest.mark.parametrize(
    "first_file, second_file, dir, style, output",
    NESTED_FILES.values(),
    ids=NESTED_FILES.keys(),
)
def test_nested_files(first_file, second_file, dir, style, output):
    file1 = get_fixture_path(first_file, dir)
    file2 = get_fixture_path(second_file, dir)
    output_file = open(get_fixture_path(output, dir), 'r').read()
    assert generate_diff(file1, file2, style) == output_file


def test_wrong_file_format():
    with pytest.raises(RuntimeError, match=r'format'):
        generate_diff(get_fixture_path('file1.doc'), get_fixture_path('file2.json'))
