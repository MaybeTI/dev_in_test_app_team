import pytest
import logging
from appium.webdriver.common.mobileby import MobileBy

from framework.sidebar_page import SidebarPage

logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@pytest.mark.parametrize(
    "email, password, add_hub, app_settings, _help, report_a_problem",
    [
        (
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            "Add hub",
            "App Settings",
            "Help",
            "Report a problem",
        )
    ],
)
def test_sidebar(
    sidebar_fixture: SidebarPage,
    email: str,
    password: str,
    add_hub: str,
    app_settings: str,
    _help: str,
    report_a_problem: str,
) -> None:
    logging.info(
        f"Running test_user_login with email: {email}, password: {password}"
    )
    sidebar_fixture.sidebar(email, password)

    elements = sidebar_fixture.find_element(
        MobileBy.CLASS_NAME, "android.widget.TextView", many=True
    )
    element_text_list = [element.text for element in elements]

    assert add_hub in element_text_list
    assert app_settings in element_text_list
    assert _help in element_text_list
    assert report_a_problem in element_text_list
