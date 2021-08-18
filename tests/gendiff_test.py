import pytest
import json
from gendiff.generate_diff import format_, get_diff


RESULT = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

@pytest.fixture
def files():
    file1 = json.load(open('tests/fixtures/file1.json'))
    file2 = json.load(open('tests/fixtures/file2.json'))
    return (file1, file2)

def test_diff_keys(files):
    first, second = files
    assert format_(get_diff(first, second), first, second) == RESULT