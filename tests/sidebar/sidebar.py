import pytest


@pytest.mark.parametrize(
    "email, password, result",
    [
        ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True)
     ]
                         )
def test_user_login(user_login_fixture, email: str, password: str, result: bool) -> None:
    assert user_login_fixture.login(email, password) == result
