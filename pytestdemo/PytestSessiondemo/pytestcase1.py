import pytest


def test_caseA(scope_module, scope_function):
    print('this is a test_caseA in pytestcase1')


class TestCase:
    def test_caseB(self, scope_module, scope_session):
        print('this is a test_caseB in pytestcase1')


if __name__ == '__main__':
    pytest.main(['-s', 'pytestcase1.py', 'pytestcase2.py'])