import pytest


@pytest.fixture(scope="module")
def scope_module():
    print('scope_module...每个py文件前执行')


def test_caseA(scope_module):
    print('this is a test_caseA')

class TestCase:

    def test_caseB(self, scope_module):
        print('this is a test_caseB')


if __name__ == '__main__':
    pytest.main(['-s', 'pytestdemo2.py'])