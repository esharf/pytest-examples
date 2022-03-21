import pytest

from src_files.some_functions import add, hello_world

'''Basic examples'''


def test_hello_world():
    hello_world()


def test_add():
    assert 5 == add(2, 3)


@pytest.mark.xfail      # explained in examples/markers_test.py
def test_fail():
    assert 5 == add(3, 3)


'''This is used to gather some tests that have somthing in common.'''


class TestClass:

    def test_add_with_ints(self):
        assert 5 == add(2, 3)

    def test_add_with_floats(self):
        assert 5.5 == add(3.0, 2.5)

    def test_add_with_multiple_types(self):
        assert 5.5 == add(3, 2.5)
