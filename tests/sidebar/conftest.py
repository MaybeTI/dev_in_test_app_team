import pytest

from framework.sidebar import Sidebar


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield Sidebar(driver)
