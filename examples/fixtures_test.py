import json

import pytest

'''Using a fixture'''


def test_stdout(capsys):
    print('hello')
    captured = capsys.readouterr()
    assert captured.out == "hello\n"


'''Using your own fixture'''


class MyClass:
    def __init__(self, some_value):
        self.some_value = some_value


@pytest.fixture
def my_class():
    return MyClass('this is some value')


def test_some_value(my_class):
    assert my_class.some_value == 'this is some value'


'''Using your own fixture along with other fixtures'''


@pytest.fixture
def create_json_file(tmp_path):
    the_temp_json = tmp_path / 'test.json'
    the_temp_json.write_text('{"test": "test"}')
    return the_temp_json


def test_with_your_fixture(create_json_file):
    with open(create_json_file, 'r') as json_file:
        data = json.load(json_file)
    assert data['test'] == 'test'
