import pytest


class TestCase:
    @pytest.mark.parametrize('num', [1, 2, 3])
    def test_case_a(self, num):
        print('num: ', num)

    @pytest.mark.parametrize('num, num2', [(1, 2), (2, 3)])
    def test_case_b(self, num, num2):
        print('argname为字符串传入 num:', num, ' num2:', num2)

    @pytest.mark.parametrize('num', [1, 2])
    @pytest.mark.parametrize('num2', [2, 3])
    def test_case_c(self, num, num2):
        print('分开的argname num:', num, ' num2:', num2)

    @pytest.mark.parametrize(['num', 'num2'], [(1, 2), (2, 3)])
    def test_case_d(self, num, num2):
        print('argname为列表传入 num:', num, ' num2:', num2)

    @pytest.mark.parametrize(('num', 'num2'), [(1, 2), (2, 3)])
    def test_case_e(self, num, num2):
        print('argname为元组传入 num:', num, ' num2:', num2)


if __name__ == '__main__':
    pytest.main(['-s', 'pytestddt.py'])