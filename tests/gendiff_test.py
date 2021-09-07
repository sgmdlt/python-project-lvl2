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
def expected():
    stylish = open(get_fixture_path('stylish_diff.txt', 'nested'), 'r').read()
    yield stylish


def test_plain_jsons(plain_jsons):
    first, second = plain_jsons
    assert generate_diff(first, second) == PLAIN_EXPECTED


def test_plain_yamls(plain_yamls):
    first, second = plain_yamls
    assert generate_diff(first, second) == PLAIN_EXPECTED


def test_nested_json(nested_jsons, expected):
    first, second = nested_jsons
    assert generate_diff(first, second) == expected


def test_nested_yamls(nested_yamls, expected):
    first, second = nested_yamls
    assert generate_diff(first, second) == expected 