from .page import Page
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class LoginPage(Page):
    def login(self, email, password):
        self.driver.click_on_element(MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        self.driver.click_on_element(MobileBy.ID, "com.ajaxsystems:id/authHelloLogin")
        self.driver.send_keys(MobileBy.CLASS_NAME, "android.widget.EditText", True, email, password)
        self.driver.click_on_element(MobileBy.ID, "com.ajaxsystems:id/authLogin")
        try:
            self.driver.click_on_element(
                MobileBy.ID,
                "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
            )
            return True
        except (NoSuchElementException, TimeoutException):
            return False
