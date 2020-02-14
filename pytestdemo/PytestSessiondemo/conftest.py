import pytest


@pytest.fixture(scope="module")
def scope_module():
    print('scope_module...每个py文件前执行')


@pytest.fixture(scope="session")
def scope_session():
    print('scope_session...多个py文件前只执行一次')


@pytest.fixture(scope="function")
def scope_function():
    print('scope_function...每个方法前执行')


@pytest.fixture(scope="class")
def scope_class():
    print('scope_class...每个类前执行')