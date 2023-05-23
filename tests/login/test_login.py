import pytest
import logging


logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@pytest.mark.parametrize(
    "email, password, result",
    [
        ("non_Correct@o.com", "no_corr123", False),
        ("qa.ajax.app.automation@gmail.com", "password", False),
        ("noval@email.com", "qa_automation_password", False),
        ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True)
     ]
                         )
def test_user_login(user_login_fixture, email: str, password: str, result: bool) -> None:
    logging.info(f"Running test_user_login with email: {email}, password: {password}")
    assert user_login_fixture.login(email, password) == result
