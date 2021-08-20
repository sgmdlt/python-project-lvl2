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
def files():
    file1 = PATH + 'file1.json'
    file2 = PATH + 'file2.json'
    yield (file1, file2)


def test_generate_diff(files):
    first, second = files
    assert generate_diff(first, second) == RESULT