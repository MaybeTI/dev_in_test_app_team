import pytest
from appium.webdriver.webdriver import WebDriver

from framework.sidebar_page import SidebarPage


@pytest.fixture(scope="function")
def sidebar_fixture(driver: WebDriver) -> SidebarPage:
    yield SidebarPage(driver)
