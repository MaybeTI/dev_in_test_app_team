from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from .page import Page


class LoginPage(Page):
    def login(self, email: str, password: str) -> bool:
        self.click_element(
            MobileBy.ID,
            "com.android.permissioncontroller:id/permission_allow_button",
        )
        self.click_element(MobileBy.ID, "com.ajaxsystems:id/authHelloLogin")
        self.send_keys(
            MobileBy.CLASS_NAME,
            "android.widget.EditText",
            True,
            email,
            password,
        )
        self.click_element(MobileBy.ID, "com.ajaxsystems:id/authLogin")
        try:
            self.click_element(
                MobileBy.ID,
                "com.android.permissioncontroller:id/permission_allow_foreground_only_button",
            )
            return True
        except (NoSuchElementException, TimeoutException):
            return False
