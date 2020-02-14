import pytest


def setup_function():
    print('setup_function()...')


def setup_module():
    print('setup_module()...')


def setup():
    print('setup()...')

def teardown_function():
    print('teardown_function()...')


def teardown_module():
    print('teardown_module()...')


def teardown():
    print('teardown()...')


def test_func1():
    print('this is a testcase1')


class Testcasedm:
    def test_func1(self):
        print('this is a testcase1...in class')

    def setup(self):
        print('setup()...in class')

    def setup_method(self):
        print('setup_method()...in class')

    def setup_class(self):
        print('setup_class()...in class')

    def teardown(self):
        print('teardown()...in class')

    def teardown_method(self):
        print('teardown_method()...in class')

    def teardown_class(self):
        print('teardown_class()...in class')


if __name__ == '__main__':
    pytest.main(['-v', 'pytestdemo1.py', '--html=report.html'])