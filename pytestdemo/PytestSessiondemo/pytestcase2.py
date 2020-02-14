import pytest


def test_caseA(scope_module):
    print('this is a test_caseA in pytestcase2')


class TestCase:
    def test_caseB(self, scope_session, scope_class):
        print('this is a test_caseB in pytestcase2')
