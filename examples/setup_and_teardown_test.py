from pathlib import Path


'''Setup and tear down a module'''


def setup_module(module):
    global SETUP_MODULE
    SETUP_MODULE = 'SETUP_MODULE'


def teardown_module(module):
    global SETUP_MODULE
    del SETUP_MODULE


def test_setup_module():
    global SETUP_MODULE
    assert SETUP_MODULE == 'SETUP_MODULE'


'''Setup and tear down a function'''


def setup_function():
    global SETUP_FUNCTION
    SETUP_FUNCTION = 'SETUP_FUNCTION_1'


def test_setup_function_1():
    global SETUP_FUNCTION
    assert SETUP_FUNCTION == 'SETUP_FUNCTION_1'


def teardown_function():
    global SETUP_FUNCTION
    del SETUP_FUNCTION


def setup_function():
    global SETUP_FUNCTION
    SETUP_FUNCTION = 'SETUP_FUNCTION_2'


def test_setup_function_1():
    global SETUP_FUNCTION
    assert SETUP_FUNCTION == 'SETUP_FUNCTION_2'


def teardown_function():
    global SETUP_FUNCTION
    del SETUP_FUNCTION


'''Setup and tear down a class'''


class TestWithClassSetupAndTeardon:
    @classmethod
    def setup_class(cls):
        cls.my_temp_file = Path('test.txt')
        cls.my_temp_file.write_text('hello world')

    @classmethod
    def teardown_class(cls):
        cls.my_temp_file.unlink()

    def test_start_with_hello(self):
        with open(self.my_temp_file, 'r') as test_file:
            assert test_file.read().startswith('hello')

    def test_ends_with_world(self):
        with open(self.my_temp_file, 'r') as test_file:
            assert test_file.read().endswith('world')


'''Setup and tear down for each function in a class'''


class TestWithSetupAndTearDownForEachTest:
    @classmethod
    def setup_class(cls):
        global TEST_COUNT
        TEST_COUNT = 0

    def setup(self):
        global TEST_COUNT
        TEST_COUNT += 1

    def teardown(self):
        global TEST_COUNT
        TEST_COUNT += 1

    def test_first(self):
        global TEST_COUNT
        assert TEST_COUNT == 1

    def test_second(self):
        global TEST_COUNT
        assert TEST_COUNT == 3

    def test_third(self):
        global TEST_COUNT
        assert TEST_COUNT == 5
