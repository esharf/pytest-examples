import pytest


'''You can skip the whole module (comment this to see the other skip types)'''
pytest.skip("skipping test_skip_module_x tests", allow_module_level=True)


'''Using a marker'''


@pytest.mark.skip
def test_conditional_skip():
    raise Exception('this test is skipped')


@pytest.mark.skipif(True, reason='this test because of the condition.')
def test_conditional_skip():
    raise Exception('this test because of the condition.')


skip = pytest.mark.skipif(True, reason='this test because of the condition.')


@skip
def test_skip():
    raise Exception('this test because of the @skip decorator.')


'''Using pytest.skip()'''


def test_skip_inside():
    pytest.skip()
