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


def get_fixture_path(file_name, directory=''):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', directory, file_name)


@pytest.fixture
def plain_jsons():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    yield (file1, file2)


@pytest.fixture
def plain_yamls():
    file1 = get_fixture_path('file1.yaml')
    file2 = get_fixture_path('file2.yml')
    yield (file1, file2)


@pytest.fixture
def nested_jsons():
    file1 = get_fixture_path('file1.json', 'nested')
    file2 = get_fixture_path('file2.json', 'nested')
    yield (file1, file2)


@pytest.fixture
def nested_yamls():
    file1 = get_fixture_path('file1.yaml', 'nested')
    file2 = get_fixture_path('file2.yml', 'nested')
    yield (file1, file2)


@pytest.fixture
def stylish_output():
    yield open(get_fixture_path('stylish_diff.txt', 'nested'), 'r').read()


@pytest.fixture
def plain_output():
    yield open(get_fixture_path('plain_diff.txt', 'nested'), 'r').read()


def test_plain_jsons(plain_jsons):
    first, second = plain_jsons
    assert generate_diff(first, second) == PLAIN_EXPECTED


def test_plain_yamls(plain_yamls):
    first, second = plain_yamls
    assert generate_diff(first, second) == PLAIN_EXPECTED


def test_stylish_formater(nested_jsons, nested_yamls, stylish_output):
    first_json, second_json = nested_jsons
    first_yaml, second_yaml = nested_yamls
    assert generate_diff(first_json, second_json) == stylish_output
    assert generate_diff(first_yaml, second_yaml) == stylish_output
    

def test_plain_formater(nested_jsons, nested_yamls, plain_output):
    first_json, second_json = nested_jsons
    first_yaml, second_yaml = nested_yamls
    assert generate_diff(first_json, second_json, style='plain') == plain_output
    assert generate_diff(first_yaml, second_yaml, style='plain') == plain_output
