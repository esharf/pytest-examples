import os


def pytest_runtest_setup(item):
    for mark in item.iter_markers(name="run_in"):
        mark.kwargs['original'] = os.getcwd()
        os.chdir(mark.kwargs.get('run_in') or mark.args[0])


def pytest_runtest_teardown(item):
    for mark in item.iter_markers(name="test_args"):
        os.chdir(mark.kwargs['original'])
