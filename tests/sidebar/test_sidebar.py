import pytest
import logging


logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@pytest.mark.parametrize(
    "email, password, result",
    [
        ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True)
     ]
                         )
def test_user_login(user_login_fixture, email: str, password: str, result: bool) -> None:
    logging.info(f"Running test_user_login with email: {email}, password: {password}")
    assert user_login_fixture.sidebar(email, password) == result
