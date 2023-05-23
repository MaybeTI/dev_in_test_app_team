import pytest
import logging

from appium.webdriver.common.mobileby import MobileBy

logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@pytest.mark.parametrize(
    "email, password, result",
    [
        ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True)
     ]
                         )
def test_sidebar(user_login_fixture, email: str, password: str, result: bool) -> None:
    logging.info(f"Running test_user_login with email: {email}, password: {password}")
    assert user_login_fixture.sidebar(email, password) == result
    assert user_login_fixture.find_element(MobileBy.ID, "com.ajaxsystems:id/addHub").text == "Add hub"
    assert user_login_fixture.find_element(MobileBy.ID, "com.ajaxsystems:id/settings").text == "App Settings"
    assert user_login_fixture.find_element(MobileBy.ID, "com.ajaxsystems:id/help").text == "Help"
    assert user_login_fixture.find_element(MobileBy.ID, "com.ajaxsystems:id/logs").text == "Report a problem"

