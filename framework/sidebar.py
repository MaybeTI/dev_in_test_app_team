from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from framework import LoginPage


class Sidebar(LoginPage):
    def sidebar(self, email, password):
        self.login(email, password)
        self.click_element(MobileBy.ID, "com.ajaxsystems:id/menuDrawer")

        try:
            self.click_element(MobileBy.ID, "com.ajaxsystems:id/settings")
            return True
        except (NoSuchElementException, TimeoutException):
            return False
