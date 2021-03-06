import pytest

from src_files.some_exceptions import ChildException, ParentException


def test_raise():
    with pytest.raises(Exception):
        raise Exception('this test should raise an exception.')


def test_raise_with_parent_xception():
    with pytest.raises(ParentException):
        raise ChildException('this test should raise an exception.')


@pytest.mark.xfail      # explained in examples/markers_test.py
def test_fail_with_unraised_exception():
    with pytest.raises(ParentException, match='this.+specific.+'):
        pass


'''You can also use regex to check the exception'''


def test_raise_with_message_match():
    with pytest.raises(ParentException, match='this.+specific.+'):
        raise ChildException('this test should raise a specific exception.')
