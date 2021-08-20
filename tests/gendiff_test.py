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
def wrongs():
    file1 = PATH + 'file1.jpeg'
    file2 = PATH + 'file2.txt'
    yield (file1, file2)


def test_diff_jsons(jsons):
    first, second = jsons
    assert generate_diff(first, second) == RESULT


def test_diff_yamls(yamls):
    first, second = yamls
    assert generate_diff(first, second) == RESULT


#def test_wrong_file_format(wrongs):
#    first, second = wrongs
#    assert generate_diff(first, second) == 'wrong'