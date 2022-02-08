import pytest
from some_functions import add


'''Use a marker'''

data_test_with_parametrize = [
    (2, 3, 5),
    (3, 3, 6),
    (2.5, 3, 5.5),
    (2.3, 3.2, 5.5),
]


@pytest.mark.parametrize('a,b,expected_value', data_test_with_parametrize)
def test_with_parametrize(a, b, expected_value):
    assert expected_value == add(a, b)


@pytest.mark.skip
def test_skip():
    raise Exception('this test is skipped for some reason')


'''Using your own marker'''


@pytest.mark.dont_run_this_test
def test_dont_run_this_test():
    '''Take a look on the pytest args in .vscode/settings.json'''
    raise Exception('this test sould not run')


@pytest.mark.dont_run_this_test
@pytest.mark.force_run_this_test
def test_force_run_this_test():
    '''Take a look on the pytest args in .vscode/settings.json'''
    print('this test is running')


@pytest.mark.run_in('../')
def test_open_file_with_parent_dir_path():
    from pathlib import Path
    assert Path('./pytest-examples/Pipfile').exists()
