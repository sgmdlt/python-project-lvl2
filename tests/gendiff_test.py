import pytest
from gendiff.generate_diff import generate_diff


RESULT = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

PATH = 'tests/fixtures/'

@pytest.fixture
def jsons():
    file1 = PATH + 'file1.json'
    file2 = PATH + 'file2.json'
    yield (file1, file2)


@pytest.fixture
def yamls():
    file1 = PATH + 'file1.yaml'
    file2 = PATH + 'file2.yml'
    yield (file1, file2)


@pytest.fixture
def jsons_nested():
    file1 = PATH + '/nested/file1.json'
    file2 = PATH + '/nested/file2.json'
    expected = PATH + '/nested/jsondiff.txt'
    yield (file1, file2, expected)


def test_plain_jsons(jsons):
    first, second = jsons
    assert generate_diff(first, second) == RESULT


def test_plain_yamls(yamls):
    first, second = yamls
    assert generate_diff(first, second) == RESULT


def test_nested_json(jsons_nested):
    first, second, expected = jsons_nested
    print(generate_diff(first, second))
    assert generate_diff(first, second) == open(expected, 'r').read()